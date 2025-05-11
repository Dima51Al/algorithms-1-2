def native_search(p: str, t: str) -> (int, list):
    """
    Даны строки p и t. Требуется найти все вхождения строки p в строку t в качестве подстроки.
    :param p:
    :param t:
    :return: n, []
    """
    i = 0
    answer = [0, []]
    if len(p) == 0 or len(p) > len(t):
        return 0, []

    while i < len(t):

        i_p = 0
        i_t = i

        while p[i_p] == t[i_t]:
            i_p += 1
            i_t += 1

            if len(p) == i_p:
                answer[0] += 1
                answer[1].append(i_t-len(p)+1)
                i = i_t - 1

                break

            if len(t) == i_t:
                break
        i += 1


    return answer[0], answer[1]


if __name__ == '__main__':
    print(native_search("aa", "aaaaa"))
