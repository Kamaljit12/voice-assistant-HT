# Voice Assistant v2

A Python-based voice assistant with advanced barge-in capabilities, allowing users to interrupt the assistant's speech and provide new queries in real-time.

## Features

- **Speech-to-Text**: Converts user speech to text using Google Speech Recognition
- **Text-to-Speech**: Provides audio responses using platform-specific TTS engines
- **LLM Integration**: Powered by Groq's Llama 3.1 model for intelligent responses
- **Barge-in Support**: Users can interrupt the assistant mid-speech to ask follow-up questions
- **Voice Activity Detection**: Real-time detection of user speech during assistant responses
- **Cross-platform**: Works on Windows, Linux, and macOS

## Prerequisites

- Python 3.7 or higher
- Microphone access
- Internet connection (for Google Speech Recognition and Groq API)
- Groq API key

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd voice_assistant-v2
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root and add your Groq API key:
```
GROQ_API_KEY=your_groq_api_key_here
```

## Usage

### Basic Voice Assistant
Run the main voice assistant:
```bash
python main.py
```

The assistant will:
- Listen for your speech input
- Process your query using the LLM
- Respond with both text and speech
- Allow you to interrupt with barge-in functionality
- Continue the conversation until you say "stop"

### Alternative Implementation
You can also run the alternative barge-in implementation:
```bash
python burge_support.py
```

## Project Structure

```
voice_assistant-v2/
├── main.py                 # Main application entry point
├── speech_to_text.py       # Speech recognition using Google Speech API
├── text_to_speech.py       # Text-to-speech with cross-platform support
├── llm_response.py         # LLM integration with Groq API
├── voice_detection.py      # Voice activity detection
├── barge_support_v1.py     # Primary barge-in implementation
├── burge_support.py        # Alternative barge-in implementation
├── requirements.txt        # Python dependencies
├── demo.txt               # Demo configuration
└── README.md              # This file
```

## Key Components

### Speech-to-Text (`speech_to_text.py`)
- Uses Google Speech Recognition API
- Handles ambient noise adjustment
- Provides error handling for various speech recognition issues

### Text-to-Speech (`text_to_speech.py`)
- **Windows**: Uses `pyttsx3` for native TTS
- **Linux/macOS**: Uses `gTTS` with `mpg123` for audio playback
- Includes stop functionality for barge-in support

### LLM Response (`llm_response.py`)
- Integrates with Groq's Llama 3.1 8B Instant model
- Optimized prompts for voice assistant responses
- Configurable temperature for response creativity

### Voice Activity Detection (`voice_detection.py`)
- Real-time audio monitoring using `sounddevice`
- Configurable threshold and duration settings
- Detects user speech during assistant responses

### Barge-in Support (`barge_support_v1.py`)
- Multi-threaded TTS with interruption capability
- Continuous voice monitoring during speech
- Seamless transition to new user queries

## Configuration

### Environment Variables
- `GROQ_API_KEY`: Your Groq API key for LLM access

### Audio Settings
You can modify audio parameters in `voice_detection.py`:
- `duration`: Recording duration for voice detection
- `threshold`: Audio amplitude threshold for speech detection
- `samplerate`: Audio sample rate (default: 16000 Hz)

## Dependencies

- `sounddevice`: Audio recording and playback
- `numpy`: Audio signal processing
- `python-dotenv`: Environment variable management
- `pyttsx3`: Text-to-speech (Windows)
- `groq`: LLM API client
- `pyaudio`: Audio I/O
- `speechRecognition`: Speech-to-text functionality
- `torchvision` & `torchaudio`: Audio processing (optional)
- `openai-whisper`: Alternative STT (optional)
- `soundfile`: Audio file handling
- `silero`: TTS engine (optional)

## Troubleshooting

### Audio Issues
- Ensure your microphone is properly connected and recognized
- Check microphone permissions in your system settings
- Adjust the voice detection threshold if experiencing false positives/negatives

### API Issues
- Verify your Groq API key is correctly set in the `.env` file
- Check your internet connection for Google Speech Recognition
- Ensure you have sufficient API credits/quota

### Platform-Specific Issues
- **Windows**: Ensure `pyttsx3` is properly installed
- **Linux**: Install `mpg123` for audio playback: `sudo apt-get install mpg123`
- **macOS**: Install `mpg123` via Homebrew: `brew install mpg123`

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source. Please check the license file for details.

## Acknowledgments

- Google Speech Recognition API for speech-to-text
- Groq for LLM API access
- The Python community for excellent audio processing libraries
