#!/usr/bin/env python3

import re
from lib.url import URLHandler
from lib.logger import Logger

# ref
# https://docs.romm.app/4.5.0/Platforms-and-Players/Supported-Platforms/

class RoMM():
    def __init__(self):
        self.name = 'romm'
        self.short = 'RMM'
        self.system_key = self.name
        self.logger = Logger(self.name)
        self.systems_url = 'https://raw.githubusercontent.com/rommapp/romm/master/backend/handler/metadata/base_handler.py'
        self.systems = []
        self.ignored = ['switch','ps5','switch-2',
                        '1292-advanced-programmable-video-system',
                        'atari8bit','hd-dvd-player',
                        'dedicated-console','dedicated-handheld',
                        'microcomputer','analogueelectronics',
                        'mos-technology-6502','motorola-6800','motorola-68k',
                        'xboxcloudgaming','amazon-alexa','antstream',
                        'luna','g-cluster','terminal','triton','gloud',
                        'tizen','tvos','beos','brew','bada','bit-90',
                        'black-point','bubble','amiga-cd','pippin',
                        'casio-programmable-calculator','clickstart',
                        'hp-programmable-calculator',
                        'beena','daydream','freebox','gimini','gnex',
                        'windows-mixed-reality','steam-vr','pico','oculus-vr',
                        'mainframe','hugo','hrx','ideal-computer',
                        'intel-8008','intel-8080','intel-8086',
                        'ipod-classic','ipad','kindle','mobile-custom'
                       ]
        self.logger.log_info("Initiated %s module" % self.name)

    def read(self):

        self.uh = URLHandler()
        self.content = self.uh.direct(self.systems_url)

        start_match = False
        if self.content is not None:
            self.content = self.content[0].split(b"\n")
            pattern = re.compile('^\s+(.*)\s=\s"(.*)"$')
            for line in self.content:
                line = line.rstrip().decode()
                if re.match("^class\sUniversalPlatformSlug.*",line):
                    start_match = True
                if start_match:
                    m = re.match(pattern,line)
                    if m is not None and len(m.groups()) >= 2:
                        self.systems.append(m.group(2))

        return self.systems
