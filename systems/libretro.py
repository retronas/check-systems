#!/usr/bin/env python3

import os
from lib.url import URLHandler
from lib.logger import Logger

class libretro():
    def __init__(self):
        self.name = 'retroarch'
        self.system_key = self.name
        self.logger = Logger(self.name)
        self.systems_repos = [
            ['libretro', 'libretro-database', "master"],
        ]
        self.ignored = []
        self.system_dirs = ['rdb']
        self.systems = []

        self.logger.log_info("Initiated %s module" % self.name)

    def read(self):
        
        self.uh = URLHandler()

        for repo in self.systems_repos:
            self.content = self.uh.github_tree(repo[0], repo[1], repo[2])

            if self.content is not None:
                for item in self.content['tree']:
                    for dirs in self.system_dirs:
                        if dirs in item['path'] and item['path'].count('/') == 1:
                            filename = item['path'].replace("%s/" % dirs,'')
                            filename = os.path.splitext(filename)[0]
                            self.systems.append(filename)
                            
        return self.systems
    