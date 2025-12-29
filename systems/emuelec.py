#!/usr/bin/env python3

import os
import json
from lib.url import URLHandler
from lib.logger import Logger
from systems.emulationstation import EmulationStation


class EmuELEC(EmulationStation):
    def __init__(self):
        self.name = 'emuelec'
        self.short = 'EME'
        self.system_key = self.name
        self.logger = Logger(self.name)
        self.systems_url = 'https://raw.githubusercontent.com/EmuELEC/EmuELEC/master/packages/sx05re/emuelec-emulationstation/config/es_systems.json'
        self.systems = []
        self.ignored = ['setup','nesh','gbah','gbch','gbh','snesh','gamegearh','genh']
        self.logger.log_info("Initiated %s module" % self.name)

    def read_json_config(self, data=None):
        return json.loads(data)

    def read(self):
        self.uh = URLHandler()
        self.content = self.uh.direct(self.systems_url)
        self.data = self.read_json_config(data=self.content[0])
        for entry in self.data["systems"]:
            if entry['name'] not in self.ignored:
                self.systems.append(entry["name"])

        return self.systems
