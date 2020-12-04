import click

from uvc.git.custom_actions.update_branch import update_branch
from uvc.git.utils import get_repo_folders
from uvc.models import config
from uvc.utils.command import fire_commands


@click.group()
def git():
    pass


@git.command(context_settings=dict(ignore_unknown_options=True,))
@click.argument('gitcmd', nargs=-1, type=click.UNPROCESSED)
def fire(gitcmd):
    """Issue a command to all of repos.
    """
    cmdline = ' '.join(gitcmd)
    _ = list(fire_commands(config.git_folders, f'git {cmdline}'))


@git.command()
@click.argument('branch_name', required=True)
def update(branch_name: str):
    """Update the specified branch if exist.

    :param branch_name:
    :return:
    """
    update_branch(branch_name)
