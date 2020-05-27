# -*- encoding: utf-8 -*-
import sys
import os
import subprocess
from collections import defaultdict

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


def fire_command_and_get_output(folder_list, command):
    """

    :param folder_list:
    :return:
    """
    cwd = os.getcwd()

    for d in folder_list:
        os.chdir(d)

        print('=================================================')
        # print(d)

        result = subprocess.run(command, stdout=subprocess.PIPE)
        # print(result.stdout.decode('utf-8'))
        show_branch_report(d, result.stdout.decode('utf-8'))
        # print(result.returncode)
        print('=================================================\n\n\n')
    os.chdir(cwd)
    for key in branch_report.keys():
        print('On "%s"' % key)
        for d in branch_report.get(key):
            print(d)



branch_report = defaultdict(list)
def show_branch_report(proj_dir, output):
    """

    :return:
    """
    branch_name = output.splitlines()[0].split('On branch ')[1]
    d_list = branch_report[branch_name]
    d_list.append(proj_dir)
    branch_report[branch_name] = d_list



if __name__ == '__main__':
    git_folders = get_all_git_folder(r'D:\workspace\project-expr')
    # for d in git_folders:
    #     print(d)
    command = r'git status'
    fire_command_and_get_output(git_folders, command)

    # traverse all folder under current working directory
    # batch fire command
