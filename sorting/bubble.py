# сортировка пузырьком

def bubble_sort(in_list):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(in_list) - 1):
            if in_list[i] > in_list[i + 1]:
                in_list[i], in_list[i + 1] = in_list[i + 1], in_list[i]
                swapped = True