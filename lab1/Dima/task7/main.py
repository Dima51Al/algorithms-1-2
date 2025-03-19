def main(K, n, array):
    array.sort()

    sum_ = 0
    count = 0
    id = 0
    while sum_ < K:
        sum_ += array[id]
        id += 1

        if sum_ < K:
            count += 1

    return count


if __name__ == '__main__':

    K, n = input().split()
    K, n = int(K), int(n)

    array = list(map(int, input().split()))



    print(main(K, n, array))

