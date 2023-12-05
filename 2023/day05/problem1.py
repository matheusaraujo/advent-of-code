import re
import sys

def convert_1d_to_2d(l, cols):
    return [l[i:i + cols] for i in range(0, len(l), cols)]

def read_input(input, begin, end):
    i1, i2 = input.index(begin), input.index(end) if end else len(input)
    s = input[i1:i2]
    return [int(n) for n in re.findall(r'\d+', s)]

def read_map(input, begin, end):
    return convert_1d_to_2d(read_input(input, begin, end), 3)

def map_function(source, mapping):
    for m in mapping:
        if source >= m[1] and source <= m[1] + m[2]:
            return source - (m[1] - m[0])
    return source

def problem1(input):
    seeds = read_input(input, 'seeds', 'seed-to-soil')
    seed_to_soil = read_map(input, 'seed-to-soil', 'soil-to-fertilizer')
    soil_to_fertilizer = read_map(input, 'soil-to-fertilizer', 'fertilizer-to-water')
    fertilizer_to_water = read_map(input, 'fertilizer-to-water', 'water-to-light')
    water_to_light = read_map(input, 'water-to-light', 'light-to-temperature')
    light_to_temperature = read_map(input, 'light-to-temperature', 'temperature-to-humidity')
    temperature_to_humidity = read_map(input, 'temperature-to-humidity', 'humidity-to-location')
    humidity_to_location = read_map(input, 'humidity-to-location', '')

    ans = sys.maxsize

    for seed in seeds:
        soil = map_function(seed, seed_to_soil)
        fertilizer = map_function(soil, soil_to_fertilizer)
        water = map_function(fertilizer, fertilizer_to_water)
        light = map_function(water, water_to_light)
        temperature = map_function(light, light_to_temperature)
        humidity = map_function(temperature, temperature_to_humidity)
        location = map_function(humidity, humidity_to_location)

        ans = min(ans, location)

    return ans