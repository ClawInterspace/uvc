import os
import subprocess

from uvc.models import config
from uvc.utils.logging import get_logger
logger = get_logger()


def fire_commands(dest_wds: list, command: object, show_output: bool = True) -> tuple:
    """

    :param dest_wds: destination working dictionary
    :param command: the target command
    :param show_output: set False to cancel display
    :return: the corresponding working folder's output
    """
    src_dir = os.getcwd()
    for working_dir in dest_wds:
        target_dir, output = _issue_command_in_directory(command, src_dir, working_dir)
        if show_output:
            display(target_dir, command, output)
        yield target_dir, output


def fire_commands_respectively(wd_and_cmd_maps: dict, show_output: bool = True) -> tuple:
    """

    :param show_output: flag for show output or not
    :param wd_and_cmd_maps: a dictionary for command and target dir maps
    :return:
    """
    src_dir = os.getcwd()
    for working_dir, issue_cmd in wd_and_cmd_maps.items():
        target_dir, output = _issue_command_in_directory(issue_cmd, src_dir, working_dir)
        if show_output:
            display(target_dir, issue_cmd, output)
        yield target_dir, output


def _issue_command_in_directory(issue_cmd, origin_dir, target_dir):

    try:
        os.chdir(target_dir)
        result = subprocess.run(issue_cmd, stdout=subprocess.PIPE, shell=config.is_shell)
        output = result.stdout.decode('utf-8')
        return target_dir, output
    except Exception as e:
        raise Exception(f': Fire "{issue_cmd}" failed')
    finally:
        os.chdir(origin_dir)


def display(wd, cmd, output):
    console_border_width = config.console_border_width
    print(f" {'':_<{console_border_width}} ")
    print(f'|{wd:^{console_border_width}}|')
    out_msg = f'=> {cmd}'
    print(f'|{out_msg:^{console_border_width}}|')
    print(f"|{'':_<{console_border_width}}|")
    print(output)