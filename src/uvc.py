# -*- encoding: utf-8 -*-
import argparse
import os

from custom_actions.update_branch import update_branch
from git.cmd_firer import get_all_git_folders
from utils.command_helper import fire_commands
from models import config
from utils import logging_helper

logger = logging_helper.get_logger()

logger.info('app start!')

arg_parser = argparse.ArgumentParser(description='parse argument')
arg_parser.add_argument('-r', '--root', default=os.getcwd())
arg_parser.add_argument('-c', '--command')
arg_parser.add_argument('-u', '--update')
args = arg_parser.parse_args()

config.git_folders = get_all_git_folders(args.root)
console_border_width = config.console_border_width

if args.command:
    config.command = args.command
    _ = list(fire_commands(config.git_folders, config.command))

if args.update:
    branch_name = args.update
    update_branch(branch_name)
