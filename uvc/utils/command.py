import os
import subprocess

from uvc.models import config
from uvc.utils.logging import get_logger

logger = get_logger()


def fire_commands(dest_wds: list, command: object) -> tuple:
    """

    :param dest_wds: destination working dictionary
    :param command: the target command
    :return: the corresponding working folder's output
    """
    trace_cmd = config.trace_command
    src_dir = os.getcwd()
    for working_dir in dest_wds:
        try:
            target_dir, output = _issue_command_in_directory(command, src_dir, working_dir)
            if trace_cmd:
                display(target_dir, command, output)
            yield target_dir, output
        except Exception as e:
            if trace_cmd:
                print(e)
            continue


def fire_commands_respectively(wd_and_cmd_maps: dict) -> tuple:
    """

    :param wd_and_cmd_maps: a dictionary for command and target dir maps
    :return:
    """
    trace_cmd = config.trace_command
    src_dir = os.getcwd()
    for working_dir, issue_cmd in wd_and_cmd_maps.items():
        target_dir, output = _issue_command_in_directory(issue_cmd, src_dir, working_dir)
        if trace_cmd:
            display(target_dir, issue_cmd, output)
        yield target_dir, output


def _issue_command_in_directory(issue_cmd, origin_dir, target_dir) -> tuple:
    """

    :param issue_cmd: the command you want to issue
    :param origin_dir: the path you want to return, usually as cwd
    :param target_dir: the working dir you used
    :return:
    """
    trace_cmd = config.trace_command
    try:
        os.chdir(target_dir)
        result = subprocess.run(issue_cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=config.is_shell)
        output = result.stdout.decode('utf-8')
        return target_dir, output
    except Exception as e:
        if trace_cmd:
            print(Exception(f': Fire "{issue_cmd}" failed'))
            raise
    finally:
        os.chdir(origin_dir)


def display(wd, cmd, output):
    console_border_width = config.console_border_width
    print(f" {'':_<{console_border_width}} ")
    print(f'|{wd:<{console_border_width}}|')
    out_msg = f'=> {cmd}'
    print(f'|{out_msg:<{console_border_width}}|')
    print(f"|{'':_<{console_border_width}}|")
    print(output)