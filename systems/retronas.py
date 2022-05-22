#!/usr/bin/env python3

import os
import yaml
from lib.url import URLHandler
from lib.logger import Logger

class RetroNAS():
    def __init__(self):
        self.name = 'retronas'
        self.system_key = 'src'
        self.logger = Logger(self.name)
        self.systems_url = 'https://raw.githubusercontent.com/danmons/retronas/main/ansible/retronas_systems.yml'
        self.systems = []
        self.ignored = [
            'system_map', 
            'system_links',
            "system_template", 
            ]
        self.logger.log_info("Initiated %s module" % self.name)

    def read(self, system_key):
        
        self.systems = []
        self.uh = URLHandler()
        self.content = self.uh.direct(self.systems_url)

        if self.content is not None:
            self.data = yaml.safe_load(self.content[0])

            for key in self.data.keys():
                if key not in self.ignored:
                    for system in self.data[key]:
                        if not system_key in system:
                            self.logger.log_error("System key: %s does not exist in retronas_systems.yml, exiting" % system_key)
                            exit(1)
                        if system[system_key]:
                            self.systems.append(system[system_key])
    
    def validate(self, system_key):
        self.read(system_key)

        print("\n\nRETRONAS SYSTEMS output, data is good, no data is :'(")
        print("-" * 130)
        print("{:<30} | {:<40} | {:30}".format("%s_system" % self.name, "romdir", "key:%s" % system_key))
        print("-" * 130)

        for entry in self.data:
            if entry not in self.ignored:
                for system in self.data[entry]:
                    if system_key in system:
                        print("{:<30} | {:<40} | {:30}".format(entry, system['src'], system[system_key]))
