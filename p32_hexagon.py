# drawing a hexagonal grid
# a Python implementation of: Indera's Pearls, page 32, box 3

import random
import math
from PIL import Image
from PIL import ImageDraw


def hexagon(center, radius):
    v0 = (center[0], center[1] + radius)
    v1 = (center[0] - radius * math.sqrt(3) / 2, center[1] + radius / 2)
    v2 = (center[0] - radius * math.sqrt(3) / 2, center[1] - radius / 2)
    v3 = (center[0], center[1] - radius)
    v4 = (center[0] + radius * math.sqrt(3) / 2, center[1] - radius / 2)
    v5 = (center[0] + radius * math.sqrt(3) / 2, center[1] + radius / 2)
    return (v0, v1, v2, v3, v4, v5)


def genT(vertices, radius, power):
    return tuple((x + radius * math.sqrt(3) * power, y) for (x, y) in vertices)


def genS(vertices, radius, power):
    return tuple(
        (x + radius * math.sqrt(3) * power / 2, y + radius * 1.5 * power)
        for (x, y) in vertices)


def drawHexagonalGrid(radius, image):
    draw = ImageDraw.Draw(image)
    center = tuple(math.floor(x / 2) for x in image.size)
    # shrink the hexagons so the background color appears as an outline
    outline = math.floor(radius / 10) + 1
    hexagonVerts = hexagon(center, radius - outline)
    for i in range(-4, 5):
        for j in range(-2, 3):
            # compensate for the horizontal translation of the S generator
            iOffset = math.floor(j / 2)
            translatedVerts = genT(hexagonVerts, radius, i - iOffset)
            translatedVerts = genS(translatedVerts, radius, j)
            color = (random.randint(0, 255), random.randint(0, 255),
                     random.randint(0, 255))
            draw.polygon(translatedVerts, fill=color)


# higher quality results in crisper images
quality = 300
size = (16 * quality, 9 * quality)
radius = math.floor(quality / 1.5)
image = Image.new("RGB", size, (255, 255, 255))
drawHexagonalGrid(radius, image)
image.save("image.png")
image.show()
