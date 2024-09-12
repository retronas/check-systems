#!/usr/bin/env python3

from lib.url import URLHandler
from lib.logger import Logger

class Recalbox():
    def __init__(self):
        self.name = 'recalbox'
        self.short = 'RCB'
        self.system_key = self.name
        self.logger = Logger(self.name)
        self.systems_projectid = '2396494'
        self.systems_path = 'package/recalbox-romfs2/systems'
        self.ignored = ['.templates']
        self.system_dirs = []
        self.systems = []

        self.logger.log_info("Initiated %s module" % self.name)

    def read(self):
        
        self.uh = URLHandler()
        self.content = self.uh.gitlab_tree(self.systems_projectid, self.systems_path)

        if self.content is not None:
            for setname in self.content:
                for entry in setname:
                    if entry['name'] not in self.ignored:
                        self.systems.append(entry['name'])

        return self.systems
    