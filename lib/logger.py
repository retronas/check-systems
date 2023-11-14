#!/usr/bin/env python3

import os
from lib.config import Config

class Logger():
    def __init__(self, logger):
        self.level = 'INFO'
        self.logger = logger
        self.config = Config()
        self.log_file = os.path.join(self.config.config_dir,'retronas_systems_scan.log')

    def show(self):
        print(self.entry)

    def write(self):
        with open(self.log_file, 'a') as f:
            f.write(self.entry)

    def log_entry(self, s):
        self.entry = "[{:>15}] {:>4} {:30}".format(self.logger, self.level, s)

    def log_plain(self, s):
        self.level = ""
        self.log_entry(s)
        self.write()
        self.show()

    def log_debug(self, s):
        self.level = "DEBUG"
        self.log_entry(s)
        self.write()
        self.show()

    def log_error(self, s):
        self.level = "ERROR"
        self.log_entry(s)
        self.write()
        self.show()

    def log_info(self, s):
        self.level = "INFO"
        self.log_entry(s)
        self.write()
        self.show()