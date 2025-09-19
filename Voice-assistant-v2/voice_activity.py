import sounddevice as sd
import numpy as np

def voice_activity_detection(duration=2, samplerate=16000, threshold=0.01):
    print("Recording... VAD is active.")
    audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='float32')
    sd.wait()
    max_amplitude = np.max(np.abs(audio))
    print(f"Max amplitude detected: {max_amplitude:.4f}")
    if max_amplitude > threshold:
        print("Audio detected!")
        detected = True
    else:
        print("Audio not detected!")
        detected = False
        
    return detected



# if __name__ == "__main__":
#     voice_activity_detection(threshold=0.01)  # Adjust down until regular voice triggers
