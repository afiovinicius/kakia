import pyttsx3


class TextToSpeech:
    def __init__(self):
        self.engine = pyttsx3.init("espeak")
        self.engine.setProperty("rate", 180)
        self.engine.setProperty("volume", 0.80)
        self.engine.setProperty("voice", self.engine.getProperty("voices")[95].id)

    def speak(self, audio):
        self.engine.say(audio)
        self.engine.runAndWait()
