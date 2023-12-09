import os
import sys
import argparse
from pydub import AudioSegment
import speech_recognition as sr

def split_audio(file_path, chunk_length_ms):
    """Splits the audio file into chunks of the specified length."""
    audio = AudioSegment.from_file(file_path)
    return [audio[i:i+chunk_length_ms] for i in range(0, len(audio), chunk_length_ms)]

def transcribe_audio(audio_chunk, language="fr-FR"):
    """Transcribes a single chunk of audio."""
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_chunk) as source:
        audio_data = recognizer.record(source)
        return recognizer.recognize_google(audio_data, language=language)

def main(audio_path, chunk_length, output_path, language):
    # Split audio into chunks
    audio_chunks = split_audio(audio_path, chunk_length * 1000)

    # Process each chunk and collect transcripts
    transcripts = []
    for i, chunk in enumerate(audio_chunks):
        # Save chunk as a temporary WAV file
        chunk_path = f"temp_chunk_{i}.wav"
        chunk.export(chunk_path, format='wav')

        # Transcribe and add to the list
        try:
            transcript = transcribe_audio(chunk_path, language)
            transcripts.append(transcript)
        except Exception as e:
            print(f"Error transcribing chunk {i}: {e}")

        # Remove the temporary file
        os.remove(chunk_path)

    # Merge transcripts into the specified output file
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as file:
        for transcript in transcripts:
            file.write(transcript + "\n\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Transcribe audio files into text.")
    parser.add_argument("audio_path", help="Path to the audio file.")
    parser.add_argument("-d", "--duration", type=int, default=60, help="Chunk duration in seconds (default: 60).")
    parser.add_argument("-o", "--output", help="Output file path (default: outputs/filename.txt).")
    parser.add_argument("-l", "--language", help="Language spoken (default: fr-FR).", default='fr-FR', type=str)
    args = parser.parse_args()

    # Determine the output file path
    output_path = args.output
    if not output_path:
        base_name = os.path.splitext(os.path.basename(args.audio_path))[0]
        output_path = f"outputs/{base_name}.txt"

    main(args.audio_path, args.duration, output_path, args.language)