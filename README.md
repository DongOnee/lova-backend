LOVA Back-end Server
===
Hanyang Univ. 2019 Capstone Team LOVA.


# 1. Functions
## 1.1. Logical Validation
Logical Validation is Essay scoring API. It used a 'get method'. **essay_id** is object id of input Essay stored in  MongoDB.
### 1.1.1 usage
- `https://{URL}:{port}/lv/{essayID}`
- use **python 3.6** environment

## 1.2. Quote Extraction
'Quote Extraction API' can extract quotation in essay. It used a 'get method'. **essay_id** is object id of input Essay stored in  MongoDB.
### 1.2.1 usage
- `https://{URL}:{port}/ec/{essayID}`
- use **python 3.6** environment

## 1.3. Truth Judgement
'Truth Judgment API' is an API designed to determine the authenticity of a sentence. Extract keywords from sentences and compare them with documents from web crawling to provide help in determining authenticity.
### 1.3.1 usage
- `https://{URL}:{port}/tv`
- use **python 2.7** environment

****
# 2. python env
we use python 3 for Logical Validation and Quote Extraction, and python 2 for Truth Judgement
1. python 3.6.1 >=
    - ```conda install allennlp -c pytorch -c allennlp -c conda-forge```
    - ```pip install --ignore-install --upgrade tensorflow-gpu```
    - ```pip install tensorflow-hub```
    - ```pip install nltk```
    - ```conda install -c anaconda pymongo```
    - ```pip install gensim```
2. python 2.7
    - ```pip install nltk```
    - ```pip install rake-nltk```
    - ```pip install enum```
    - ```pip install vocabulary```
    - ```pip install BeautifulSoup4```
    - ```pip install pdfminer```
    - ```pip install tensorflow```
    - ```pip install gensim```
    - ```pip install word2vec```
