import random
from PIL import Image

width = 500
height = 500

canvas = Image.new("RGB", (width+1, height+1), (0,0,0))
a1 = 1.0
a2 = 4.0

for i in range(width):
    # Tick of the parameter
    a = a1 + (a2 - a1) * float(i) / width

    # Random Initialization
    x = random.random()
    for j in range(1000):
        # Logistic map
        x = a * x * (1 - x)
        if j > 100:
            canvas.putpixel((i, height - int(x * height)), (255, 255, 255))

canvas.save("../logistic_map.png")