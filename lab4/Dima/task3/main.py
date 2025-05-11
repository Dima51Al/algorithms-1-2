import time


def hash(string):
    s = 0
    for i in range(len(string)):
        s += ord(string[i]) * 31 ** (len(string) - i - 1)
    return s % (2**32 - 1)


def hash_next(string_before, string_new, hash_start, len_pattern):
    hash_start -= ord(string_before) * 31 ** (len_pattern - 1)
    hash_start *= 31
    hash_start += ord(string_new)
    return hash_start % (2**32 - 1)


def rabin_karp_search(p: str, t: str) -> (int, list):
    """
    Алгоритм Рабина-Карпа для поиска всех вхождений строки p в строку t.
    :param p: Паттерн для поиска
    :param t: Текст для поиска
    :return: Кол-во вхождений и список индексов вхождений
    """
    len_p = len(p)
    len_t = len(t)
    answer = [0, []]

    if len_p == 0 or len_p > len_t:
        return 0, []

    hash_p = hash(p)
    hash_t = hash(t[:len_p])


    if hash_p == hash_t and t[:len_p] == p:
        answer[0] += 1
        answer[1].append(1)


    for i in range(1, len_t - len_p + 1):
        hash_t = hash_next(t[i - 1], t[i + len_p - 1], hash_t, len_p)
        if hash_p == hash_t and t[i:i + len_p] == p:
            answer[0] += 1
            answer[1].append(i+1)

    return answer[0], answer[1]


if __name__ == '__main__':
    start = time.time()
    pattern = "aba"*10
    text = "abax"*10**6

    rabin_karp_search(pattern, text)
    print(time.time() - start)
