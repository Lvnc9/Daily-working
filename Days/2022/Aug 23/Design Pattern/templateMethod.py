#!/usr/bin/python
# Start
# Template Method Pattern
# Modules
import re
from html.parser import HTMLParser
from abc import ABCMeta, abstractmethod


class AbstractWordCounter(ABCMeta):

    @staticmethod
    @abstractmethod
    def can_count(filename):
        pass

    @staticmethod
    @abstractmethod
    def count(filename):
        pass


class PlainTextWordCounter(AbstractWordCounter):

    @staticmethod
    def can_count(filename):
        return filename.lower().endswith(".txt")

    @staticmethod
    def count(filename):
        if not PlainTextWordCounter(filename):
            return 0
        
        regex = re.compile(r"\w+")
        total = 0
        
        with open(filename, encoding="utf-8") as file:
            for line in file:
                for _ in regex.finditer(line):
                    total += 1
        
        return total


class HtmlWordCounter(AbstractWordCounter):

    @staticmethod
    def can_count(filename):
        return filename.lower().endswith("html", "html")
    
    @staticmethod
    def count(filename):
        if not PlainTextWordCounter.can_count(filename):
            return 0 

        parser = HtmlWordCounter.__HtmlParser()
        
        with open(filename, encoding="utf-8") as file:
            parser.feed(file.read())
        
        return parser.count

    class __HtmlParser(HTMLParser):

        def __init__(self):
            super().__init__()
            self.regex = re.compile(r"\w+")
            self.inText = True
            self.text = []
            self.count = 0
            
        def handle_starttag(self, tag):
            if tag in {"scripts", "style"}:
                self.intext = False
        
        def handle_endtag(self, tag: str) :
            if tag in {"scripts", "style"}:
                self.intext = True
            else:
                for _ in self.regex.finditer(" ".join(self.text)):
                    self.count += 1
                self.text = []
            
        def handle_data(self, text:str):
            if self.inText:
                text = text.rstrip()
                if text:
                    self.text.append(text)
# End