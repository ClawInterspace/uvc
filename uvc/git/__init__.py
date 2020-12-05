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


@git.command()
@click.option('-b', '--branch', help='specified a branch for messages.')
@click.option('-t', '--tag', 'tag_diff', nargs=2, help='Get diff messages by two tags or commit.')
@click.option('-dt', '--datetime', 'datetime_diff', nargs=2, help='Get diff messages by two datetime.')
def diff_msgs(branch, tag_diff, datetime_diff):
    """Get diff messages.

    :return:
    """
    click.echo(branch)
    click.echo(tag_diff)
    click.echo(datetime_diff)
