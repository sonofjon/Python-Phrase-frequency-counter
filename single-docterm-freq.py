# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 10:11:14 2017

@author: MStattelman
"""
import re
import string
import collections
from collections import Counter

frequency = {}
document_text = open('/home/andreas/projects/nltk-stuff/nltk_data/corpora/genesis/english-web.txt', 'r')
text_string = document_text.read().lower()
match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)

for word in match_pattern:
    count = frequency.get(word,0)
    frequency[word] = count + 1

frequency_list = frequency.keys()
od = collections.OrderedDict(sorted(frequency.items(),key=lambda t: t[1], reverse=True))

import pandas as pd
df = pd.DataFrame.from_dict(od, orient='index').reset_index()
df = df.rename(columns={'index':'Word', 0:'Count'})
#print (df)
df.to_html(open('SingleWord.html', 'w'))
#Convert to pdf.
#import pdfkit
#pdfkit.from_url('SingleWord.html', 'SingleWord.pdf')
