from from_workbook import gen_sublist

def test_empty():
    assert gen_sublist([]) == [[]]

def test_default():
    expected = [[], [1], [2], [3],
                [1, 2], [2, 3],
                [1, 2, 3]]

    assert gen_sublist([1, 2, 3]) == expected

def test_4_items():
    expected = [[], [1], [2], [3], [4],
            [1, 2], [2, 3], [3, 4],
            [1, 2, 3], [2, 3 ,4],
            [1, 2, 3, 4]]

    assert gen_sublist([1, 2, 3, 4]) == expected