# audio-to-text-script
This script is a universal transcriber powered by OpenAI’s Whisper model. It automatically detects the language of the audio and converts speech into text.
Features:

- Checks if Whisper and ffmpeg are installed and installs them if necessary.

- Runs in Google Colab, allowing direct upload of audio files.

- Supports GPU acceleration for faster processing.

- Lets you choose the model size (tiny, base, medium, large), with "large" selected here.

- Processes all uploaded audio files, transcribes them, and saves the results as text files.

- Automatically downloads the generated transcripts to the user’s computer.
