#!/usr/bin/env python3

import yaml
import json
import re
import time
from lib.url import URLHandler
from lib.logger import Logger

class Loader(yaml.SafeLoader):
    pass

def construct_GetAnalogueCore(loader, suffix, node):
    return dict(loader.construct_mapping(node))

Loader.add_multi_constructor('!ruby/object:Analogue::Core', construct_GetAnalogueCore)

class AnaloguePocket():
    def __init__(self):
        self.name = 'analoguepocket'
        self.short = 'AGP'
        self.system_key = self.name
        self.logger = Logger(self.name)
        self.systems_repos = [
            ['openfpga-cores-inventory','analogue-pocket']
            ]
        self.systems = []
        self.ignored = [
                        'alphamission',
                        'astdelux',
                        'asteroids',
                        'athena',
                        'bakraid',
                        'bankpanic',
                        'batrider',
                        'coinopkey',
                        'combatribes',
                        'congo',
                        'defender',
                        'digdug',
                        'dkong3',
                        'dkongjr',
                        'dominos',
                        'donkeykong',
                        'doubledragoniii',
                        'druaga',
                        'exerion',
                        'galaga',
                        'gaplus',
                        'garegga',
                        'gauntlet',
                        'gauntlet',
                        'gberet',
                        'irem_m92',
                        'irem_m92',
                        'jailbreak',
                        'joust2',
                        'jt1942',
                        'jt1943',
                        'jtaliens',
                        'jtbiocom',
                        'jtbtiger',
                        'jtbubl',
                        'jtcastle',
                        'jtcircus',
                        'jtcommnd',
                        'jtcomsc',
                        'jtcontra',
                        'jtcop',
                        'jtcps1',
                        'jtcps15',
                        'jtcps2',
                        'jtdd',
                        'jtdd2',
                        'jtexed',
                        'jtflane',
                        'jtfround',
                        'jtgng',
                        'jtgunsmk',
                        'jtkarnov',
                        'jtkchamp',
                        'jtkicker',
                        'jtkiwi',
                        'jtkunio',
                        'jtlabrun',
                        'jtmidres',
                        'jtmikie',
                        'jtmx5k',
                        'jtninja',
                        'jtoutrun',
                        'jtpang',
                        'jtparoda',
                        'jtpatreon',
                        'jtpinpon',
                        'jtrastan',
                        'jtriders',
                        'jtroadf',
                        'jtroc',
                        'jtrumble',
                        'jts16',
                        'jts16b',
                        'jts18',
                        'jtsarms',
                        'jtsbaskt',
                        'jtsectnz',
                        'jtsf',
                        'jtshanon',
                        'jtshouse',
                        'jtsimson',
                        'jtslyspy',
                        'jttmnt',
                        'jttoki',
                        'jttora',
                        'jttrack',
                        'jttrojan',
                        'jtvigil',
                        'jtwc',
                        'jtwwfss',
                        'jtxmen',
                        'jtyiear',
                        'kingdmgp',
                        'lunarlander',
                        'mario',
                        'mortalkombat',
                        'narc',
                        'performan',
                        'pipibibs',
                        'pooyan',
                        'qbert',
                        'radarscope',
                        'robotron',
                        'slapfight',
                        'smashtv',
                        'snowbros2',
                        'spaceinvaders',
                        'spacerace',
                        'sstriker',
                        'superbreakout',
                        'system1',
                        'system1',
                        'taitosj',
                        'tecmo',
                        'tekipaki',
                        'totalcarnage',
                        'truxton2',
                        'wrestlefest',
                        'xevious',
                    ]
        self.system_dirs = ['_data/cores']
        self.arcadewhitelist = ['pong']
        self.key = "platform_ids"

        self.logger.log_info('Initiated %s module' % self.name)

    def read(self):
        
        self.uh = URLHandler()

        for repo in self.systems_repos:
            self.content = self.uh.github_tree(repo[0],repo[1])

            if self.content is not None:
                for item in self.content['tree']:
                    for dirs in self.system_dirs:
                        if dirs in item['path'] and item['path'].count('/') == 1:
                            filename = item['path'].replace("%s/" % dirs,'')
                            content = self.uh.direct(item['url'])
                            decoded = json.loads(content[0].decode())

                            for config in decoded['tree']:
                                filename = config['path']
                                self.yaml = self.uh.direct(f"https://raw.githubusercontent.com/{repo[0]}/{repo[1]}/refs/heads/main/_data/cores/{filename}")

                                if self.yaml is not None:
                                    self.data = yaml.load(self.yaml[0], Loader=Loader)
                                    for platform in self.data["metadata"][self.key]:
                                        if platform not in self.ignored:
                                            self.systems.append(platform)
        return self.systems
    