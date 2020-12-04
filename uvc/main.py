# -*- encoding: utf-8 -*-
import os

import click

from uvc.models import config
from uvc.utils import logging
from uvc.git import git, get_repo_folders

logger = logging.get_logger()
console_border_width = config.console_border_width


@click.group()
@click.option('-r', '--root', default=os.getcwd(), help='Setup version control root folder for parsing.')
def cli(root):
    click.echo(f'root: {root}')
    config.git_folders = get_repo_folders(root)


cli.add_command(git)

if __name__ == '__main__':
    cli()
