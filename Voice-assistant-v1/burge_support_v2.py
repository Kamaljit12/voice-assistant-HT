from text_to_speech import text_to_speech, stop_tts
from voice_detection import voice_detection
from llm_response import generate_response
import threading
import time


def barge_in_voice_assistant():
    exit_words = ["stop", "exit", "quit"]
    last_input = "Hello! How can I assist you today?"
    stop_event = threading.Event()

    def tts_worker(text, stop_event):
        text_to_speech(text)
        stop_event.set()  # Signal done

    while True:
        stop_event.clear()
        tts_thread = threading.Thread(target=tts_worker, args=(last_input, stop_event))
        tts_thread.start()

        # Run detection loop in foreground so STT does not block within detection window
        detected_text = None
        while tts_thread.is_alive():  
            sound_text = voice_detection()  # listens for 3 seconds for voice
            if sound_text:
                detected_text = sound_text.replace("[User]:", "").strip()
                print(f"Detected user: {detected_text}")
                # Barge in! Stop the TTS and break the TTS loop
                stop_tts()
                if sound_text in exit_words:
                    print("You said to exit goodbye")
                    text_to_speech(text=detected_text)
                    stop_tts()
                    time.sleep(0.3)
                    break

            time.sleep(0.3)  # Slight pause to prevent busy looping

        tts_thread.join()  # Ensure TTS thread finishes or is stopped
        
        # If user said "stop", exit
        if detected_text and any(word in detected_text.lower() for word in exit_words):
            print("Assistant exiting as per user's request.")
            stop_tts()
            break

        # If no speech detected during TTS playback
        if not detected_text:
            reply_text = "I didn’t get what you said. Please speak loudly."
            print(reply_text)
            last_input = reply_text
            continue

        # If new, non-exit text—call LLM and start a new TTS loop
        reply_text = generate_response(detected_text)
        print(f"Assistant reply: {reply_text}")
        last_input = reply_text

# Run the assistant!
if __name__ == "__main__":
    barge_in_voice_assistant()
