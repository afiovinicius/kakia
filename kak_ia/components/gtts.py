import os
from gtts import gTTS


class TextToSpeech:
    def __init__(self):
        self.lang = "pt"
        self.audio_file = "audio.mp3"

    def speak(self, audio):
        tts = gTTS(text=audio, lang=self.lang, slow=False)
        tts.save(self.audio_file)
        os.system(f"mpg123 {self.audio_file}")
        os.remove(self.audio_file)
