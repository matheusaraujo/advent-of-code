import re


class Reindeer:
    def __init__(self, input_line):
        name, speed, fly_time, rest_time = re.match(
            r"(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.",
            input_line,
        ).groups()

        self.name = name
        self.speed = int(speed)
        self.fly_time = int(fly_time)
        self.rest_time = int(rest_time)
        self.cycle_length = self.fly_time + self.rest_time
        self.points = self.position = 0

    def position_at(self, seconds):
        full_cycles = seconds // self.cycle_length
        remaining_time = seconds % self.cycle_length
        distance = full_cycles * self.fly_time * self.speed
        distance += min(remaining_time, self.fly_time) * self.speed
        self.position = distance
        return distance

    def win_points(self):
        self.points += 1
