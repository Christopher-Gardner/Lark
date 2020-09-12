# Drawing a hexagonal grid.
# A Python implementation of "box 3" from Indera's Pearls.

import random
import math
from PIL import Image
from PIL import ImageDraw


def getHexagon(center, radius):
    v0 = center[0], center[1] + radius
    v1 = center[0] - radius * math.sqrt(3) / 2, center[1] + radius / 2
    v2 = center[0] - radius * math.sqrt(3) / 2, center[1] - radius / 2
    v3 = center[0], center[1] - radius
    v4 = center[0] + radius * math.sqrt(3) / 2, center[1] - radius / 2
    v5 = center[0] + radius * math.sqrt(3) / 2, center[1] + radius / 2
    return v0, v1, v2, v3, v4, v5


# translation along the x axis
def genT(polygon, radius, power):
    return tuple((x + radius * math.sqrt(3) * power, y) for (x, y) in polygon)


# translation along the line forming a pi / 2 angle with the x axis
def genS(polygon, radius, power):
    return tuple(
        (x + radius * math.sqrt(3) * power / 2, y + radius * 1.5 * power)
        for (x, y) in polygon)


def getRandomColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def drawHexagonalGrid(radius, image):
    draw = ImageDraw.Draw(image)
    center = tuple(math.floor(x / 2) for x in image.size)
    # shrink the hexagons so the background color appears as an outline
    outline = math.ceil(radius / 10)
    polygon = getHexagon(center, radius - outline)
    for i in range(-4, 5):
        for j in range(-2, 3):
            # compensate for the horizontal translation of the S generator
            iOffset = math.floor(j / 2)
            translated = genT(polygon, radius, i - iOffset)
            translated = genS(translated, radius, j)
            color = getRandomColor()
            if i == 0 and j == 0:
                color = 200, 200, 200
            draw.polygon(translated, fill=color)


quality = 300
size = (16 * quality, 9 * quality)
radius = math.ceil(quality / 1.5)
image = Image.new("RGB", size, (255, 255, 255))
drawHexagonalGrid(radius, image)
image.save("image.png")
image.show()
