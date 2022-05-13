#!/usr/bin/env python3

import yaml
from lib.url import URLHandler
from lib.config import Config
from lib.logger import Logger

class Batocera():
    def __init__(self):
        self.name = 'batocera'
        self.system_key = self.name
        self.logger = Logger(self.name)
        self.systems_url = 'https://raw.githubusercontent.com/batocera-linux/batocera.linux/master/package/batocera/emulationstation/batocera-es-system/es_systems.yml'
        self.systems = []
        self.ignored = []
        self.logger.log_info("Initiated %s module" % self.name)

    def read(self):
        
        self.uh = URLHandler()
        self.content = self.uh.direct(self.systems_url)

        if self.content is not None:
            self.data = yaml.safe_load(self.content[0])

            for key in self.data.keys():
                self.systems.append(key)

        return self.systems
    