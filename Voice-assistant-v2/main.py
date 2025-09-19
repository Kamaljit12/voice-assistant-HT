from barge_in import speak_with_barge_in
from llm_response import generate_response
from speech_to_text import speech_to_text

def main():
    exit_commands = {
        "exit", "stop", "stop listening", "bye", "goodbye", "good bye", "ok done"
    }

    while True:
        user_input = speech_to_text()
        if user_input and user_input.strip():
            cmd = user_input.strip().lower()
            if cmd in exit_commands:
                print(f"You said '{user_input}'. So goodbye!")
                speak_with_barge_in(text=f"You said '{user_input}'. So goodbye!")
                break
            else:
                print("Agent is speaking with barge-in support...")
                try:
                    response = generate_response(user_input=user_input)
                except Exception as e:
                    response = "Sorry, I couldn't generate a response due to an error."
                    print(f"LLM Error: {str(e)}")
                speak_with_barge_in(text=response)
        else:
            print("Did not receive any input from the user...")
            speak_with_barge_in(text="I didn't get anything, please speak loudly.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nAssistant stopped by user.")
