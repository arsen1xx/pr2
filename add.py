import random

DAYS = ["Пн", "Вт", "Ср", "Чт", "Пт"]
FREE = "Вільне вікно"
SUBJECTS = ["Математика", "Фізика", "Програмування", "Історія", FREE]

random.seed(1)
schedule = [[[random.choice(SUBJECTS) for _ in range(4)] for _ in range(5)] for _ in range(3)]

group = 0

for g in range(3):
    print(f"Група {g + 1}:")
    for d in range(5):
        print(f"  {DAYS[d]}: {schedule[g][d]}")


def lessons(day):
    return sum(p != FREE for p in day)


loads = [lessons(day) for day in schedule[group]]
best = [DAYS[d] for d in range(5) if loads[d] == max(loads)]
print(f"\nНайбільше навантаження у групи {group + 1}: {best} ({max(loads)} пар)")


def has_window(day):
    idx = [i for i, p in enumerate(day) if p != FREE]
    return bool(idx) and idx[-1] - idx[0] + 1 > len(idx)


windows = [DAYS[d] for d in range(5) if has_window(schedule[group][d])]
print(f"Дні з вікнами у групи {group + 1}: {windows}")

print("\nПотоки:")
found = False
for d in range(5):
    for p in range(4):
        subjects = [schedule[g][d][p] for g in range(3)]
        for s in set(subjects):
            if s != FREE and subjects.count(s) > 1:
                groups = [g + 1 for g in range(3) if subjects[g] == s]
                print(f"  {DAYS[d]}, пара {p + 1}: {s}, групи {groups}")
                found = True
if not found:
    print("  потоків немає")