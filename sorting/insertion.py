# сортировка вставками
def insertion_sort(in_list: list) -> None:
    for i in range(1, len(in_list)):
        item_to_insert = in_list[i]
        j = i - 1
        while j >= 0 and in_list[j] > item_to_insert:
            in_list[j + 1] = in_list[j]
            j -= 1
        in_list[j + 1] = item_to_insert
