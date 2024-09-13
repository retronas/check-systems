#!/usr/bin/env python3

from lib.logger import Logger

class Tools():
    def __init__(self):
        self.logger = Logger('tools')
        return

    def diff(self, left, right, ignore=[]):
        pieces = []
        pieces.append("Checking for %s systems not in %s" % (left.name, right.name))
        found = False

        for entry in left.systems:
            if entry not in right.systems and entry not in left.ignored:
                pieces.append(" %s[%s] %s" % (" "*17, right.short.upper(), entry))
                found = True
        self.logger.log_info('\n'.join(pieces))

        if not found:
            self.logger.log_info("No missing %s systems found" % left.name)

    def compare(self, left, right, inverse=True):
        ignore = left.ignored
        if inverse:
            ignore = right.ignored
        if len(left.systems) and len(right.systems):
            self.logger.log_info('Running left (%s) > right (%s) compare' % (left.name, right.name))
            self.diff(left, right, ignore)
        else:
            self.logger.log_error("Data sets were incomplete, comparison is not possible")