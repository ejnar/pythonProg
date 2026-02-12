from gtts import gTTS
from moviepy.editor import *

# Step 1: Read text file
with open("media/input.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Step 2: Convert text to speech
tts = gTTS(text=text, lang='en')
tts.save("media/audio.mp3")

# Step 3: Create video with background color
audio = AudioFileClip("media/audio.mp3")
video = ColorClip(size=(1280,720), color=(0,0,0), duration=audio.duration)
video = video.set_audio(audio)

# Step 4: Export to MP4
video.write_videofile("media/output.mp4", fps=24)