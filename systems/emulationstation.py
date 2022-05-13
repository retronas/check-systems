#!/usr/bin/env python3

import os
from lxml import etree
from lib.url import URLHandler

class EmulationStation():
    def __init__(self):
        self.name = ''
        self.system_key = None
        self.logger = None
        self.systems_url = ''
        self.systems = []
        self.ignored = []

    def read_config(self, data):

        self.data = None
        if data is not None:
            self.data = etree.fromstring(data)

        return self.data

    def get_paths(self, data):

        if data is not None:
            for path in data.xpath("//path"):
                dirname = os.path.split(path.text)[1]
                self.systems.append(dirname)

        return self.systems