#!/usr/bin/env python3

import os
import yaml
from lib.url import URLHandler
from lib.config import Config
from lib.logger import Logger

class RetroNAS():
    def __init__(self):
        self.name = 'retronas'
        self.system_key = 'src'
        self.logger = Logger(self.name)
        self.systems_url = 'https://raw.githubusercontent.com/danmons/retronas/main/ansible/retronas_systems.yml'
        self.systems = []
        self.ignored = ['system_map', 'system_links']
        self.logger.log_info("Initiated %s module" % self.name)

    def read(self, system_key):
        
        self.uh = URLHandler()
        self.content = self.uh.direct(self.systems_url)

        if self.content is not None:
            self.data = yaml.safe_load(self.content[0])

            for key in self.data.keys():
                if key not in self.ignored:
                    for system in self.data[key]:
                        if system[system_key]:
                            self.systems.append(system[system_key])

        return self.systems
    