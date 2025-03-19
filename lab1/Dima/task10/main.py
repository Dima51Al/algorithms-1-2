def task10(s, array):

    array.sort(key=lambda x: x[0])
    array.sort(key=lambda x: x[1], reverse=True)

    answer = []
    while len(array) != 0:
        for i in range(len(array)):
            if array[i][0] < s:
                s += array[i][1]
                answer.append(array[i][2] + 1)
                array.pop(i)
                break
        else:
            return -1
    return answer


if __name__ == '__main__':

    n, s = list(map(int, input().split()))
    array = []

    for i in range(n):
        a, b = list(map(int, input().split()))
        array.append([a, b - a, i])


    print(task10(s, array))

