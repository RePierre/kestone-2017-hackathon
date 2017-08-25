#!/usr/bin/env python3
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import numpy as np


class QueryProcessor:
    def __init__(self):
        self._tokenizer = RegexpTokenizer(r'\w+')
        self._stop_words = set(stopwords.words('english'))

    def process(self, query):
        tokens = self._tokenizer.tokenize(query)
        tokens = self.remove_stop_words(tokens)
        tokens = set(tokens)
        return tokens

    def remove_stop_words(self, tokens):
        return [w for w in tokens if w.lower() not in self._stop_words]


class TfidfQuery:
    def __init__(self, tfidfindex, queryprocessor):
        self._tfidfindex = tfidfindex
        self._queryprocessor = queryprocessor

    def get_results(self, query):
        terms = self._queryprocessor.process(query)
        dict = {}
        for term in terms:
            results = self._tfidfindex.search(term)
            dict[term] = results
        results = self.compute_score(dict)
        return sorted(results, key=lambda doc: doc[1], reverse=True)

    def compute_score(self, dict):
        # pdb.set_trace()
        document_names = self.get_document_names(dict)
        terms = self.get_term_indices(dict)
        score_matrix = np.zeros((len(document_names),
                                len(terms)))

        for term in dict:
            results = dict[term]
            term_index = terms[term]
            for name, score in results:
                name_index = document_names[name]
                score_matrix[name_index, term_index] = score

        results = []
        for document in document_names:
            index = document_names[name]
            score = np.sum(score_matrix[index, :])
            results.append((document, score))
        return results

    def get_term_indices(self, dict):
        terms = {}
        for term in dict:
            if term not in terms:
                terms[term] = len(terms)
        return terms

    def get_document_names(self, dict):
        names = {}
        for value in dict.values():
            for name, _ in value:
                if name not in names:
                    names[name] = len(names)
        return names
