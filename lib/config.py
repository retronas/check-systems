#!/usr/bin/env python3

import os

class Config():
    def __init__(self):
        self.config_dir = os.path.expanduser('~/.retronas')
        
        self.setup()

    def setup(self):
        if not os.path.exists(self.config_dir):
            os.mkdir(self.config_dir)


    def ignored(self):
        return [
            # recent
            'switch','ps5','switch-2','switch2',
        ]
