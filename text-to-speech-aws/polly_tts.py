import boto3
import os
from pydub import AudioSegment

# Initialize Polly client
polly = boto3.client("polly")

# Function to chunk text into <=3000 characters
def chunk_text(text, max_length=3000):
    chunks = []
    while len(text) > max_length:
        # find a good split (end of sentence)
        split_index = text.rfind(".", 0, max_length)
        if split_index == -1:
            split_index = max_length
        chunks.append(text[:split_index + 1])
        text = text[split_index + 1:].lstrip()
    chunks.append(text)
    return chunks

def text_to_speech_from_file(input_file, voice="Joanna", output_file="output.mp3"):
    
    print(f"✅ Read in text file {input_file}")
    # Read text file
    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()

    chunks = chunk_text(text)
    audio_segments = []

    for i, chunk in enumerate(chunks):
        print(f"✅ chunk: {chunk}")
        response = polly.synthesize_speech(
            Text=chunk,
            VoiceId=voice,
            OutputFormat="mp3"
        )
        # Save each chunk temporarily
        chunk_filename = f"chunk_{i}.mp3"
        with open(chunk_filename, "wb") as f:
            f.write(response["AudioStream"].read())
        audio_segments.append(AudioSegment.from_mp3(chunk_filename))

    # Combine all audio chunks into one
    final_audio = sum(audio_segments)
    final_audio.export(output_file, format="mp3")

    # Clean up temporary files
    for i in range(len(audio_segments)):
        os.remove(f"chunk_{i}.mp3")

    print(f"✅ Final audio saved as {output_file}")

# Example usage
if __name__ == "__main__":
    text_to_speech_from_file("aws-question.txt", voice="Joanna", output_file="final_output.mp3")
