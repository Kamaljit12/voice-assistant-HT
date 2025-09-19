# ======================= VAD Testing ============================
import sounddevice as sd
import numpy as np

def voice_activity_detection(duration=2, samplerate=16000, threshold=0.6):
    """
    Detects if any significant sound is present (not just silence).
    Returns True if sound is detected, else False.
    """
    print("Recording... VAD is active.")
    audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='float32')
    sd.wait()

    # Check the max absolute amplitude
    max_amplitude = np.max(np.abs(audio))
    print(f"Max amplitude detected: {max_amplitude:.4f}")
    if max_amplitude > threshold:
        print("Audio detected!")
        # sd.play(audio, samplerate)
        sd.wait()
        detected = True
    else:
        print("Audio not detected!")
        detected = False
    
    return detected
        