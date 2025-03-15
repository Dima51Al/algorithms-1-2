def quicksort(items):
    if len(items) <= 1:
        return items
    pivot = items[len(items) // 2]
    pivot_value = pivot[0] / pivot[1]  # удельная стоимость опорного

    l = [item for item in items if item[0] / item[1] > pivot_value] # стоят больше
    m = [item for item in items if item[0] / item[1] == pivot_value] # только же
    r = [item for item in items if item[0] / item[1] < pivot_value] # меньше

    return quicksort(l) + m + quicksort(r)
