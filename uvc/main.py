# -*- encoding: utf-8 -*-
import os

import click

from uvc.git import git, get_repo_folders
from uvc.models import config
from uvc.utils import logging
from uvc.utils.command import fire_commands

logger = logging.get_logger()


@click.group()
@click.option('-r', '--root', default=os.getcwd(), help='Setup version control root folder for parsing.')
@click.option('--no-trace-command', is_flag=True, help=r"Set if you don't need stdout output.")
def cli(root, no_trace_command):
    config.git_folders = get_repo_folders(root)
    config.trace_command = not no_trace_command


@git.command(context_settings=dict(ignore_unknown_options=True,))
@click.argument('cmds', nargs=-1, type=click.UNPROCESSED)
def fire(cmds):
    """Issue a command to all of repos.
    """
    cmdline = ' '.join(cmds)
    _ = list(fire_commands(config.git_folders, f'{cmdline}'))


cli.add_command(git)
cli.add_command(fire)

if __name__ == '__main__':
    cli()
