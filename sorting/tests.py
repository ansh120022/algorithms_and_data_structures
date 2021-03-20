import pytest
from algorithms_and_data_structures.sorting.selection import selection_sort
from algorithms_and_data_structures.sorting.insertion import insertion_sort
from algorithms_and_data_structures.sorting.bubble import bubble_sort

initial_list_1 = [4, 9, 1, 10, 15, 8]
expected_list_1 = [1, 4, 8, 9, 10, 15]

initial_list_2 = ['a', 'r', 'n']
expected_list_2 = ['a', 'n', 'r']


class TestSort:
    @pytest.mark.parametrize("initial, expected",
                             ([initial_list_1, expected_list_1],
                              [initial_list_2, expected_list_2]))
    def test_selection_sort(self, initial, expected):
        selection_sort(initial)
        assert initial == expected, "Сортировка выбором отработала некорректно"

    @pytest.mark.parametrize("initial, expected",
                             ([initial_list_1, expected_list_1],
                              [initial_list_2, expected_list_2]))
    def test_insertion_sort(self, initial, expected):
        insertion_sort(initial)
        assert initial == expected, "Сортировка вставками отработала некорректно"

    @pytest.mark.parametrize("initial, expected",
                             ([initial_list_1, expected_list_1],
                              [initial_list_2, expected_list_2]))
    def test_bubble_sort(self, initial, expected):
        bubble_sort(initial)
        assert initial == expected, "Сортировка пузырьком отработала некорректно"

