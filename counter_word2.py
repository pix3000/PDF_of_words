import argparse
import PyPDF2
from googletrans import Translator

def count_word_occurrences(pdf_file, word):
    word_count = 0

    with open(pdf_file, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)

        for page in pdf_reader.pages:
            text = page.extract_text()
            word_count += text.lower().count(word.lower())

    return word_count


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Count word occurrences in a PDF document')
    parser.add_argument('pdf_file', type=str, help='Path to the PDF file')
    parser.add_argument('word', type=str, help='Word to count occurrences of')
    args = parser.parse_args()

    count = count_word_occurrences(args.pdf_file, args.word)
    print(f'The word "{args.word}" appears "{count}" times in the PDF document.')

translator = Translator()
translated =  translator.translate(f"{args.word}", src="en", dest="ko")
print(f"{args.word} -> {translated.text}")
