def quicksort(items):
    if len(items) <= 1:
        return items
    pivot = items[len(items) // 2]
    pivot_value = pivot[0] / pivot[1]  # удельная стоимость опорного

    l = [item for item in items if item[0] / item[1] > pivot_value] # стоят больше
    m = [item for item in items if item[0] / item[1] == pivot_value] # только же
    r = [item for item in items if item[0] / item[1] < pivot_value] # меньше

    return quicksort(l) + m + quicksort(r)


n, W = map(int, input().split())
items = [tuple(map(int, input().split())) for i in range(n)]


def find_best(n, W, items):
    items = quicksort(items)  # кастомная сортировка по удельной стоимости 
    main_price = 0.0  # вся цена предметов у вора

    for price, weight in items:
        if W == 0:  # случай когда сумка заполнена
            break

        take_new = min(W, weight) # минимум из остатка места и веса нового предмета
        main_price += take_new * (price / weight) # если взяли не весь предмет
        W -= take_new

    return main_price

maximum = find_best(n, W, items)
print(f"{maximum:.4f}")
