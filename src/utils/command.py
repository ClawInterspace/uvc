import os
import subprocess

from models import config
from utils.logging import get_logger
logger = get_logger()


def fire_commands(dest_wds: list, command: object, show_output: bool = True) -> tuple:
    """

    :param dest_wds: destination working dictionary
    :param command: the target command
    :param show_output: set False to cancel display
    :return: the corresponding working folder's output
    """
    cwd = os.getcwd()

    logger.debug(f'Fire command: {command}')

    for wd in dest_wds:
        try:
            os.chdir(wd)
            result = subprocess.run(command, stdout=subprocess.PIPE)
            output = result.stdout.decode('utf-8')
            if show_output:
                display(wd, command, output)
            yield wd, output
        except Exception as e:
            raise Exception(f': Fire "{command}" failed')
        finally:
            os.chdir(cwd)


def fire_commands_respectively(wd_and_cmd_maps: dict, show_output: bool = True) -> tuple:
    """

    :param wd_and_cmd_maps:
    :return:
    """
    cwd = os.getcwd()

    for wd, cmd in wd_and_cmd_maps.items():
        try:
            os.chdir(wd)
            result = subprocess.run(cmd, stdout=subprocess.PIPE)
            output = result.stdout.decode('utf-8')
            if show_output:
                display(wd, cmd, output)
            yield wd, output
        except Exception as e:
            raise Exception(f': Fire "{cmd}" failed')
        finally:
            os.chdir(cwd)


def display(wd, cmd, output):
    console_border_width = config.console_border_width
    print(f" {'':_<{console_border_width}} ")
    print(f'|{wd:^{console_border_width}}|')
    out_msg = f'=> {cmd}'
    print(f'|{out_msg:^{console_border_width}}|')
    print(f"|{'':_<{console_border_width}}|")
    print(output)