from speech_to_text import speech_to_text
from llm_response import generate_response
from barge_support_v1 import speak_with_barge_in

def main():
    print("🤖 Voice assistant started. Say 'stop' to quit.")


    while True:
        print("\n🎤 Waiting for user speech...")
        user_input = speech_to_text()

        if not user_input:
            continue

        if "stop" in user_input.lower():
            print("👋 Exiting voice assistant.")
            break

        print(f"🧑 You: {user_input}")

        # Get LLM response
        response = generate_response(user_input)
        print(f"🤖 Assistant: {response}")

        # Speak with barge-in
        new_input = speak_with_barge_in(response)

        # If user interrupted, process new query immediately
        if new_input:
            print(f"🧑 (Interrupted) You: {new_input}")
            follow_up = generate_response(new_input)
            print(f"🤖 Assistant: {follow_up}")
            speak_with_barge_in(follow_up)



if __name__=="__main__":
    main()