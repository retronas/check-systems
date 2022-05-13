#!/usr/bin/env python3

import os
import yaml
from lib.url import URLHandler
from lib.config import Config
from lib.logger import Logger

class MiSTer():
    def __init__(self):
        self.name = 'mister'
        self.system_key = self.name
        self.logger = Logger(self.name)
        self.systems_repos = [
            ['MiSTer-devel', 'Distribution_MiSTer'],
            ['MiSTer-DB9','Distribution_MiSTer'],
        ]
        self.ignored = ['MEMTEST']
        self.system_dirs = ['games']
        self.systems = []

        self.logger.log_info("Initiated %s module" % self.name)

    def read(self):
        
        self.uh = URLHandler()

        for repo in self.systems_repos:
            self.content = self.uh.github_tree(repo[0], repo[1])

            if self.content is not None:
                for item in self.content['tree']:
                    for dirs in self.system_dirs:
                        if dirs in item['path'] and item['path'].count('/') == 1:
                            filename = item['path'].replace("%s/" % dirs,'')
                            self.systems.append(filename)
                            
        return self.systems
    