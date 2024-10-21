from kak_ia.core.commands import CommandProcessor
from kak_ia.core.voicer import VoiceRecognition
from kak_ia.core.gtts import TextToSpeech
from kak_ia.core.logging import setup_logging


class KakiaAssistant:
    def __init__(self):
        setup_logging()
        self.tts = TextToSpeech()
        self.vr = VoiceRecognition()
        self.command_processor = CommandProcessor(self.tts, self.vr)

    def run(self):
        self.tts.speak("Assistente Kakía foi ativada.")
        option = input(
            "Você deseja digitar o comando ou falar? (digitar/falar): "
        ).lower()
        while True:
            if option == "digitar":
                command = input("Comando: ").lower()
                self.command_processor.process_command(command, option)
            elif option == "falar":
                command = self.vr.get_command()
                self.command_processor.process_command(command, option)
