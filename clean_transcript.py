import spacy
import argparse
import re

def clean_transcript(input_file, output_file):
    # Load the spaCy model for sentence tokenization
    nlp = spacy.load("en_core_web_sm")

    # Read the input file
    with open(input_file, 'r') as file:
        text = file.read()

    # Process the text with spaCy to get sentence boundaries
    doc = nlp(text)
    sentences = [sent.text.strip() for sent in doc.sents]

    # Capitalize each sentence
    capitalized_sentences = [sentence.capitalize() for sentence in sentences]

    # Join the sentences back into a single string
    cleaned_text = ' '.join(capitalized_sentences)

    # Write the cleaned text to the output file
    with open(output_file, 'w') as file:
        file.write(cleaned_text)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Clean up a transcribed text file.")
    parser.add_argument("input_file", help="Path to the input .txt file.")
    parser.add_argument("-o", "--output", help="Path to the output .txt file. Defaults to input filename with '_cleaned' suffix.")
    args = parser.parse_args()

    # Determine the output file path
    output_file = args.output
    if not output_file:
        output_file = re.sub(r'(\.txt)$', r'_cleaned\1', args.input_file)

    clean_transcript(args.input_file, output_file)