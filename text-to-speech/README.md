# Text to Speech MP4 Generator

This project reads text from a `.txt` file, converts it to speech using gTTS, and generates an MP4 video using MoviePy.

---

## 📦 Requirements

- Python 3.9+
- Homebrew (macOS)
- FFmpeg

---

## 🔧 Setup (macOS)

### 1. Install Python (Homebrew)

```bash
brew install python
```

### 2. Install FFmpeg

```bash
brew install ffmpeg
```

### 3. Create Virtual Environment

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install moviepy==1.0.3 gTTS
```

---

## ▶️ Run the App

Make sure venv is activated:

```bash
python textToSpeech.py
```

Or run directly:

```bash
venv/bin/python textToSpeech.py
```

# alt run script
./run.sh


---

## 📁 Project Structure

```
text-to-speech/
│
├── textToSpeech.py
├── media/input.txt
├── media/output.mp4
├── venv/
└── README.md
```

---

## ⚠️ Common Errors

### ModuleNotFoundError
Make sure you activated the virtual environment:

```bash
source venv/bin/activate
```

### MoviePy Import Error
Use version 1.0.3:

```bash
pip install moviepy==1.0.3
```

---

## 🧠 How It Works

1. Reads text from `input.txt`
2. Converts text to speech (MP3)
3. Combines audio with a background
4. Exports as MP4 video

## Howto write input file

- Tips for Better Audio Output
- Use punctuation (. , ! ?) → improves speech rhythm
- Add line breaks between paragraphs → clearer pauses
- Avoid very long sentences
- Keep numbers written as words if needed (e.g., “twenty five” instead of 25)

---