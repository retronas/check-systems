#!/usr/bin/env python3

import yaml
from lib.url import URLHandler
from lib.logger import Logger

# dependency on other data
from systems.libretro import libretro


class Pretty():
    def __init__(self):
        self.name = 'pretty'
        self.short = 'PRT'
        self.system_key = "pretty_name"
        self.logger = Logger(self.name)
        self.systems_url = ''
        self.systems = []
        self.ignored = []
        self.logger.log_info("Initiated %s module" % self.name)

    def read(self):

        self.systems = []

        self.dep = libretro().read()

        for entry in self.dep:
            self.systems.append(entry.replace("- ",""))

        print(self.systems[1])

        return self.systems
    