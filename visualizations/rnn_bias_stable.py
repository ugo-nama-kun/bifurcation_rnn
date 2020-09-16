import random
import math

import matplotlib.pyplot as plt

fig = plt.figure(figsize=(20, 20))

width = 500
height = 500

alpha = 0.9
w = 1.0
b1 = -10
b2 = 10

x = []
y = []
for i in range(width):
    # Tick of the parameter
    b = b1 + (b2 - b1) * float(i) / width

    # Random Initialization
    h = 2 * random.random() - 1
    for j in range(1000):
        # RNN-map
        h = alpha * h + (1 - alpha) * (1 / (1 + math.exp(-(w * h + b))))
        if j > 100:
            x.append(b)
            y.append(h)

plt.scatter(x, y, s=1)
plt.xlabel("bias")
plt.ylabel("hidden activation")
plt.grid(True)
plt.show()