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
        self.ignored = [
                        '1292-advanced-programmable-video-system',

                        # cloud
                        'xboxcloudgaming','antstream','luna','g-cluster','gloud',

                        # subscription
                        'playstation-now',

                        # os
                        'tvos','beos','visionos','watchos','webos',

                        # amazon
                        'amazon-alexa','kindle',

                        # roku
                        'roku',

                        # vr
                        'windows-mixed-reality','steam-vr','pico','oculus-vr',

                        # ios
                        'ipod-classic','ipad',

                        # mobile
                        'mobile-custom',

                        # calc
                        'casio-programmable-calculator',
                        'hp-programmable-calculator',
                        'ti-programmable-calculator',

                        # cpu/chip
                        'mos-technology-6502','motorola-6800','motorola-68k',
                        'intel-8008','intel-8080','intel-8086',
                        'z80','zilog-z8000',

                        # symlinks
                        'beena',            # sega/advanced-pico-beena
                        'panasonic-m2',     # panasonic/3d0
                        'amiga-cd',         # ??
                        'pippin',           # apple/apple-pippin
                        'vc-4000',          # interton/vc4000
                        'vis',              # tandy/tandy-vis
                        'zod',              # tapwave/zodiac

                        # general
                        'atari8bit',
                        'dedicated-console','dedicated-handheld',
                        'microcomputer','analogueelectronics',
                        'photocd','mainframe','terminal','tim',

                        # not enough info
                        'black-point',
                        'daydream',
                        'palmtex',
                        'pandora',
                        'wipi',
                        'freebox',
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
