# Plotting rotations.
# A Python implementation of project 1.4 from Indera's Pearls.

import random
import math
from PIL import Image
from PIL import ImageDraw


def getParallelogram(origin, scale):
    v0 = origin[0] - scale * 2, origin[1] + 3 * scale
    v1 = origin[0] - scale * 2, origin[1] + 2 * scale
    v2 = origin
    v3 = origin[0], origin[1] + scale
    return v0, v1, v2, v3


def translateVertex(vertex, translation):
    x = vertex[0] + translation[0]
    y = vertex[1] + translation[1]
    return x, y


def translatePolygon(polygon, translation):
    return tuple(translateVertex(vertex, translation) for vertex in polygon)


def rotateVertex(vertex, angle):
    x = vertex[0] * math.cos(angle) - vertex[1] * math.sin(angle)
    y = vertex[1] * math.cos(angle) + vertex[0] * math.sin(angle)
    return x, y


def rotatePolygon(polygon, angle):
    return tuple(rotateVertex(vertex, angle) for vertex in polygon)


def rotatePolygonAboutPoint(polygon, angle, point):
    negatedPoint = -point[0], -point[1]
    translated = translatePolygon(polygon, negatedPoint)
    rotated = rotatePolygon(translated, angle)
    return translatePolygon(rotated, point)


def getRandomColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def plotRotations(scale, image):
    center = tuple(math.floor(x / 2) for x in image.size)
    polygon = getParallelogram(center, scale)
    draw = ImageDraw.Draw(image)
    for i in range(20):
        translated = rotatePolygonAboutPoint(polygon, 100 * math.sqrt(2) * i, center)
        color = getRandomColor()
        draw.polygon(translated, fill=color)


quality = 100
size = 16 * quality, 9 * quality
scale = quality
image = Image.new("RGB", size, (255, 255, 255))
plotRotations(scale, image)
image.save("image.png")
image.show()
