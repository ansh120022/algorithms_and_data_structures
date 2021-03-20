# сортировка выбором
def selection_sort(in_list: list) -> None:
    # i последовательно перебирает элементы списка
    for i in range(len(in_list)):
        # хранит значение минимального найденного элемента
        min_index = i
        # сравниваем найденный минимальный элемент с остальными в поисках меньшего
        for j in range(i + 1, len(in_list)):
            if in_list[j] < in_list[min_index]:
                # нашли элемент с ещё меньшим значением
                min_index = j
        # переставляем меньший элемент с большим
        in_list[i], in_list[min_index] = in_list[min_index], in_list[i]
