#!/usr/bin/env python3

from lib.logger import Logger

class Tools():
    def __init__(self):
        self.logger = Logger('tools')
        return

    def diff(self, left, right, left_name="", right_name="", ignore=[]):


        pieces = []
        pieces.append("Checking for %s systems not in %s" % (left_name, right_name))
        found = False

        for entry in left:
            if entry not in right and entry not in ignore:
                pieces.append(" %s[%s] %s" % (" "*17, right_name.upper(), entry))
                found = True
        self.logger.log_info('\n'.join(pieces))

        if not found:
            self.logger.log_info("No missing %s systems found" % left_name)

    def compare(self, left, right, left_name="", right_name="", ignore=[]):
        if len(left) and len(right):
            self.logger.log_info('Running left (%s) > right (%s) compare' % (left_name, right_name))
            self.diff(left, right, left_name, right_name, ignore)
        else:
            self.logger.log_error("Data sets were incomplete, comparison is not possible")

    def inverse_compare(self, left, right, left_name="", right_name="", ignore=[]):
        if len(left) and len(right):
            self.logger.log_info('Running right (%s) > left (%s) compare' % (right_name, left_name))
            self.diff(right, left, right_name, left_name, ignore)
        else:
            self.logger.log_error("Data sets were incomplete, inverse comparison is not possible")