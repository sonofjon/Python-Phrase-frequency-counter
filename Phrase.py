# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 11:48:25 2017

@author: MStattelman
"""
import re
import os
import nltk
# import textract
import collections
from collections import Counter
from nltk import bigrams
from nltk import trigrams
#Use tweet tokenizer to prevent contracted words from spliting
from nltk.tokenize import TweetTokenizer

def remove_punctuation(text):
    """
    Removes all punctuation and conotation from the string and returns a 'plain' string
    """
    punctuation2 = '-&'+'®©™€â´‚³©¥ã¼•ž®è±äüöž!@#Â“§$%^*()î_+€$=¿{”}[]:«;"»\â¢|<>,.?/~`0123456789'
    for sign in punctuation2:
        text = text.replace(sign, " ")
    return text

# document_text = open('YOURDIRECTORY/YOURFILE', 'r')
document_text = open('/home/andreas/projects/nltk-stuff/nltk_data/corpora/genesis/english-web.txt', 'r')
document_text = open('https://career.odevo.com/jobs/1652504-linux-sys-admin', 'r')
text_string = document_text.read().lower()
Q = remove_punctuation(text_string)

# Comment out the above 3 lines and Uncomment the line below if you are using .docx, .pdf, .html, .pptx files
#Q = textract.process("YOURDIRECTORY/YOURFILE.extension")
# Q = open('/home/andreas/projects/nltk-stuff/nltk_data/corpora/genesis/english-web.txt', 'r')

tknzr = TweetTokenizer()
tokens = tknzr.tokenize(Q)
unigrams = {}
for token in tokens:
  if token not in unigrams:
    unigrams[token] = 1
  else:
    unigrams[token] += 1
bi_tokens = Counter(bigrams(tokens))
tri_tokens = Counter(trigrams(tokens))

od = collections.OrderedDict(tri_tokens.most_common())
import pandas as pd
df = pd.DataFrame.from_dict(od, orient='index').reset_index()
df = df.rename(columns={'index':'3 Word Phrase', 0:'Count'})

df.to_html(open('Phrases.html', 'w'))
#Convert to pdf.
# import pdfkit
# pdfkit.from_url('Phrases.html', 'Phrases.pdf')
