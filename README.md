# PDF_top_words
PDF 문서를 읽고 가장 많이 나온 단어를 내림차순으로 n개 출력해주는 파이썬 코드

## Test
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
which: 27
number: 27
based: 24
performance: 21
ResNeXt: 20
Proceedings: 20
optimal: 17
objects: 16
Table: 16
```
