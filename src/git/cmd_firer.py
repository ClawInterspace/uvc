# -*- encoding: utf-8 -*-
import os
# from asyncio import subprocess
import copy

from utils.logging_helper import get_logger

logger = get_logger()


def get_all_git_folders(proj_root):
    """
    """
    git_folders = []
    dir_paths = [copy.copy(proj_root)]
    for dir_path in dir_paths:
        if os.path.exists(os.path.join(dir_path, '.git')):
            git_folders.append(os.path.abspath(dir_path))
            continue

        # BFS
        for file_or_dir_name in os.listdir(dir_path):
            full_path = os.path.join(dir_path, file_or_dir_name)
            if os.path.isdir(full_path):
                dir_paths.append(os.path.join(dir_path, file_or_dir_name))

    # remove duplicated object
    return list(set(git_folders))
