#!/usr/bin/env python
import numpy as np
import pandas as pd
from collections import Counter
import re, math
import sys
import time

start_time = time.time()
word = re.compile(r'\w+')
data = pd.read_csv('na100.tsv', header=None, sep='\t', engine='python')

def get_cosine(vec1, vec2): #calculation for cosine similarity
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])
    
    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([vec2[x]**2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)
    
    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator

def text_to_vector(text):
    words = word.findall(text)
    return Counter(words)

def main():
    ids = {}
    rows = data
    _u = lambda t: t.decode('UTF-8', 'replace') if isinstance(t, str) else t
    
    for row in data.values:
        id = row[0]
        text = row[3]
        ids[id] = "".join(text)
        
    for x,v1 in ids.items():
        for y,v2 in ids.items():
            if (x != y):
                vector1 = text_to_vector(v1)
                vector2 = text_to_vector(v2)
                score = get_cosine(vector1, vector2)
                score = "%10.5f" % score
                print(x, ",", y, ",", score, file = cosdata)
                

if __name__ == '__main__':
    cosdata = open("cosscore.csv", "w") 
    main()
    print(" %s seconds " % round(time.time() - start_time))