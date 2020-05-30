# -*- encoding: utf-8 -*-
import os
# from asyncio import subprocess
import subprocess

from utils.logging_helper import get_logger

logger = get_logger()


def fire_commands(dest_wds: list, command):
    """

    :param dest_wds: destination working dictionary
    :param command: the target command
    :return: the corresponding working folder's output
    """
    cwd = os.getcwd()

    logger.debug(f'Fire command: {command}')
    try:
        for wd in dest_wds:
            os.chdir(wd)
            result = subprocess.run(command, stdout=subprocess.PIPE)
            yield wd, result.stdout.decode('utf-8')
    except Exception as e:
        raise Exception(f': Fire "{command}" failed')
    finally:
        os.chdir(cwd)


def get_all_git_folders(proj_root):
    """
    """
    git_folders = []

    for dir_path, dir_names, file_names in os.walk(proj_root):
        if os.path.exists(os.path.join(dir_path, '.git')):
            git_folders.append(os.path.abspath(dir_path))

    return git_folders
