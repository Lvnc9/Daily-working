#!/usr/bin/python3
# Start
# Ho hooo here we come with AI algorithm STUFF!!!!
# Modules
import csv
from random import random
import math
from collections import Counter


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


def write_results(filename="output.csv"):
    with open(filename, "w") as file:
        writer = csv.writer(file)
        while True:
            color, name = yield
            writer.writerow(list(color) + [name])


def name_colors(get_neighbors):
    color = yield
    while True:
        near = get_neighbors.send(color)
        name_guess = Counter(
            n[1] for n in near).most_common(1)[0][0]
        color = yield name_guess


def process_colors(dataset_filename="colors.csv"):
    model_colors = load_colors(dataset_filename)
    get_neighbors = nearest_neighbors(model_colors, 5)
    get_color_name = name_colors(get_neighbors)
    output = write_results()
    next(output)
    next(get_neighbors)
    next(get_color_name)

    for color in generate_colors():
        name = get_color_name.send(color)
        output.send((color, name))


results = write_results()
next(results)
for i in range(3):
    print(i)
    results.send(((i, i, i), i * 10))

process_colors()
# End