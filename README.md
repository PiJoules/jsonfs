# jsonfs
Convert a filesystem to a dictionary you can edit in python.

Currently, this is just meant to be a quick and easy way to create nested
directories easily in python.


## Usage
```py
from jsonfs import Directory

# Creates a directory in the current dir.
# This oject can be treated as a dictionary.
directory = Directory("somedir")

# Create a file
directory["somefile.txt"] = None

# Create a directory
directory["anotherdir"] = {"anotherfile.csv": None}

# Commit the changes to impliment the changes above.
directory.commit()  # Now the files and dir are created under "somedir/"

# You can commit with a callback function to call every time a file
# is found in the tree when iterating over files.
def callback(fullpath):
    print fullpath
directory.commit(filehandler=callback)  # prints "somefile.txt" and "anotherfile.csv"
```


## TODO
- Add a way for deleting files.


## Suggestions/Bug/I messed something up horribly
Feel free to submit an issue.

