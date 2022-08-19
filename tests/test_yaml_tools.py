import os

from codebox.yaml_tools import load

MODULE_PATH = os.path.abspath(os.path.dirname(__file__))


def test_load_files():
    data = load(
        os.path.join(MODULE_PATH, "files"),
        recursive=True,
        match_pattern=r"sample.*\.yaml",
    )
