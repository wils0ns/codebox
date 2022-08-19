import os
import pytest

from codebox.yaml_tools import load

MODULE_PATH = os.path.abspath(os.path.dirname(__file__))


def test_load():
    data = load(
        os.path.join(MODULE_PATH, "files"),
        recursive=True,
        match_pattern=r".*sample.*",
        ignore_empty=False,
        parse_jinja=True,
        jinja_context={"replace": "expected"},
    )

    assert data["a"] == 1
    assert data["b"] == {"b1": ["expected"], "b2": "b2"}
    assert data["c"] == "expected"
    assert data["d"] == "expected"


def test_load_raises_error():
    with pytest.raises(AttributeError):
        load(os.path.join(MODULE_PATH, "files/empty.yaml"))


def test_load_ignores_empty():
    data = load(
        os.path.join(MODULE_PATH, "files/empty.yaml"),
        ignore_empty=True,
    )

    assert data == {}
