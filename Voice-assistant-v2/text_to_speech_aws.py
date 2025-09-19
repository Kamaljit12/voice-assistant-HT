import os
import simpleaudio as sa
import boto3
from dotenv import load_dotenv

load_dotenv()

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_DEFAULT_REGION = os.getenv("AWS_DEFAULT_REGION", "us-east-1")

session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_DEFAULT_REGION
)
polly_client = session.client("polly")

# Global for current playback
_current_play_obj = None

def text_to_speech(text, voice_id="Kajal", rate=16000):
    global _current_play_obj
    response = polly_client.synthesize_speech(
        Text=text,
        OutputFormat="pcm",
        VoiceId=voice_id,
        LanguageCode='en-IN',
        Engine='neural',  # Required for Kajal!
        SampleRate=str(rate)
    )
    if "AudioStream" in response:
        audio_stream = response["AudioStream"].read()
        play_obj = sa.play_buffer(audio_stream, 1, 2, rate)
        _current_play_obj = play_obj
        play_obj.wait_done()
        _current_play_obj = None

def stop_tts():
    global _current_play_obj
    if _current_play_obj is not None and _current_play_obj.is_playing():
        _current_play_obj.stop()
        _current_play_obj = None



if __name__ == "__main__":
    import threading
    import time

    # Play TTS in a thread so you can call stop_tts() while it's playing
    def play():
        text_to_speech("Hello, how are you. I am Kajal. How can I help you?, I am kajal how can i help you. if you have any query please let me know.")
    t = threading.Thread(target=play)
    t.start()
    time.sleep(5)   # Let it play for 2 seconds
    print("Stopping TTS!")
    stop_tts()
    t.join()
