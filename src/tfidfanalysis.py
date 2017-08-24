#!/usr/bin/env python3
import glob
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

glob_pattern = '../data/metadata*/**/*.txt'

files = list(glob.iglob(glob_pattern))
count_vectorizer = CountVectorizer(input='filename')
count_vect = count_vectorizer.fit_transform(files)

idx_radium = count_vectorizer.vocabulary_['radium']
print("Trained counts shape: ")
print(count_vect.shape)
print("Index of 'radium': %s" % (idx_radium))

tf_transformer = TfidfTransformer(use_idf=True)
train_tfidf = tf_transformer.fit_transform(count_vect)
train_tfidf.shape

radium_related = train_tfidf[:, idx_radium]
[(file, score) for file, score in zip(files, radium_related)]


def search(term):
    term_index = count_vectorizer.vocabulary_[term]
    frequency_matrix_slice = train_tfidf[:, term_index]
    filenames = [os.path.split(file)[1] for file in files]
    documents = [(filenames[i], frequency_matrix_slice[i, 0])
                 for i in range(len(files))
                 if frequency_matrix_slice[i, 0] > 0]
    ordered = sorted(documents, key=lambda doc: doc[1], reverse=True)
    return ordered


def print_results(results):
    for file, score in results:
        line = '{:s} {:f}'.format(file, score)
        print(line)
