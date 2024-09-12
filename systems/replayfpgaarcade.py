#!/usr/bin/env python3

import os
import configparser
import re
from lib.url import URLHandler
from lib.logger import Logger

class ReplayFPGAArcade():
    def __init__(self):
        self.name = 'replayfpgaarcade'
        self.short = 'RFA'
        self.system_key = self.name
        self.logger = Logger(self.name)
        self.systems_repos = [
            ['FPGAArcade', 'replay_release', 'master']
        ]
        self.exclude = [
                'README.md',
                'firmware',
                'amiga/amiga_68060',
                'amiga/amiga_68060/removable',
                'amiga/amiga_68060/fixed',
                'amiga/amiga_aga',
                'amiga/amiga_aga/removable',
                'amiga/amiga_aga/fixed',
                'amiga/amiga_fx68k',
                'amiga/amiga_fx68k/removable',
                'amiga/amiga_fx68k/fixed',
                'c64/removable',
                'cbm64/carts',
                'cbm64/removable',
                'ccastles/roms',
                'mrdo/roms',
                'vic20/removable',
                ]
        self.ignored = self.exclude #old need to change comparison code to use exclude/include
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
                            procpath = os.path.dirname(config['UPLOAD'][option]).split(',')[0]
                            if procpath:
                                abspath = os.path.join(dirname,os.path.join(procpath))
                            else:
                                abspath = dirname
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
    