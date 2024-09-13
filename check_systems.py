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
from systems.analoguepocket import AnaloguePocket
from systems.emudeck import EmuDeck
from systems.igdb import IGDB
from systems.replayfpgaarcade import ReplayFPGAArcade


APP_NAME="Check Systems"
APP_VER="0.01"
APP_AUTH="sairuk"
VALID_SYSTEMS={
    "mister" : MiSTer(), 
    "batocera" : Batocera(), 
    "recalbox" : Recalbox(),
    "emuelec" : EmuELEC(),
    "retroarch" : libretro(),
    "libretro" : libretro(),
    "analoguepocket" : AnaloguePocket(),
    "emudeck" : EmuDeck(),
    "igdb" : IGDB(),
    "replayfpgaarcade" : ReplayFPGAArcade()
    }

def main(args):
    logger = Logger('main')
    logger.log_info("%s %s" % (APP_NAME, APP_VER))


    # override projects if a system is passed
    if args.system is not None:
        projects = [VALID_SYSTEMS[args.system]]
    else:
        projects = VALID_SYSTEMS.values()

    if projects is not None:
        tools = Tools()
        if args.retronas_branch is not None:
            if args.retronas_local is not None:
                retronas = RetroNAS(args.retronas_branch,args.retronas_local)
            else:
                retronas = RetroNAS(args.retronas_branch)
        else:
            retronas = RetroNAS()
        
        for project in projects:
            if not args.validate_only:
                retronas.read(project.system_key)
                project.read()
                tools.compare(project, retronas)
                tools.compare(retronas, project, inverse=True)
            else:
                retronas.validate(project.system_key)
    else:
        logger.log_error("Could not find module for %s" % args.system)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Compare supported project system data against retronas')
    parser.add_argument('--system', help='get the system data', type=str, required=False, choices=VALID_SYSTEMS.keys())
    parser.add_argument('--validate-only', help='validate the retronas data', default=False, const=True, nargs='?', required=False)
    parser.add_argument('--retronas-branch', help='check against a different branch', type=str, required=False)
    parser.add_argument('--retronas-local', help='check against a local retronas file', type=str, required=False)
    args = parser.parse_args()
    if args.retronas_branch == 'local' and args.retronas_local is None:
        parser.error('--retronas-local RETRONAS_LOCAL is required when --retronas-branch is set to local')
    if args.retronas_local is not None and args.retronas_branch is None :
        parser.error('--retronas-local has no affect without --retronas-branch local ')

    main(args)