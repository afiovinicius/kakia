from kak_ia.core.assistant import KakiaAssistant
from dotenv import load_dotenv, find_dotenv


_ = load_dotenv(find_dotenv())


if __name__ == "__main__":
    assistant = KakiaAssistant()
    assistant.run()
