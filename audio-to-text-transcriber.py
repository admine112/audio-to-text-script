🚀 Whisper Multilang Transcriber (with auto language detection, GPU, and optimal installation)

# ✅ Install Whisper and ffmpeg only if they are not already installed
import importlib.util
import subprocess

def is_installed(package):
    return importlib.util.find_spec(package) is not None

# Whisper
if not is_installed("whisper"):
    print("📦 Installing Whisper...")
    subprocess.run(["pip", "install", "-q", "git+https://github.com/openai/whisper.git"])
else:
    print("✅ Whisper is already installed")

# ffmpeg
res = subprocess.run(["which", "ffmpeg"], capture_output=True, text=True)
if not res.stdout.strip():
    print("📦 Installing ffmpeg...")
    subprocess.run(["apt", "update"])
    subprocess.run(["apt", "install", "-y", "ffmpeg"])
else:
    print("✅ ffmpeg is already installed")

# 💡 Import libraries
import whisper
import os
from google.colab import files
from IPython.display import display, Markdown

# 📌 GPU tip
display(Markdown("**💡 Tip:** Go to `Runtime → Change runtime type` and select `GPU` to speed up model performance.**"))

# 🧠 Load the model (can be changed to: tiny, base, medium, large)
model_size = "large"
print(f"📦 Loading model: {model_size}")
model = whisper.load_model(model_size)

# 📂 Upload audio files
print("⬆ Upload one or more audio files (MP3, WAV, etc.)")
uploaded = files.upload()

# 📝 Transcribe all files
for filename in uploaded.keys():
    print(f"🔍 Transcribing: {filename}")
    result = model.transcribe(filename)  # auto language detection
    text_filename = f"{os.path.splitext(filename)[0]}_transcript.txt"
    with open(text_filename, "w", encoding="utf-8") as f:
        f.write(result["text"])
    print(f"✅ Saved: {text_filename}")

# 📤 Automatically download all transcripts
print("📥 Downloading text files…")
for file in os.listdir():
    if file.endswith("_transcript.txt"):
        files.download(file)
