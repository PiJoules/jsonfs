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
import shutil
import mock

from jsonfs import Directory
from random import choice
from string import ascii_uppercase, digits


def rand_str(n=10):
    """Generate a random string."""
    return "".join(choice(ascii_uppercase + digits) for i in xrange(n))


class Custom(object):
    """Class for testing if something that isn't a string to Directory."""

    def __str__(self):
        return "How's my driving?"


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
        self.assertTrue(os.path.isfile(os.path.join(dirname,
                                                    "somefile.txt")))

        # Test filehandler
        handler_mock = mock.MagicMock()
        directory.commit(filehandler=handler_mock)
        handler_mock.assert_called_once_with(os.path.join(dirname,
                                                          "somefile.txt"))

    def test_dir_create(self):
        """Test directory creation."""
        dirname = self.__dirname
        directory = self.__directory

        directory["somedir"] = {"somefile.txt": "someval"}
        directory.commit()
        self.assertTrue(os.path.isdir(os.path.join(dirname, "somedir")))
        self.assertTrue(os.path.isfile(os.path.join(dirname,
                                                    "somedir",
                                                    "somefile.txt")))

        # Test filehandler for dir
        handler_mock = mock.MagicMock()
        directory.commit(filehandler=handler_mock)
        handler_mock.assert_called_once_with(os.path.join(dirname,
                                                          "somedir",
                                                          "somefile.txt"))

    def test_bad_key(self):
        """Test the results of passing a key that isn't a string."""
        dirname = self.__dirname
        directory = self.__directory

        # Int
        handler_mock = mock.MagicMock()
        directory[100] = "somefile"
        directory.commit(filehandler=handler_mock)
        self.assertTrue(os.path.isfile(os.path.join(dirname, "100")))
        handler_mock.assert_called_once_with(os.path.join(dirname, "100"))

        # Tuple (sequential spaces are replace with _)
        directory[(1, 2)] = {"somedir": {"somefile": None}}
        directory.commit()
        filepath = os.path.join(dirname,
                                "(1,-2)",
                                "somedir",
                                "somefile")
        self.assertTrue(os.path.isfile(filepath))

        # Some object
        directory[Custom()] = {"somedir": {"somefile": None}}
        directory.commit()
        filepath = os.path.join(dirname,
                                "How's-my-driving?",
                                "somedir",
                                "somefile")
        self.assertTrue(os.path.isfile(filepath))


if __name__ == "__main__":
    unittest.main()

