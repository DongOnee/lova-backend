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

### Truth Validation
1. ```https://localhost:4000/tv/*essayId*```
2. requirements
    - argparse
    - nltk
    - numpy
    - gc
    ...

### Claim Extract
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
