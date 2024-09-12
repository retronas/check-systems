#!/usr/bin/env python3

import yaml
import re
from lib.url import URLHandler
from lib.logger import Logger

class AnaloguePocket():
    def __init__(self):
        self.name = 'analoguepocket'
        self.short = 'AGP'
        self.system_key = self.name
        self.logger = Logger(self.name)
        self.systems_url = 'https://raw.githubusercontent.com/openfpga-cores-inventory/analogue-pocket/main/_data/cores.yml'
        self.systems = []
        self.ignored = []
        self.logger.log_info('Initiated %s module' % self.name)
        self.arcadewhitelist = ['pong']

    def read(self):
        
        self.uh = URLHandler()
        self.content = self.uh.direct(self.systems_url)

        if self.content is not None:
            self.data = yaml.safe_load(self.content[0])

            for entry in self.data:
                for core in entry['cores']:
                    if re.match('^Arcade.*', core['platform']['category']) is None or core['platform_id'] in self.arcadewhitelist:
                        self.systems.append(core['platform_id'])
        return self.systems
    