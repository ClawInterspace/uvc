# -*- encoding: utf-8 -*-
import argparse
import os

from custom_actions.update_branch import update_branch
from git.cmd_firer import get_all_git_folders, fire_commands
from models import config
from utils import logging_helper

logger = logging_helper.get_logger()

logger.info('app start!')

arg_parser = argparse.ArgumentParser(description='parse argument')
arg_parser.add_argument('-r', '--root', default=os.getcwd())
arg_parser.add_argument('-c', '--command')
arg_parser.add_argument('-g', '--git')
arg_parser.add_argument('-u', '--update')
args = arg_parser.parse_args()

config.git_folders = get_all_git_folders(args.root)
# for d in git_folders:
#     print(d)
if args.command:
    config.command = args.command
elif args.git:
    config.command = f'git {args.git}'

console_border_width = config.console_border_width

update_branch('develop')

# for _ in fire_commands(config.git_folders, config.command): pass
# deque(fire_commands(config.git_folders, config.command), maxlen=0)
_ = list(fire_commands(config.git_folders, config.command))
