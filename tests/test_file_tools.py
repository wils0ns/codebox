from codebox.file_tools import replace_in_files


def test_replace_in_files(tmp_path):
    f1 = tmp_path / "file1.txt"
    f1.write_text("#old-in-f1# is #replaced#")

    f2 = tmp_path / "file2.txt"
    f2.write_text("#original#")

    f3 = tmp_path / "file3.txt"

    files = {f1: None, f2: f3}

    replace_in_files(files, {r"\#.*\#": "expected"})

    assert f1.read_text() == "expected"
    assert f2.read_text() == "#original#"
    assert f3.read_text() == "expected"
