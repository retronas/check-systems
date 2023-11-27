#!/usr/bin/env python3

import os, re
from bs4 import BeautifulSoup   
from lib.url import URLHandler
from lib.logger import Logger

class IGDB():
    def __init__(self):
        self.name = 'igdb'
        self.system_key = self.name
        self.logger = Logger(self.name)
        self.systems_url = 'https://www.igdb.com/platforms'
        self.data_file = '_data/https __www.igdb.com_platforms.html'
        self.local_mode = True
        self.systems = []
        self.ignored = []
        self.logger.log_info('Initiated %s module' % self.name)
        self.arcadewhitelist = []
        self.headers = {}

    def read(self):
        
        if self.local_mode:
            if os.path.exists(self.data_file):
                self.content = [open(self.data_file,'r').read()]
            else:
                self.content = None
        else:
            self.uh = URLHandler()
            self.content = self.uh.direct(self.systems_url, self.headers)

        if self.content is not None:
            soup = BeautifulSoup(self.content[0],'lxml')
            self.data = soup.find_all('a', href=True)

            for entry in self.data:
                match = re.match('^\/platforms\/(.+)',entry.text)
                if match is not None:
                    self.systems.append(match.groups()[0])
        return self.systems
    