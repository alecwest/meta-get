# meta.api.shell.py

# Copyright (C) 2018 Nathan Martindale <nathanamartindale@gmail.com>
# Licensed under GPL-3.0: https://www.gnu.org/licenses/gpl-3.0.en.html

"""API for accessing basic git functionality."""

import logging

import meta.shell


def execute(command, silent=False):
    """Executes the passed command as a git command in the system shell

    :param str command: The string command to execute.
    :param bool silent: Whether to suppress the console output of the command or not.
    :returns: A string of everything written to stdout and stderr by the shell.
    """

    output = meta.shell.execute("git {0}".format(command), silent=silent)
    return output
