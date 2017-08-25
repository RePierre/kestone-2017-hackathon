#!/usr/bin/env python3
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer


class QueryProcessor:
    def __init__(self):
        self._tokenizer = RegexpTokenizer(r'\w+')
        self._stop_words = set(stopwords.words('english'))

    def process(self, query):
        tokens = self._tokenizer.tokenize(query)
        tokens = self.remove_stop_words(tokens)
        return tokens

    def remove_stop_words(self, tokens):
        return [w for w in tokens if w.lower() not in self._stop_words]


class TfidfQuery:
    def __init__(self, tfidfindex, queryprocessor):
        self._tfidfindex = tfidfindex
        self._queryprocessor = queryprocessor

    def get_results(self, query):
        terms = self._queryprocessor.process(query)
        for term in terms:
            results = self._tfidfindex.search(term)
            print('Results for term [{:s}]:'.format(term))
            print_results(results, 1)


def print_results(results,
                  topic,
                  hackathonformat=False,
                  team='Data Wizards'):
    rank = 1
    for file, score in results:
        if hackathonformat:
            line = '{:d} Q0 {:s} {:d} {:s}'.format(topic, file, rank, team)
        else:
            line = '{:s} {:f}'.format(file, score)
        print(line)
        rank += 1
