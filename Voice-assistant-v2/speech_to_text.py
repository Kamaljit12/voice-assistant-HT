import speech_recognition as sr

# ===================== voice to text (STT)=================================
def speech_to_text(phrase_time_limit: int = None):
    """Converts speech from microphone to text."""
    speech = sr.Recognizer()
    print('Python is listening...')
    with sr.Microphone() as source:
        try:
            speech.adjust_for_ambient_noise(source, duration=0.5)
            audio = speech.listen(source, timeout=5, phrase_time_limit=phrase_time_limit)
            user_input = speech.recognize_google(audio)
            return user_input.lower()
        except sr.UnknownValueError:
            return None  # Return empty string if speech is unintelligible
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return None
        except sr.WaitTimeoutError:
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None
        

# if __name__ == "__main__":
#     text = speech_to_text()
#     if text:
#         print(text)
#     else:
#         print("Not found anything!")