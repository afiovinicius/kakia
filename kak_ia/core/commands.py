import webbrowser
import time
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers.string import StrOutputParser


class CommandProcessor:
    def __init__(self, tts, vr):
        self.tts = tts
        self.vr = vr
        self.setup_chat()
        self.req_max = 30
        self.req_count = 0
        self.start_time = time.time()

    def setup_chat(self):
        template = """
        {text}
        """
        self.prompt = PromptTemplate.from_template(template=template)
        self.chat = ChatGroq(model="llama-3.1-70b-versatile")
        self.chain = self.prompt | self.chat | StrOutputParser()

    def ask_groq(self, question):
        if self.req_count >= self.req_max:
            elapsed_time = time.time() - self.start_time
            if elapsed_time < 60:
                wait_time = 60 - elapsed_time
                print(
                    f"Aguardando {int(wait_time)} segundos para reiniciar requisições..."
                )
                self.tts.speak(f"Aguardando {int(wait_time)} segundos.")
                time.sleep(wait_time)
            self.req_count = 0
            self.start_time = time.time()

        try:
            formatted_question = self.prompt.format(text=question)
            response = self.chain.invoke({"text": formatted_question})
            print(f"Retorno do modelo: {response}")
            self.req_count += 1
            return response
        except Exception as e:
            print(f"Erro ao consultar o modelo: {e}")
            self.tts.speak("Erro ao consultar o modelo.")
            return "Não consegui obter uma resposta agora."

    def process_command(self, command, opt):
        if "abrir youtube" in command:
            self.open_youtube(opt)
        elif "abrir google" in command:
            self.open_google(opt)
        elif "tchau" in command or "fechar" in command:
            self.tts.speak("Até a próxima!")
            exit(0)
        elif command:
            self.tts.speak("Deixe-me ver...")
            response = self.ask_groq(command)
            self.tts.speak(response)

    def open_youtube(self, opt):
        self.tts.speak("O que você deseja pesquisar no Youtube?")
        query = (
            input("Pesquisa no YouTube: ")
            if opt == "digitar"
            else self.vr.get_command()
        )
        if query:
            webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
            self.tts.speak(f"Pesquisando {query}.")
        else:
            self.tts.speak("Não entendi o que você deseja pesquisar.")

    def open_google(self, opt):
        self.tts.speak("O que você deseja pesquisar no Google?")
        query = (
            input("Pesquisa no Google: ") if opt == "digitar" else self.vr.get_command()
        )
        if query:
            webbrowser.open(f"https://www.google.com/search?q={query}")
            self.tts.speak(f"Pesquisando {query}.")
        else:
            self.tts.speak("Não entendi o que você deseja pesquisar.")
