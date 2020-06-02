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
arg_parser.add_argument('-g', '--git')
args = arg_parser.parse_args()

git_folders = get_all_git_folders(args.root)
# for d in git_folders:
#     print(d)
if args.command:
    command = args.command
elif args.git:
    command = f'git {args.git}'

console_border_width = 80

for wd, out in fire_commands(git_folders, command):
    print(f" {'':_<{console_border_width}} ")
    print(f'|{wd:^{console_border_width}}|')
    out_msg = f'=> {command}'
    print(f'|{out_msg:^{console_border_width}}|')
    print(f"|{'':_<{console_border_width}}|")
    print(out)
