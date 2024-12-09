#!/usr/bin/env python3

import os
from lib.url import URLHandler
from lib.logger import Logger
from systems.emulationstation import EmulationStation


class RetroDECK(EmulationStation):
    def __init__(self):
        self.name = 'retrodeck'
        self.short = 'RDK'
        self.system_key = self.name
        self.logger = Logger(self.name)
        self.systems = []
        self.targets = [ 'android', 'linux', 'macos', 'unix', 'windows' ]
        self.ignored = [
            # garbage systems
            'emulators','cloud','desktop','epic','lutris','steam','kodi',
            'consolearcade','pcarcade',
            # symlinks
            'ags','amiga600',
            'cps','genesis','mame-advmame','type-x','mame-mame4all',
            'megacdjp','megadrivejp','neogeocdjp','saturnjp','sega32xjp','sega32xna','segacd',
            'sneshd','snesna','tg-cd'
            ]
        self.logger.log_info("Initiated %s module" % self.name)

    def build_systems(self):
        systems = []
        self.uh = URLHandler()
        for target in self.targets:
            systems_url = f'https://raw.githubusercontent.com/RetroDECK/ES-DE/refs/heads/main/resources/systems/{target}/es_systems.xml'
            self.content = self.uh.direct(systems_url)
            self.data = self.read_config(self.content[0])
            for item in self.get_paths(self.data):
                systems.append(item)
        self.systems = set(systems)


    def read(self):
        self.build_systems()
        return self.systems