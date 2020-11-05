# -*- encoding: utf-8 -*-
import argparse
import os

from uvc.git.custom_actions.update_branch import update_branch
from uvc.git.utils import get_repo_folders
from uvc.utils.command import fire_commands
from uvc.models import config
from uvc.utils import logging

logger = logging.get_logger()

logger.info('app start!')

arg_parser = argparse.ArgumentParser(description='parse argument')
arg_parser.add_argument('-r', '--root', default=os.getcwd())
arg_parser.add_argument('-c', '--command')
arg_parser.add_argument('-u', '--update')
args = arg_parser.parse_args()

config.git_folders = get_repo_folders(args.root)
console_border_width = config.console_border_width

if args.command:
    config.command = args.command
    _ = list(fire_commands(config.git_folders, config.command))

if args.update:
    branch_name = args.update
    update_branch(branch_name)
