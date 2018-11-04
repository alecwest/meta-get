# meta.api.shell.py

# Copyright (C) 2018 Nathan Martindale <nathanamartindale@gmail.com>
# Licensed under GPL-3.0: https://www.gnu.org/licenses/gpl-3.0.en.html

"""API for accessing basic git functionality."""

import logging
import os

import meta.shell


def clone(url, directory=None, silent=False):
    """Executes the clone command, which clones a repository into a new directory

    :param str url: The url to clone a repository from (https or ssh)
    :param str directory: The location and name of the new directory
    :param bool silent: Whether to suppress the console output of the command or not.
    :returns: A string of everything written to stdout and stderr by the shell.
    """

    if directory is None:
        directory = url.split("/")[-1].replace(".git", "")

    directory = os.path.abspath(directory)

    logging.info("Git API accessed with command clone %s", url)

    output = execute("clone {0} {1}".format(url, directory), silent=silent)
    return output


def execute(command, silent=False):
    """Executes the passed command as a git command in the system shell

    :param str command: The string command to execute.
    :param bool silent: Whether to suppress the console output of the command or not.
    :returns: A string of everything written to stdout and stderr by the shell.
    """

    output = meta.shell.execute("git {0}".format(command), silent=silent)
    return output
