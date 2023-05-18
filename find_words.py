import argparse
import re
import PyPDF2
from collections import Counter

def get_most_common_words(file_path, num_words=10):
    # PDF 문서 열기
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        
        # 모든 페이지의 텍스트 추출
        text = ''
        for page in reader.pages:
            text += page.extract_text()
        
        # 숫자, 전치사, 문장기호, 3자리 미만 단어 제외한 단어 추출
        words = re.findall(r'\b(?!(?:in|on|at|for|to|with|a|an|the|[.,!?;:]|\d|\b\w{1,2}\b))\w+\b', text, flags=re.IGNORECASE)
        
        # 단어 빈도수 계산
        word_counter = Counter(words)
        
        # 가장 많이 나온 단어들 반환
        return word_counter.most_common(num_words)

# 커맨드 라인 인자 처리
parser = argparse.ArgumentParser(description='Extract most common words from a PDF document')
parser.add_argument('pdf_file', type=str, help='Path to the PDF file')
parser.add_argument('-n', '--num_words', type=int, default=10, help='Number of most common words to display')
args = parser.parse_args()

# 가장 많이 나온 단어 출력
most_common_words = get_most_common_words(args.pdf_file, args.num_words)
for word, count in most_common_words:
    print(f'{word}: {count}')