import time
import pyttsx3
import webbrowser
import speech_recognition as sr
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers.string import StrOutputParser
from dotenv import load_dotenv, find_dotenv


# Carregar variáveis de ambiente
_ = load_dotenv(find_dotenv())

# Configurações de texto e voz
template = """
{text}
"""
engine = pyttsx3.init("espeak")
engine.setProperty("voice", engine.getProperty("voices")[0].id)
# Configuração do modelo GROQ
prompt = PromptTemplate.from_template(template=template)
chat = ChatGroq(model="llama-3.1-70b-versatile")
chain = prompt | chat | StrOutputParser()
# Controle de limite de requisições
req_max = 30  # Limite de requisições por minuto
req_count = 0
start_time = time.time()


# Função para falar o texto
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# Função para escutar comandos de voz
def get_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Ouvindo...")
        r.pause_threshold = 1
        try:
            audio = r.listen(source)
            print("pausa começo")
            print("Reconhecendo...")
            command = r.recognize_google(audio, language="pt-br")
            print(f"Usuário falou: {command}\n")
            return command.lower()
        except sr.UnknownValueError:
            print("Não entendi.")
            speak("Desculpe, não entendi.")
            return ""
        except sr.RequestError as e:
            print(f"Erro de conexão: {e}")
            return ""
        except Exception as e:
            print(f"Erro: {e}")
            speak("Desculpe, ocorreu um erro ao tentar ouvir.")
            return ""


# Função para processar as perguntas usando o modelo da GROQ
def ask_groq(question):
    global req_count, start_time

    if req_count >= req_max:
        elapsed_time = time.time() - start_time
        if elapsed_time < 60:
            wait_time = 60 - elapsed_time
            print(f"Aguardando {int(wait_time)} segundos para reiniciar requisições...")
            speak(f"Aguardando {int(wait_time)} segundos.")
            time.sleep(wait_time)
        req_count = 0
        start_time = time.time()

    try:
        formatted_question = prompt.format(text=question)
        response = chain.invoke({"text": formatted_question})
        print(f"Retorno do modelo: {response}")
        req_count += 1
        return response
    except Exception as e:
        print(f"Erro ao consultar o modelo: {e}")
        speak(f"Erro ao consultar o modelo: {e}")
        return "Não consegui obter uma resposta agora."


# Função principal para processar os comandos
def process_command(command, opt):
    if "abrir youtube" in command:
        speak("O que você deseja pesquisar no Youtube?")
        query = input("Pesquisa no YouTube: ") if opt == "digitar" else get_command()
        if query:
            webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
            speak(f"Pesquisando {query}.")
        else:
            speak("Não entendi o que você deseja pesquisar.")
    elif "abrir google" in command:
        speak("O que você deseja pesquisar no Google?")
        query = input("Pesquisa no Google: ") if opt == "digitar" else get_command()
        if query:
            webbrowser.open(f"https://www.google.com/search?q={query}")
            speak(f"Pesquisando {query}.")
        else:
            speak("Não entendi o que você deseja pesquisar.")

    elif "tchau" in command or "fechar" in command:
        speak("Tchau Tchau!")
        exit(0)

    elif command:
        speak("Deixe-me ver...")
        response = ask_groq(command)
        speak(response)


# Função para ativar a assistente com o comando "Ei Kakía"
def activate_assistant():
    option = input("Você deseja digitar o comando ou falar? (digitar/falar): ").lower()
    while True:
        if option == "digitar":
            command = input("Comando: ").lower()  # Input para comando digitado
            process_command(command, option)

        elif option == "falar":
            command = get_command()  # Comando de voz
            process_command(command, option)


# Início do programa
if __name__ == "__main__":
    speak("Assistente Kakía foi ativada.")
    activate_assistant()
