#!/usr/bin/env python3

import os
import argparse
from lib.logger import Logger
from lib.tools import Tools
from systems.batocera import Batocera
from systems.retronas import RetroNAS
from systems.mister import MiSTer
from systems.recalbox import Recalbox


APP_NAME="Check Systems"
APP_VER="0.01"
APP_AUTH="sairuk"
VALID_SYSTEMS=["mister", "batocera", "recalbox"]

def main(args):
    logger = Logger('main')
    logger.log_info("%s %s" % (APP_NAME, APP_VER))
    project=None  

    if args.system == "mister":
        project = MiSTer()

    elif args.system == "batocera":
        project = Batocera()

    elif args.system == "recalbox":
        project = Recalbox()

    if project is not None:

        tools = Tools()

        retronas = RetroNAS()
        retronas_data = retronas.read(project.system_key)

        project_data = project.read()

        tools.compare(project_data, retronas_data, project.name, retronas.name, project.ignored)
        tools.inverse_compare(project_data, retronas_data, project.name, retronas.name, project.ignored)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Compare supported project system data against retronas')
    parser.add_argument('--system', help='get the Batocera system data', type=str, required=True, choices=VALID_SYSTEMS)
    args = parser.parse_args()
    main(args)