import itertools

# Variables and domains
variables = ['A', 'B', 'C']
colors = ['Red', 'Green', 'Blue']

# Constraints: adjacency pairs
adjacent = [('A','B'), ('B','C'), ('A','C')]

# Try all possible assignments
for assignment in itertools.product(colors, repeat=3):
    mapping = dict(zip(variables, assignment))
    if all(mapping[x] != mapping[y] for x,y in adjacent):
        print(mapping)
