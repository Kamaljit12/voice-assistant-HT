# ============== STT
import speech_recognition as sr


def speech_to_text(phrase_time_limit: int=None):
    speech = sr.Recognizer()
    print("🎤 Listening Please speak...")

    with sr.Microphone() as source:

        try:
            speech.adjust_for_ambient_noise(source)
            audio = speech.listen(source, phrase_time_limit=phrase_time_limit)
            user_input = speech.recognize_google(audio)
            return f"[User]: {user_input}"
        except sr.UnknownValueError:
            return ""  # Return empty string if speech is unintelligible
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return ""
        except sr.WaitTimeoutError:
            return ""
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return ""
    