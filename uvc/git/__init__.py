import click

from uvc.git.custom_actions.update_branch import update_branch
from uvc.git.utils import get_repo_folders


@click.group()
def git():
    pass


@git.command()
@click.argument('branch_name', required=True)
def update(branch_name: str):
    """Update the specified branch if exist.

    :param branch_name:
    :return:
    """
    update_branch(branch_name)
