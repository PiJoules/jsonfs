#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Unit tests for jsonfs.

This most likely isn't the correct way to make a unit test for a cython
package, but it'll have to do for now until I learn how.
"""

from __future__ import print_function

import unittest
import os
import contextlib
import shutil
import tempfile

from jsonfs import Directory
from random import choice
from string import ascii_uppercase, digits


def rand_str(n=10):
    """Generate a random string."""
    return "".join(choice(ascii_uppercase + digits) for i in xrange(n))


@contextlib.contextmanager
def tempdir():
    """Create a temprary directory that will be removed on close."""
    dirpath = tempfile.mkdtemp()
    try:
        yield dirpath
    finally:
        shutil.rmtree(dirpath)


class TestJSONFS(unittest.TestCase):
    """Bagels."""

    def __create_dirname(self):
        """Create a random string for a directory name."""
        dirname = rand_str()
        while os.path.isdir(dirname):
            dirname = rand_str()
        return dirname

    def setUp(self):
        """Create the Directory on setup."""
        self.__dirname = self.__create_dirname()
        self.__directory = Directory(self.__dirname)

    def tearDown(self):
        """Destroy the Directory on deletion."""
        shutil.rmtree(self.__dirname)

    def test_create(self):
        """Test creating the Directory."""
        dirname = self.__dirname

        # Test creation
        self.assertTrue(os.path.isdir(dirname))

        # No error should be thrown on creating
        try:
            Directory(dirname)
        except Exception as e:
            self.fail(
                "Exception raised when recreating the Directory: {}"
                .format(e))

    def test_file_create(self):
        """Test file creation."""
        dirname = self.__dirname
        directory = self.__directory

        directory["somefile.txt"] = None
        directory.commit()
        self.assertTrue(os.path.isfile(os.path.join(dirname, "somefile.txt")))


if __name__ == "__main__":
    unittest.main()

