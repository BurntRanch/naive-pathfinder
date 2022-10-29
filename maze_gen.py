import numpy as np
import cv2
from secrets import randbelow
from perlin_noise import PerlinNoise

def generate(width, height):
    out = np.zeros([height, width, 3], dtype=np.uint8)
    y = randbelow(height)

    for x in range(width - 1):
        out[y][x] = [255, 255, 255]
        y += randbelow(3) - 1
        if y < 0:
            y = 0
        out[y][x] = [255, 255, 255]
        out[y][x + 1] = [255, 255, 255]

    cv2.imwrite("maze.png", out)
