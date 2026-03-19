import numpy as np

G = np.array([
[1,0,0,0,0,1,1,1],
[0,1,0,0,1,0,1,1],
[0,0,1,0,1,1,0,1],
[0,0,0,1,1,1,1,0]
], dtype=int) % 2

weights = []
for i in range(16):
    u = np.array([int(b) for b in format(i, '04b')])
    c = (u @ G) % 2
    wt = np.sum(c)
    weights.append(wt)

unique_weights = set(weights)
min_d = min(w for w in weights if w > 0)
print(f'Unique weights: {unique_weights}')
print(f'Min distance: {min_d}')
