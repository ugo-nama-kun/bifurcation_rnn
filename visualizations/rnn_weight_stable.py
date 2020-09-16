import random
import math

import matplotlib.pyplot as plt

fig = plt.figure(figsize=(20, 20))

width = 500
height = 500

alpha = 0.5
w1 = -600.0
w2 = 10.0
b = 10.0

x = []
y = []
for i in range(width):
    # Tick of the parameter
    w = w1 + (w2 - w1) * float(i) / width

    # Random Initialization
    h = 2 * random.random() - 1
    for j in range(1000):
        # RNN-map
        h = alpha * h + (1 - alpha) * (1 / (1 + math.exp(-(w * h + b))))  # Chaotic behavior
        if j > 100:
            x.append(w)
            y.append(h)

plt.scatter(x, y, s=1)
plt.xlabel("weight")
plt.ylabel("hidden activation")
plt.grid(True)
plt.show()