#!/usr/bin/env python3
from tfidfindex import TfidfIndex


def save_vocabulary(path='../data/vocabulary.txt'):
    index = TfidfIndex()
    index.index()
    with open(path, 'w') as output:
        for key in index.vocabulary.keys():
            output.write('{:s}\n'.format(key))
