from text_to_speech import text_to_speech, stop_tts
from voice_detection import voice_activity_detection
from speech_to_text import speech_to_text
import threading
import time

# ================== BARGE-IN TTS ==================
def speak_with_barge_in(text):
    interrupted = threading.Event()
    user_text = [None]  # to store user speech if detected

    def tts_play():
        text_to_speech(text)

    tts_thread = threading.Thread(target=tts_play)
    tts_thread.start()

    while tts_thread.is_alive():
        if voice_activity_detection(duration=0.4, threshold=0.4):
            print("🎤 Possible user speech detected, recording for 3s...")
            
            # Record 3 seconds and convert to text
            new_input = speech_to_text()  # your function already uses phrase_time_limit=5, modify if needed
            if new_input:
                print(f"✅ User actually spoke: {new_input}")
                stop_tts()
                user_text[0] = new_input
                interrupted.set()
                break
            else:
                print("❌ Noise detected, ignoring. Continuing TTS...")

        time.sleep(0.15)

    tts_thread.join()

    return user_text[0]  # return new user input if captured, else None