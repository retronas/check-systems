#!/usr/bin/env python3

import re
from lib.url import URLHandler
from lib.logger import Logger

class RoMM():
    def __init__(self):
        self.name = 'romm'
        self.short = 'RMM'
        self.system_key = self.name
        self.logger = Logger(self.name)
        self.systems_url = 'https://raw.githubusercontent.com/rommapp/romm/master/backend/handler/metadata/base_handler.py'
        self.systems = []
        self.ignored = ['switch']
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
