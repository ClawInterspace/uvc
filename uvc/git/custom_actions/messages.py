from uvc.models import config


def get_diff_messages_by_commits(commit_from, commit_to, branch=''):
    """

    :param commit_from: the start commit or tag
    :param commit_to: the end commit or tag
    :return: output messages
    """
    cmd = f'git log --after="2020-10-01" --before="2020-11-10" --oneline --merges --first-parent'
