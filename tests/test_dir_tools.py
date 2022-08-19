from codebox.dir_tools import list_files


def test_list_files(tmp_path):
    f1 = tmp_path / "file1.txt"
    f1.touch()
    f2 = tmp_path / "sub/file2.txt"
    f2.parent.mkdir()
    f2.touch()

    assert not list(list_files(f1))
    assert len(list(list_files(tmp_path))) == 1
    assert len(list(list_files(tmp_path, recursive=True))) == 2
