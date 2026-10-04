import random


def generate(m, n, low, high):
    return [[random.randint(low, high) for _ in range(n)] for _ in range(m)]


def show(a):
    if not a or not a[0]:
        print("(матриця порожня)\n")
        return
    print(" " * 9 + "".join(f"{'стовпець ' + str(j + 1):>12}" for j in range(len(a[0]))))
    for i, row in enumerate(a):
        print(f"{'рядок ' + str(i + 1):<9}" + "".join(f"{round(x, 2):>12}" for x in row))
    print()


def subtract_mean(a):
    return [[x - sum(row) / len(row) for x in row] for row in a]


def shift(a, k):
    m, n = len(a), len(a[0])
    a = [row[-(k % n):] + row[:-(k % n)] for row in a]
    return a[k % m:] + a[:k % m]


def remove_max(a):
    mx = max(max(row) for row in a)
    rows = {i for i, row in enumerate(a) if mx in row}
    cols = {j for row in a for j, x in enumerate(row) if x == mx}
    return [[x for j, x in enumerate(row) if j not in cols]
            for i, row in enumerate(a) if i not in rows]


def rotate(a):
    n = len(a)
    for i in range(n):
        for j in range(i + 1, n):
            a[i][j], a[j][i] = a[j][i], a[i][j]
    for row in a:
        row.reverse()


m, n, k = 4, 5, 2
matrix = generate(m, n, 1, 10)
print("Початкова матриця:")
show(matrix)

print("1. Мінус середнє арифметичне рядка:")
show(subtract_mean(matrix))

print(f"2. Зсув на {k} вправо і на {k} догори:")
show(shift(matrix, k))

print("3. Без рядків і стовпців з максимумом:")
show(remove_max(matrix))

square = generate(4, 4, 1, 10)
print("4. Квадратна матриця до повороту:")
show(square)
rotate(square)
print("Після повороту на 90° за годинниковою стрілкою:")
show(square)