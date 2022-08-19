import os

from codebox.file_tools import replace_in_files


MODULE_DIR = os.path.dirname(os.path.abspath(__file__))

FILES = {os.path.join(MODULE_DIR, "src", "ex01.txt"): os.path.join(MODULE_DIR, "dest", "ex01.txt")}

replace_in_files(FILES, {r"0.0.0": "1.1.1", "{{version}}": "2.2.2"})
