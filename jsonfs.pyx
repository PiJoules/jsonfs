from __future__ import print_function

"""
Cython module for managing a file hierarchy as JSON.
"""

import os
import errno


cdef class File(object):
    """Class representing a file in a directory."""

    cdef char* __filename

    def __init__(self, char* filename):
        self.__filename = filename


cdef class Directory(dict):
    """Class representing a file hierarchy as a dictionary."""

    cdef char* __dirname

    def __init__(self, char* dirname):
        """Populate the dictionary from the directory."""
        self.__dirname = dirname

        if not os.path.exists(dirname):
            self.mkdir(dirname)

    cdef void mkdir(self, dirname):
        """Create a directory if not exist."""
        try:
            os.makedirs(dirname)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise RuntimeError(
                    "Coould not create directory '{}': {}".format(dirname, e))

    cpdef void commit(self):
        """Commit changes to filesystem."""
        pass

