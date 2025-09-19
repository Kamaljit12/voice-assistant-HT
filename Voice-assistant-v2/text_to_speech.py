# ==================TTS
import pyttsx3
import platform
import os

if platform.system() == "Windows":
    import pyttsx3
    engine = pyttsx3.init()
    def text_to_speech(text):
        engine.say(text)
        # engine.save_to_file(filename="output.wav", text=text)
        engine.runAndWait()
    def stop_tts():
        engine.stop()
else:
    # On non-Windows systems (Linux/macOS), use gTTS and mpg123
    # You will need to install gTTS and mpg123:
    # pip install gTTS
    # On Linux: sudo apt-get install mpg123
    # On macOS: brew install mpg123
    from gtts import gTTS
    def text_to_speech(text):
        tts = gTTS(text, lang='en')
        tts.save("temp_speech.mp3")
        os.system("mpg123 -q temp_speech.mp3")
        # os.remover("temp_speech.mp3")
    def stop_tts():
        pass # Not stoppable directly with mpg123

# text_to_speech(text="Hello My name is kamal jit singh. I am a data sciectiest and AI Engineer!")