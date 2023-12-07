#!/usr/bin/env python3

import os
import configparser
import re
from lib.url import URLHandler
from lib.logger import Logger

class ReplayFPGAArcade():
    def __init__(self):
        self.name = 'replayfpgaarcade'
        self.system_key = self.name
        self.logger = Logger(self.name)
        self.systems_repos = [
            ['FPGAArcade', 'replay_release', 'master']
        ]
        self.ignored = [] #old need to change comparison code to use exclude/include
        self.exclude = ['README.md','firmware']
        self.include = ['.*\.ini']
        self.system_dirs = []
        self.systems = []

        self.logger.log_info("Initiated %s module" % self.name)

    def read(self):
        
        self.uh = URLHandler()

        for repo in self.systems_repos:
            self.content = self.uh.github_tree(repo[0], repo[1], repo[2])
            if self.content is not None:
                configfiles = []
                for item in self.content['tree']:
                    for include in self.include:
                        if re.match(f'^{include}.*',item['path']):
                            configfiles.append(f"{item['path']}")

            for configfile in configfiles:
                configdata = self.uh.github_raw(repo[0], repo[1], repo[2], configfile)
                config = configparser.ConfigParser(strict=False,allow_no_value=True)
                config.read_string(configdata[0].decode())

                if config.has_section('UPLOAD'):
                    for option in config['UPLOAD']:
                        if re.match('^(rom|ROM).*', option):
                            dirname = os.path.dirname(configfile)
                            abspath = os.path.join(dirname,os.path.dirname(config['UPLOAD'][option]).split(',')[0])
                            if abspath not in self.systems:
                                self.systems.append(abspath)

                if config.has_section('FILES'):
                    for option in config['FILES']:
                        if re.match('.+_cfg', option):
                            dirname = os.path.dirname(configfile)
                            abspath = os.path.join(dirname,config['FILES'][option].split(',')[0].replace('"',''))
                            if abspath not in self.systems:
                                self.systems.append(abspath)
                           
        return self.systems
    