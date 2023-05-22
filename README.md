# PDF_top_words
**find_words:** PDF 문서를 읽고 가장 많이 나온 단어를 내림차순으로 n개 출력해주는 파이썬 코드  
**counter_words:** PDF 문서를 읽고 입력한 단어가 전체에서 몇 번 나오는 지 출력해주는 파이썬 코드
  
# find_words.py
```
$ python3 find_words.py [path to pdf] -n [number of words] 
```  
**path to pdf:** pdf의 경로 지정  
**number of words:** 출력할 단어 개수 지정
<br/>
### Example
```
$ python3 find_words.py test.pdf -n 15
```  
## Result  
```
PDF NAME: test.pdf

object: 44
detection: 44
pages: 38
positive: 35
detectors: 29
label: 28
number: 27
based: 24
performance: 21
ResNeXt: 20
Proceedings: 20
optimal: 17
objects: 16
Table: 16
Vision: 16
```

  
  
# counter_words.py
```
$ python3 counter_words.py [path to pdf] [word] 
```  
**path to pdf:** pdf의 경로 지정  
**word:** 횟수를 알고 싶은 단어
<br/>
### Example
```
$ python3 find_words.py test.pdf correlated
```  
## Result  
```
The word "correlated" appears "2" times in the PDF document.
```
