#!/usr/bin/env python
import numpy as np
import pandas as pd
from collections import Counter
import re, math
import sys
import time

#calculation of real time - impacted by other tasks run by CPU
start_time = time.time() 

#compile regex pattern for one or more alphanumeric characters
word = re.compile(r'\w+')

#read csv file into dataframe where t denotes tab separated file and parser engine of type python
data = pd.read_csv('na100.tsv', header=None, sep='\t', engine='python')

#calculation for cosine similarity
def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])
    
    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([vec2[x]**2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)
    
    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator

#conversion of text to vectors
def text_to_vector(text):
    words = word.findall(text)
    return Counter(words)

#Unicode text, go through each row and output to csv as similarity score between 0 & 1
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