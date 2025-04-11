import sys


def finding(array_of_dots, array_of_variants, i, j, is_rec):
    sys.setrecursionlimit(40000 * 2)

    if i >= len(array_of_variants) or i < 0:
        return 0
    if j >= len(array_of_variants[0]) or j < 0:
        return 0

    if array_of_variants[i][j] == 0:
        array_of_variants[i][j] = 1

        if array_of_dots[i][j] == 1:
            finding(array_of_dots, array_of_variants, i + 1, j, 1)
            finding(array_of_dots, array_of_variants, i, j + 1, 1)
            finding(array_of_dots, array_of_variants, i - 1, j, 1)
            finding(array_of_dots, array_of_variants, i, j - 1, 1)
            if is_rec == 0:
                return 1
    return 0


def main(array_of_dots, N, M):
    array_of_variants = [[0 for _ in range(M)] for _ in range(N)]
    c = 0
    for i in range(N):
        for j in range(M):
            c += finding(array_of_dots, array_of_variants, i, j, 0)
    return c


if __name__ == '__main__':
    with open('INPUT.TXT', 'r') as input_file:
        lines = input_file.readlines()
        N, M = map(int, lines[0].strip().split())
        array_of_dots = []
        for line in lines[1:N + 1]:
            row = []
            for char in line.strip():
                if char == '#':
                    row.append(1)
                else:
                    row.append(0)
            array_of_dots.append(row)

    result = main(array_of_dots, N, M)

    with open('OUTPUT.TXT', 'w') as output_file:
        output_file.write(str(result))
