import threading
import time
from speech_to_text import speech_to_text
from voice_activity import voice_activity_detection
from text_to_speech import text_to_speech, stop_tts

def record_probe_stt(duration=3):
    """Record a short chunk and return text if speech is detected, else ''."""
    return speech_to_text(phrase_time_limit=duration)

def stt_until_silence(silence_limit=1.0):
    """Continue transcribing user utterance as long as they speak."""
    # Your implementation may use VAD/energy threshold logic here
    texts = []
    while True:
        text = speech_to_text(phrase_time_limit=3)
        if text:
            texts.append(text)
            # Continue listening, as long as voice_activity_detection is positive
            # Use your custom logic or adjust below as needed:
            if not voice_activity_detection():
                break
        else:
            break
    return " ".join(texts).strip()

def speak_with_barge_in(text):
    """
    TTS and VAD run in parallel.
    When VAD triggers, record 3s and STT.
        - If speech is detected (text), stop TTS, run full STT until silence, return user speech.
        - If noise/None, let TTS continue.
    """
    interrupted = threading.Event()
    user_utterance = [None]  # Mutable holder to return detected text

    def tts_play():
        text_to_speech(text)

    tts_thread = threading.Thread(target=tts_play)
    tts_thread.start()

    try:
        while tts_thread.is_alive():
            if voice_activity_detection():
                print("[Barge-in candidate detected: probing 3s for voice...]")
                probe_text = record_probe_stt(duration=3)
                if probe_text:
                    print(f"[User speech detected: '{probe_text.strip()}'. Interrupting TTS.]")
                    stop_tts()
                    interrupted.set()
                    # Now do continuous STT as long as user speaks (until silence)
                    user_input = stt_until_silence()
                    user_utterance[0] = user_input if user_input else probe_text
                    break
                else:
                    # Noise or silence: do not interrupt, let TTS continue
                    print("[VAD: Only noise detected, TTS continues.]")
                    continue
            else:
                # No VAD: just yield execution, let TTS continue
                time.sleep(0.05)
        tts_thread.join()
    except Exception as e:
        stop_tts()
        tts_thread.join()
        raise e

    if interrupted.is_set():
        print("[User finished barge-in speech.]")
        return user_utterance[0]
    else:
        print("[No barge-in, TTS finished normally.]")
        return None

# Example usage:

# if __name__=="__main__":
#     result = speak_with_barge_in("Hello, how can I help you?")
#     print("Barge-in user said:", result)
