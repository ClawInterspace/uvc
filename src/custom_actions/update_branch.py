from datetime import datetime

from git.cmd_firer import fire_commands, fire_commands_respectively
from models import config
from models.dir_status import GitDirStatus


def update_branch(branch):
    git_status_snapshot1 = build_folder_status()

    has_target_branch_dirs = [wd for wd, status in git_status_snapshot1.map.items()
                              if branch in status.local_branches]

    has_changes_dirs = [wd for wd, status in git_status_snapshot1.map.items()
                        if status.has_changed]

    need_stashed_dirs = list(set(has_target_branch_dirs) & set(has_changes_dirs))

    dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    identify_msg = f'uvc stash at {dt}'
    _ = list(fire_commands(need_stashed_dirs, f'git stash push --all -m "{identify_msg}"'))
    _ = list(fire_commands(has_target_branch_dirs, f'git checkout {branch}'))
    _ = list(fire_commands(has_target_branch_dirs, f'git fetch --all --prune'))
    _ = list(fire_commands(has_target_branch_dirs, f'git fetch --tags -f'))
    _ = list(fire_commands(has_target_branch_dirs, f'git pull'))

    cmd_maps = {wd: f'git checkout {git_status_snapshot1.map.get(wd).current_branch}'
                for wd in has_target_branch_dirs}
    _ = list(fire_commands_respectively(cmd_maps))


def build_folder_status() -> GitDirStatus:
    dir_status = GitDirStatus(config.git_folders)

    for wd, out in fire_commands(config.git_folders, 'git status'):
        wd_status = dir_status.map.get(wd)
        lines = str(out).splitlines()
        wd_status.current_branch = lines[0].replace("On branch ", "")

    for wd, out in fire_commands(config.git_folders, 'git status --porcelain'):
        wd_status = dir_status.map.get(wd)
        lines = str(out).splitlines()
        if lines:
            wd_status.has_changed = True

    for wd, out in fire_commands(config.git_folders, 'git branch -l'):
        wd_status = dir_status.map.get(wd)
        lines = str(out).splitlines()
        for line in lines:
            if '*' in line:
                bn = line.split(' ')[1]
            else:
                bn = line.strip()
            wd_status.local_branches.append(bn)

    return dir_status
