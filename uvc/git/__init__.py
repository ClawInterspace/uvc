import click

from uvc.git.custom_actions.messages import (get_diff_messages_by_commits,
                                             extract_messages, extract_jira_issue_key)
from uvc.git.custom_actions.update import update_branch
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
@click.option('-b', '--branch', default='', help='specified a branch for messages.')
@click.option('-t', '--tag', 'tag_diff', nargs=2, help='Get diff messages by two tags or commit.')
@click.option('-dt', '--datetime', 'datetime_diff', nargs=2, help='Get diff messages by two datetime.')
@click.option('-re', 'pattern', help='Extract regular expression pattern.')
@click.option('-o', '--output', 'format', help='Output message format.')
def diff_msgs(branch, tag_diff, datetime_diff, pattern='', format=''):
    """Get diff messages.

    :return:
    """
    aggregate_messages = ''
    if tag_diff:
        aggregate_messages = get_diff_messages_by_commits(tag_diff[0], tag_diff[1], branch)

    if pattern:
        aggregate_messages = extract_messages(aggregate_messages, pattern)

    if format:
        if format == 'jira':
            msgs = []
            issue_list = extract_jira_issue_key(aggregate_messages)
            for issue_key in issue_list:
                msg = issue_key, f"https://cybersoft4u.atlassian.net/browse/{issue_key}"
                msgs.append(msg)
            aggregate_messages = msgs

    for msg in aggregate_messages:
        print(msg)
