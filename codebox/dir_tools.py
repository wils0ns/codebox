"""Directory utility tools"""
import os
from typing import Iterator


def list_files(path: str, recursive: bool = False) -> Iterator[str]:
    """List of the absolute path of all files within a folder.

    Args:
        path (str): The folder to be scanned for files.
        recursive (bool, optional): Defaults to False. Whether or not to include all subdirectories.

    Yields:
        str: The next file's absolute path within the folder
    """

    if os.path.isdir(path):
        for dirpath, dirnames, filenames in os.walk(path):
            if dirnames and recursive:
                for _dir in dirnames:
                    list_files(os.path.join(dirpath, _dir))
            for _file in filenames:
                yield os.path.abspath(os.path.join(dirpath, _file))
