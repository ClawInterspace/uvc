import re

from uvc.models import config
from uvc.utils.command import fire_commands


def get_diff_messages_by_commits(commit_after='', commit_before='', branch=''):
    """

    :param commit_after: the start commit or tag
    :param commit_before: the end commit or tag
    :return: output messages
    """
    cmd = f'git log {branch} {commit_after}..{commit_before} ' \
          f'--oneline --merges --first-parent --pretty="format:%s"'

    # check branch exist
    # check tag exist

    aggregate_messages = []
    for wd, out in fire_commands(config.git_folders, cmd):
        aggregate_messages.append(out)
    return aggregate_messages


def get_diff_messages_by_time(time_after='', time_before='', branch=''):
    """
    TODO: not done yet.
    :param time_after: example: 2020-11-26 15:40:22, 2020-11-26 all ok
    :param time_before: example: 2020-11-26 15:40:22, 2020-11-26 all ok
    :param branch:
    :return:
    """

    cmd = f'git log origin develop --after="2020-11-26 15:40:22" --before="2020-11-30 11:24:50" ' \
          f'--oneline --merges --first-parent --pretty="format:%s, %an, %ct"'


def extract_messages(messages: list, pattern: str) -> list:
    msgs = []
    for msg in messages:
        matched_list = re.findall(pattern, msg)
        msgs.append(matched_list)
    return msgs


def extract_jira_issue_key(messages: list) -> list:
    issue_keys = set()
    for msg in messages:
        issue_key_set = set(msg)
        issue_keys = issue_keys.union(issue_key_set)

    return list(issue_keys)
