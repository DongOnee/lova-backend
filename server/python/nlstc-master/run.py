import sys
import nlstc
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--vocab-path", dest="vocabs", type=str, metavar='<str>', required=True,
                    help="The path to the vocabulary")
parser.add_argument("-m", "--model-path", dest="models", type=str, metavar='<str>', required=True,
                    help="The path to the models")
parser.add_argument("-s", "--sentence", dest="sentence", type=str, metavar='<str>', default="According to the report, the results of an EDA survey in China complied by analyst Nancy Wu, consumer electronics applications were the primary design market in China in 2005, replacing telecommunications/data communications, which fell to third place behind industrial controls.",
                    help="The sentence")
args = parser.parse_args()

sentence = args.sentence
vocab_file = args.vocabs
model_file = args.models
nlstc.truth_check(sentence, vocab_file, model_file, process_debug=False)
exit()

try :
    sentence = args.sentence
    vocab_file = args.vocabs
    model_file = args.models
    nlstc.truth_check(sentence, vocab_file, model_file, process_debug=False)
except :
    print "you can use this form - python nlstc.py 'sentence' 'vocabulary file path' 'model file path'"
    exit()
