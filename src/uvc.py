# -*- encoding: utf-8 -*-
import argparse
import os

from git.cmd_firer import get_all_git_folders, fire_commands
from utils import logging_helper

logger = logging_helper.get_logger()

logger.info('app start!')

arg_parser = argparse.ArgumentParser(description='parse argument')
arg_parser.add_argument('-r', '--root', default=os.getcwd())
arg_parser.add_argument('-c', '--command')
args = arg_parser.parse_args()

git_folders = get_all_git_folders(args.root)
# for d in git_folders:
#     print(d)
command = args.command

width = 80

print(f'Command: "{command}"')
for wd, out in fire_commands(git_folders, command):
    print(f" {'':_<{width}} ")
    print(f'|{wd:^{width}}|')
    print(f"|{'':_<{width}}|")
    print(out)
