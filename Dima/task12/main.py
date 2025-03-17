import copy


def task12(array: list[int]):
    """Мы допускаем,что можно разбить [-3, 1, 2] на [-3, 1, 2] и []"""

    array = copy.copy(array)

    array.sort()
    sum_array = sum(array)

    if sum_array % 2 == 1:
        return -1, -1

    sum_array //= 2

    s = 0
    id = 0
    while s < sum_array and id < len(array):
        s += array[id]
        id += 1
    if s == sum_array:
        return id-1, s
    else:
        return -1, -1



if __name__ == '__main__':
    n = input()
    n = int(n)
    array = list(map(int, input().split()))
    answer = task12(array)
    print(answer[0])
    print(answer[1])