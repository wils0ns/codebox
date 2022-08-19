from codebox.dict_tools import merge, update_nested, get_nested


def test_merge():
    samples = [
        [
            {"a": 1, "b": 2},
            {"a": 1, "b": 2, "c": 3},
            {"a": 1, "b": 2, "c": 3},
        ],
        [
            {"a": 1, "b": 2},
            {"a": 1, "c": 3},
            {"a": 1, "b": 2, "c": 3},
        ],
        [
            {"a": 1, "b": {"b1": 2, "b2": 3}, "c": 4},
            {"b": {"b2": 22, "b3": 33}},
            {"a": 1, "b": {"b1": 2, "b2": 22, "b3": 33}, "c": 4},
        ],
        [
            {"a": 1, "b": [1, 2, 3]},
            {"a": 2, "b": [4, 5, 6]},
            {"a": 2, "b": [4, 5, 6]},
        ],
    ]

    for i in samples:
        assert merge(i[0], i[1]) == i[2]


def test_get_nested():
    assert get_nested({"a": {"b": {"c": 1}}}, "a:b:c") == 1
    assert get_nested(None, "a:b:c", 1) == 1
    assert get_nested({"a": 2}, "b", 1) == 1
    assert get_nested({"a": 2}, "b:c", 1) == 1


def test_update_nested():
    t = {"a": {"b": {"c": 1}}}
    update_nested(t, "a:b:c", 2)
    update_nested(t, "d:e", 3)
    assert get_nested(t, "a:b:c") == 2
    assert get_nested(t, "d:e") == 3
