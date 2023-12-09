
# Audio Transcription and Text Cleaning Project

## Description
This project consists of two main components: 
1. A script (`audio_transcriber.py`) to transcribe audio files into text by splitting them into manageable chunks.
2. A script (`clean_transcript.py`) to clean the transcribed text by capitalizing sentences and performing basic cleanup.

## Requirements
- Python 3.x
- `pydub` library
- `speech_recognition` library
- `spaCy` library and its English language model

## Installation

### Install Python Dependencies
Ensure you have Python installed on your system. Then, install the required Python libraries using the following commands:

```bash
pip install pydub speech_recognition spacy
```

### Install spaCy Language Model
Download the English language model for spaCy:

```bash
python -m spacy download en_core_web_sm
```

### FFmpeg
`pydub` requires FFmpeg for handling audio files. Install FFmpeg following the instructions for your operating system.

## Usage

### Audio Transcription
Run `audio_transcriber.py` to transcribe an audio file. The script splits the audio into chunks (default is 60 seconds) and transcribes each chunk.

```bash
python audio_transcriber.py <path_to_audio_file> -d <chunk_duration_in_seconds> -o <output_text_file>
```

- `<path_to_audio_file>`: Path to the audio file you want to transcribe.
- `<chunk_duration_in_seconds>` (optional): Duration of each audio chunk in seconds. Default is 60 seconds.
- `<output_text_file>` (optional): Path to save the transcribed text. Defaults to `outputs/filename.txt` where `filename` is the name of the audio file.

### Text Cleaning
Run `clean_transcript.py` to clean the transcribed text file. The script capitalizes sentences and performs basic text cleanup.

```bash
python clean_transcript.py <path_to_transcribed_file> -o <path_to_output_cleaned_file>
```

- `<path_to_transcribed_file>`: Path to the transcribed text file.
- `<path_to_output_cleaned_file>` (optional): Path to save the cleaned text file. Defaults to the input filename with a `_cleaned` suffix.

## Note
The text cleaning script performs basic cleanup and may not add punctuation or correct all errors accurately. Manual review is recommended for high accuracy requirements.