#!/usr/bin/env python3

import argparse
from lib.logger import Logger
from lib.tools import Tools
from systems.batocera import Batocera
from systems.retronas import RetroNAS
from systems.mister import MiSTer
from systems.recalbox import Recalbox
from systems.emuelec import EmuELEC
from systems.libretro import libretro


APP_NAME="Check Systems"
APP_VER="0.01"
APP_AUTH="sairuk"
VALID_SYSTEMS=["mister", "batocera", "recalbox","emuelec", "retroarch", "libretro"]

def main(args):
    logger = Logger('main')
    logger.log_info("%s %s" % (APP_NAME, APP_VER))
    projects = [MiSTer(), Batocera(), Recalbox(), EmuELEC(), libretro()]

    if args.system == "mister":
        projects = [projects[0]]

    elif args.system == "batocera":
        projects = [projects[1]]

    elif args.system == "recalbox":
        projects = [projects[2]]

    elif args.system == "emuelec":
        projects = [projects[3]]

    elif args.system == "retroarch" or args.system == "libretro":
        projects = [projects[4]]


    if projects is not None:

        tools = Tools()
        retronas = RetroNAS()
        
        for project in projects:

            if not args.validate_only:
                retronas.read(project.system_key)
                project.read()
                tools.compare(project.systems, retronas.systems, project.name, retronas.name, project.ignored)
                tools.inverse_compare(project.systems, retronas.systems, project.name, retronas.name, project.ignored)
            else:
                retronas.validate(project.system_key)

    else:
        logger.log_error("Could not find module for %s" % args.system)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Compare supported project system data against retronas')
    parser.add_argument('--system', help='get the system data', type=str, required=False, choices=VALID_SYSTEMS)
    parser.add_argument('--validate-only', help='validate the retronas data', default=False, const=True, nargs='?', required=False)
    args = parser.parse_args()
    main(args)