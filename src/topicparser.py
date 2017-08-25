#!/usr/bin/env python3
import xml.etree.ElementTree as ElementTree


class Topic:
    def __init__(self):
        self._number = None
        self._type = None
        self._description = None
        self._summary = None
        self._diagnosis = None

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        self._number = value

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def summary(self):
        return self._summary

    @summary.setter
    def summary(self, value):
        self._summary = value

    @property
    def diagnosis(self):
        return self._diagnosis

    @diagnosis.setter
    def diagnosis(self, value):
        self._diagnosis = value


class TopicParser:
    def parse(self, file='../data/topics.xml'):
        root = ElementTree.parse(file).getroot()
        for topic_element in root.findall('topic'):
            topic = Topic()
            topic.description = self.get_child_element_text(topic_element, 'description')
            topic.diagnosis = self.get_child_element_text(topic_element, 'diagnosis')
            topic.number = topic_element.get('number')
            topic.summary = self.get_child_element_text(topic_element, 'summary')
            topic.type = topic_element.get('type')
            yield topic

    def get_child_element_text(self, element, childname):
        child = element.find(childname)
        if child is not None:
            return child.text
        return None
