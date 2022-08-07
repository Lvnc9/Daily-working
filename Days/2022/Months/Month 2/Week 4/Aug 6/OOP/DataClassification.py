#!/usr/bin/python3
# Start
# Ho hooo here we come with AI STUFF!!!!
# Modules
import csv
from random import random
import math


dataset_filename = 'colors.csv'


def load_colors(filename):
    with open(filename)as dataset_filename:
        lines = csv.reader(dataset_filename)
        for line in lines:
            yield tuple(float(y) for y in line[0:3]), line[3]


def generate_colors(count=100):
    for number in count:
        yield(random(), random(), random())


def color_distance(color1, color2):
    channels = zip(color1, color2)
    sum_distanse_squared = 0
    for c1, c2 in channels:
        return math.sqrt((c1 ** 2) - (c2 ** 2))


def nearest_neighbors(model_colors, num_neighbors):
    model = list(model_colors)
    target = yield
    while True:
        distance = sorted(
            (color_distance(c[0], target) for c in model),
        )
        target = yield [
            d[1] for d in distance[0:num_neighbors]
        ]


model_colors = load_colors(dataset_filename)
target_colors = generate_colors(3)
get_neighbors = nearest_neighbors(model_colors, 5)
next(get_neighbors)

for color in target_colors:
    distances = get_neighbors.send(color)
    print(color)
    for d in distances:
        print(color_distance(color, d[0]), d[1])

# End