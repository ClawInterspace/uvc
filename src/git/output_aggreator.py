# coding: utf-8
from collections import defaultdict

from utils.logging_helper import get_logger

logger = get_logger()


class Aggreator(object):

    def __init__(self):
        self.output_map = defaultdict(list)

    def create_branch_report(self, proj_dir, output):
        """

        :return:
        """
        branch_name = output.splitlines()[0].split('On branch ')[1]
        d_list = self.output_map[branch_name]
        d_list.append(proj_dir)
        self.output_map[branch_name] = d_list

    def show(self):
        for key in self.output_map.keys():
            logger.debug('On "%s"' % key)
            for d in self.output_map.get(key):
                logger.debug(d)
