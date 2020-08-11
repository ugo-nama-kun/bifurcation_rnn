import random
import math

import matplotlib.pyplot as plt

fig = plt.figure(figsize=(20, 20))

width = 500
height = 500

w1 = -20.0
w2 = 20.0
b = 0.2

x = []
y = []
for i in range(width):
    # Tick of the parameter
    w = w1 + (w2 - w1) * float(i) / width

    # Random Initialization
    h = 2 * random.random() - 1
    for j in range(1000):
        # RNN-map
        h = math.tanh(w * h + b)  # Tanh
        # h = 1/(1 + math.exp(-(w * h + b)))  # Sigmoid
        # h = max(w * h + b, 0)  # Relu
        if j > 100:
            x.append(w)
            y.append(h)

plt.scatter(x, y, s=1)
plt.xlabel("weight")
plt.ylabel("hidden activation")
plt.grid(True)
plt.show()