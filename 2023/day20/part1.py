from abc import abstractmethod
from dataclasses import dataclass


@dataclass
class Pulse:
    signal: int
    source: str
    target: str

    def __str__(self):
        s = "high" if self.signal == 1 else "low"
        return f"{self.source} -{s}-> {self.target}"


class Module:
    def __init__(self, identifier: str, connections: [str]):
        self.id = identifier
        self.state = 0
        self.connections = connections

    @abstractmethod
    def receives(self, pulse: Pulse) -> [Pulse]:
        pass

    def __str__(self):
        return (
            "module "
            f"id: {self.id}, "
            f"state: {self.state}, "
            f"type: {type(self)}, "
            f"connections {','.join(self.connections)}"
        )


# pylint: disable=too-few-public-methods
class Broadcast(Module):
    def receives(self, pulse: Pulse) -> [Pulse]:
        return [
            Pulse(signal=pulse.signal, source=self.id, target=connection)
            for connection in self.connections
        ]


# pylint: disable=too-few-public-methods
class FlipFlop(Module):
    def receives(self, pulse: Pulse) -> [Pulse]:
        if pulse.signal == 1:
            return None

        self.state = 1 if self.state == 0 else 0

        return [
            Pulse(signal=self.state, source=self.id, target=connection)
            for connection in self.connections
        ]


# pylint: disable=too-few-public-methods
class Conjunction(Module):
    def __init__(self, identifier: str, connections: [str]):
        super().__init__(identifier, connections)
        self.inputs = {}

    def add_input(self, input_identifiers):
        for input_id in input_identifiers:
            self.inputs[input_id] = 0

    def receives(self, pulse: Pulse) -> [Pulse]:
        self.state = pulse.signal
        self.inputs[pulse.source] = pulse.signal

        signal = 0 if all(s == 1 for s in self.inputs.values()) else 1

        return [
            Pulse(signal=signal, source=self.id, target=connection)
            for connection in self.connections
        ]


def part1(puzzle_input):
    modules, limit = [], 1000

    for line in puzzle_input:
        identifier, connections = line.split(" -> ")

        connections = connections.replace(" ", "").split(",")

        if identifier[0] == "%":
            modules.append(FlipFlop(identifier[1:], connections))
        elif identifier[0] == "&":
            modules.append(Conjunction(identifier[1:], connections))
        elif identifier[0] == "b":
            modules.append(Broadcast(identifier, connections))
        else:
            raise ValueError(f"invalid identifier: {identifier}")

    cnt_button, cnt_high, cnt_low = 0, 0, 0

    for module in modules:
        if isinstance(module, Conjunction):
            inputs = [m.id for m in modules if module.id in m.connections]
            module.add_input(inputs)

    while True:
        pulses = [Pulse(signal=0, source="button", target="broadcaster")]
        cnt_button += 1

        while len(pulses) > 0:
            pulse = pulses.pop(0)

            cnt_high += 1 if pulse.signal == 1 else 0
            cnt_low += 1 if pulse.signal == 0 else 0

            target = next(filter(lambda m: m.id == pulse.target, modules), None)

            if target is None:
                continue

            new_pulses = target.receives(pulse)

            if new_pulses is None:
                continue

            pulses += new_pulses

        if cnt_button == limit or all(m.state == 0 for m in modules):
            break

    return (limit // cnt_button * cnt_high) * (limit // cnt_button * cnt_low) + (
        limit % cnt_button * cnt_high
    ) * (limit % cnt_button * cnt_low)
