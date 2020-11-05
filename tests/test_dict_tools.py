import pytest

from codebox.dict_tools import merge, update_nested, get_nested


class TestCodeboxDictTools:
    def test_merge(self):
        samples = [
            [
                {'a': 1, 'b': 2},
                {'a': 1, 'b': 2, 'c': 3},
                {'a': 1, 'b': 2, 'c': 3},
            ],
            [
                {'a': 1, 'b': 2},
                {'a': 1, 'c': 3},
                {'a': 1, 'b': 2, 'c': 3},
            ],
            [
                {'a': 1, 'b': {'b1': 2, 'b2': 3}, 'c': 4},
                {'b': {'b2': 22, 'b3': 33}},
                {'a': 1, 'b': {'b1': 2, 'b2': 22, 'b3': 33}, 'c': 4},
            ],
        ]

        for i in samples:
            assert merge(i[0], i[1]) == i[2]

    def test_get_nested(self):
        assert get_nested({'a': {'b': {'c': 1}}}, 'a:b:c') == 1
        assert get_nested(None, 'a:b:c', 1) == 1
        assert get_nested({'a': 2}, 'b', 1) == 1

    def test_update_nested(self):
        t = {'a': {'b': {'c': 1}}}
        update_nested(t, 'a:b:c', 2)
        assert get_nested(t, 'a:b:c') == 2
