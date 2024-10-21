import speech_recognition as sr

from kak_ia.core.gtts import TextToSpeech


class VoiceRecognition:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.tts = TextToSpeech()

    def get_command(self):
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source)
            print("Ouvindo...")
            self.recognizer.pause_threshold = 1.5
            try:
                audio = self.recognizer.listen(source)
                print("Reconhecendo...")
                command = self.recognizer.recognize_google(audio, language="pt-br")
                print(f"Usuário falou: {command}\n")
                return command.lower()
            except sr.UnknownValueError:
                print("Não entendi.")
                self.tts.speak("Não entendi.")
                return ""
            except sr.RequestError as e:
                print(f"Erro de conexão: {e}")
                self.tts.speak(f"Erro de conexão: {e}")
                return ""
            except Exception as e:
                print(f"Erro: {e}")
                self.tts.speak(f"Erro: {e}")
                return ""
