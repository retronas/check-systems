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
        self.systems_url = 'https://raw.githubusercontent.com/RetroDECK/ES-DE/refs/heads/main/resources/systems/unix/es_systems.xml'
        self.systems = []
        self.ignored = [
            # garbage systems
            'emulators','cloud','desktop','epic','lutris','steam','kodi',
            'consolearcade','pcarcade',
            # symlinks
            'ags','amiga600',
            'cps','genesis','mame-advmame','type-x','mame-mame4all','pc',
            'megacdjp','megadrivejp','neogeocdjp','saturnjp','sega32xjp','sega32xna','segacd',
            'sneshd','snesna','tg-cd'
            ]
        self.logger.log_info("Initiated %s module" % self.name)

    def read(self):
        self.uh = URLHandler()
        self.content = self.uh.direct(self.systems_url)
        self.data = self.read_config(self.content[0])
        self.systems = self.get_paths(self.data)

        return self.systems