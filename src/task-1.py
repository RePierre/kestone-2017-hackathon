#!/usr/bin/env python3
from tfidfindex import TfidfIndex
from queryprocessing import TfidfQuery
from queryprocessing import QueryProcessor
from topicparser import TopicParser
import timeit
import csv


def save_vocabulary(path='../data/vocabulary.txt'):
    index = TfidfIndex()
    index.index()
    with open(path, 'a') as output:
        for key in index.vocabulary.keys():
            output.write('{:s}\n'.format(key))


def print_results(results,
                  topic,
                  team='Data-Wizards',
                  outputfile='../data/task1-results.txt'):
    rank = 1
    with open(outputfile, 'a') as output:
        writer = csv.writer(output, delimiter=' ')
        for file, score in results:
            line = (topic, 'Q0', file, rank, score, team)
            writer.writerow(line)
            rank += 1


if __name__ == '__main__':
    index = TfidfIndex()
    index.index()
    processor = QueryProcessor()
    query = TfidfQuery(index, processor)
    parser = TopicParser()
    for topic in parser.parse():
        print('Building results for topc {:s}.'.format(topic.number))
        start_time = timeit.default_timer()
        results = query.get_results(topic.description)
        print_results(results, topic.number)
        elapsed = timeit.default_timer() - start_time
        print('Elapsed time: {:f}.'.format(elapsed))
