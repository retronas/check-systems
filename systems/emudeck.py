#!/usr/bin/env python3

import os, json
from lib.url import URLHandler
from lib.logger import Logger

class EmuDeck():
    def __init__(self):
        self.name = 'emudeck'
        self.short = 'EMD'
        self.system_key = self.name
        self.logger = Logger(self.name)
        self.systems_repos = [
            ['dragoonDorise','EmuDeck']
            ]
        self.ignored = [
            # garbage systems
            'systeminfo.txt','systems.txt','cloud','desktop','epic','lutris','moonlight',
            'primehacks','remoteplay','steam','kodi','emulators','generic-applications','android/roms'
            # symlinks
            'ags','amiga600','atarijaguarcd','cps','gc','genesis','mame-advmame',
            'mame-mame4all','mastersystem','megacdjp','megadrivejp','n3ds','neogeocdjp',
            'psx','saturnjp','sega32xjp','sega32xna','segacd','sneshd','snesna',
            ]
        self.system_dirs = ['roms']
        self.systems = []

        self.logger.log_info("Initiated %s module" % self.name)

    def read(self):
        
        self.uh = URLHandler()

        for repo in self.systems_repos:
            self.content = self.uh.github_tree(repo[0],repo[1])

            if self.content is not None:
                for item in self.content['tree']:
                    for dirs in self.system_dirs:
                        if dirs in item['path'] and item['path'].count('/') == 1:
                            filename = item['path'].replace("%s/" % dirs,'')
                            self.systems.append(filename)
                            
        return self.systems
    