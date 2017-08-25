#!/usr/bin/env python3
import glob
from os.path import basename
from os.path import splitext
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer


class TfidfIndex:
    def __init__(self):
        self._document_corpus = None
        self._count_vectorizer = CountVectorizer(input='filename')
        self._tfidf_transformer = TfidfTransformer(use_idf=True)
        self._tfidf_index = None
        self._filenames = None

    @property
    def vocabulary(self):
        return self._count_vectorizer.vocabulary_

    @property
    def tfidf_index(self):
        return self._tfidf_index

    @property
    def corpus(self):
        return self._document_corpus

    @property
    def filenames(self):
        if self._filenames is None:
            basenames = [basename(file) for file in self._document_corpus]
            names = [splitext(name) for name in basenames]
            self._filenames = [name for name, _ in names]
        return self._filenames

    def index(self, glob_pattern='../data/metadata*/**/*.txt'):
        print('Loading document corpus...')
        self._document_corpus = list(glob.iglob(glob_pattern))
        print('Done.')
        print('Building TF-IDF index...')
        count_vect = self._count_vectorizer.fit_transform(
            self._document_corpus)
        self._tfidf_index = self._tfidf_transformer.fit_transform(count_vect)
        print('Done.')

    def search(self, term):
        term_index = self.vocabulary[term]
        freq_matrix_slice = self.tfidf_index[:, term_index]
        documents = [(self.filenames[i], freq_matrix_slice[i, 0])
                     for i in range(len(self.corpus))
                     if freq_matrix_slice[i, 0] > 0]
        results = sorted(documents, key=lambda doc: doc[1], reverse=True)
        return results
