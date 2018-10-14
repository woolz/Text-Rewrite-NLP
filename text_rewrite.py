
__author__ = 'woolz'
__git__ = 'https://github.com/woolz/Text-Rewrite-NLP'

from spacy.tokenizer import Tokenizer
from spacy.lang.en.examples import sentences
from best_syn import *


class TextRewrite:


    def __init__(self, sentence):
        self.sentence = sentence

    def work(self):
        """
        @var rewrite_types: Type of words that can rewrited 
        """
        rewrite_types = [u'NN', u'NNS', u'JJ', u'JJS']
        pos_tokenizer = nlp(unicode(self.sentence))
        words = []
        for token in pos_tokenizer:
            #print(token.pos_, token.text, token.tag_)
            if token.tag_ in rewrite_types:
                words.append(token.text)
        rewrited_sentence = self.sentence
        for word in words:
            word_syn = BestSyn(word).pull()[1]
            rewrited_sentence = rewrited_sentence.replace(word, word_syn)
        return rewrited_sentence

    def __del__(self):
        self.sentence = False

