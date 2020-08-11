import random
import math

import matplotlib.pyplot as plt

fig = plt.figure(figsize=(20, 20))

width = 500
height = 500

w = 3
b1 = -4.0
b2 = 4.0

x = []
y = []
for i in range(width):
    # Tick of the parameter
    b = b1 + (b2 - b1) * float(i) / width

    # Random Initialization
    h = 2 * random.random() - 1
    for j in range(1000):
        # RNN-map
        h = math.tanh(w * h + b)
        #h = 1/(1 + math.exp(-(w * h + b)))  # Sigmoid
        # h = max(w * h + b, 0)  # Relu
        if j > 100:
            x.append(b)
            y.append(h)

plt.scatter(x, y, s=1)
plt.xlabel("bias")
plt.ylabel("hidden activation")
plt.grid(True)
plt.show()