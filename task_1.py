class FlatIterator:

    def __init__(self, list_of_list):
        self.data = list_of_list
        self.index_list = 0
        self.nested_list_index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.nested_list_index += 1

        if self.nested_list_index + 1 > len(self.data[self.index_list]):
            self.nested_list_index = 0
            self.index_list += 1

        if self.index_list + 1 > len(self.data):
            raise StopIteration

        return self.data[self.index_list][self.nested_list_index]


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
