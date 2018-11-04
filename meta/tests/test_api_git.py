# meta.tests.test_api_git.py

# Copyright (C) 2018 Nathan Martindale <nathanamartindale@gmail.com>
# Licensed under GPL-3.0: https://www.gnu.org/licenses/gpl-3.0.en.html

"""Test set to ensure the git API is working as intended."""

# pylint:disable=redefined-outer-name
# pylint:disable=unused-argument

import os
import pytest

import meta.api.git


# --------------------------------------
#   Fixtures
# --------------------------------------


@pytest.fixture
def shell_mock(mocker):
    """Mock for the backend shell execution function."""
    execution_mock = mocker.patch("meta.shell.execute", autospec=True)
    execution_mock.return_value = "executed"
    return execution_mock


# --------------------------------------
#   Tests
# --------------------------------------


def test_default_command_execution(shell_mock):
    """Ensure that a command gets passed correctly to the underlying shell function."""
    meta.api.git.execute("push")
    shell_mock.assert_called_with("git push", silent=False)


def test_silent_command_execution(shell_mock):
    """Ensure that the api, if called silently, calls the backend shell silently."""
    meta.api.git.execute("push", silent=True)
    shell_mock.assert_called_with("git push", silent=True)


def test_command_execution_return(shell_mock):
    """Ensure that the shell output gets returned correctly."""
    assert meta.api.git.execute("push") == "executed"


def test_clone(shell_mock):
    """Ensure that the clone command gets passed correctly to the underlying shell function."""
    meta.api.git.clone("https://github.com/fsufitch/git-gud.git", silent=False)
    shell_mock.assert_called_with(
        "git clone https://github.com/fsufitch/git-gud.git {0}".format(
            os.path.abspath("git-gud")
        ),
        silent=False,
    )


def test_silent_clone(shell_mock):
    """Ensure that the clone command, if called silently gets passed correctly
    to the underlying shell function."""
    meta.api.git.clone("https://github.com/fsufitch/git-gud.git", silent=True)
    shell_mock.assert_called_with(
        "git clone https://github.com/fsufitch/git-gud.git {0}".format(
            os.path.abspath("git-gud")
        ),
        silent=True,
    )


def test_clone_different_directory(shell_mock):
    """Ensure that the clone command, if called with a different directory gets
    passedd correctly to the underlying shell function"""
    meta.api.git.clone(
        "git@github.com:fsufitch/git-gud.git", directory="hello-world", silent=False
    )
    shell_mock.assert_called_with(
        "git clone git@github.com:fsufitch/git-gud.git {0}".format(
            os.path.abspath("hello-world")
        ),
        silent=False,
    )
