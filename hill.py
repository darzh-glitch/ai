import random

d = [
    [0, 0, 15, 0],
    [10, 0, 35, 45],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

p = [0, 1, 2, 3]

def find(path):
    return (d[path[0]][path[1]] + d[path[1]][path[2]]
            + d[path[2]][path[3]] + d[path[3]][path[0]])

random.shuffle(p)
best = p[:]
short = find(p)

for i in range(10000):
    a = random.randint(0, 3)
    b = random.randint(0, 3)
    p[a], p[b] = p[b], p[a]

    now = find(p)
    if now < short:
        best = p[:]
        short = now
    else:
        # undo swap if worse
        p[a], p[b] = p[b], p[a]

print("Best path:", best)
print("Distance:", short)

