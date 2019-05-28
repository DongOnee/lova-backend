# LOVA Back-end Server

### Logical Validation
1. ```https://localhost:4000/lv/*essayID*```
2. requirements
    - python==3.6
    - tensorflow==1.13.1
    - tensorflow-hub
    - nltk
    - pymongo
    - bson

### Truth Judgment
1. ```https://localhost:4000/tv/*essayId*```
2. requirements
    - argparse
    - nltk
    - numpy
    - gc
    ...

### Quote Extract
1. ```https://localhostd:4000/ec/*essayId*```
2. requirements
    - nltk
    - tensorflow
    - pandas
    - gensim
    - pymongo
    - git clone http://github.com/ioatr/textcnn.git
    - mv textcnn text_cnn_
    - mv text_cnn_/textcnn text_cnn_/TextCNN

### python env
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
