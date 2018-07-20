import os
import yaml
from re import match

from codebox import dir_tools
from codebox import dict_tools

def load(path, recursive=False, match_pattern=None):
    """Loads and parses a file or a folder containing yaml files.
    All existing dictorinaries will be deeply merged.

    Args:
        path (str): File or directory path.
        recursive (bool, optional): Defaults to False. Whether or not to include subdirectoties.
        match_pattern (str, optional): A regular expression to be used to filter the files to be load
            based on the file's full name.

    Returns:
        dict
    """

    files = []
    if os.path.isdir(path):
        files = dir_tools.list_files(path, recursive)
    else:
        files = [path]

    data = dict()
    for _file in files:
        if match_pattern and not match(match_pattern, _file):
            continue
        with open(_file) as f:
            data = dict_tools.merge(data, yaml.load(f.read()))

    return data

if __name__ == '__main__':
    print(load('examples/yml/', match_pattern='.*sls$'))
    print(load('examples/yml/'))
