# -*- encoding: utf-8 -*-
import sys
import os
import subprocess

# sort last update date
# sync specific branch with auto stash changee


def get_all_git_folder(proj_root):
    """
    """
    git_folders = []

    for dir_path, dir_names, file_names in os.walk(proj_root):
        if os.path.exists(os.path.join(dir_path, '.git')):
            git_folders.append(os.path.abspath(dir_path))

    return git_folders


def fire_command_and_get_output(folder_list):
    """

    :param folder_list:
    :return:
    """
    cwd = os.getcwd()

    for d in folder_list:
        os.chdir(d)

        print('=================================================')
        print(d)
        command = r'git status'
        result = subprocess.run(command, stdout=subprocess.PIPE)
        print(result.stdout.decode('utf-8'))
        print('=================================================\n\n\n')

    os.chdir(cwd)


if __name__ == '__main__':
    git_folders = get_all_git_folder(r'D:\workspace\project-tis')
    # for d in git_folders:
    #     print(d)
    fire_command_and_get_output(git_folders)

    # traverse all folder under current working directory
    # batch fire command
