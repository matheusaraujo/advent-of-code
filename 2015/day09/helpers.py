import re
from itertools import permutations


def parse_input(input_data):
    distances, cities = {}, set()

    for line in input_data:
        city1, city2, distance = re.match(r"(\w+) to (\w+) = (\d+)", line).groups()
        distances[(city1, city2)] = distances[(city2, city1)] = int(distance)
        cities.add(city1)
        cities.add(city2)

    return distances, cities


def solve(puzzle_input, func):
    distances, cities = parse_input(puzzle_input)
    city_permutations = permutations(cities)
    permutations_distances = []

    for perm in city_permutations:
        total_distance = 0
        for i in range(len(perm) - 1):
            total_distance += distances[(perm[i], perm[i + 1])]
        permutations_distances.append(total_distance)

    return func(permutations_distances)
