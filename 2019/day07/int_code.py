import json
from enum import Enum


class ParameterMode(Enum):
    POSITION = 0
    IMMEDIATE = 1


class Operation(Enum):
    HALT = 99
    ADDS = 1
    MULTIPLIES = 2
    READ_INPUT = 3
    WRITE_OUTPUT = 4
    JUMP_IF_TRUE = 5
    JUMP_IF_FALSE = 6
    LESS_THAN = 7
    EQUALS = 8


class Command:
    def __init__(self, memory_value):
        self.value = memory_value

    def __str__(self):
        return json.dumps({"operation": self.operation().name})

    def operation(self) -> Operation:
        return Operation(self.value % 100)

    def mode_1(self) -> ParameterMode:
        return ParameterMode((self.value // 100) % 10)

    def mode_2(self) -> ParameterMode:
        return ParameterMode((self.value // 1000) % 10)

    def mode_3(self) -> ParameterMode:
        return ParameterMode((self.value // 10000) % 10)

    def size(self):
        return {
            Operation.HALT: 1,
            Operation.ADDS: 4,
            Operation.MULTIPLIES: 4,
            Operation.READ_INPUT: 2,
            Operation.WRITE_OUTPUT: 2,
            Operation.LESS_THAN: 4,
            Operation.EQUALS: 4,
            Operation.JUMP_IF_TRUE: 3,
            Operation.JUMP_IF_FALSE: 3,
        }[self.operation()]


class IntCode:
    def __init__(self, program: list[int], input_array: list[int]):
        self.mp = 0  # memory pointer
        self.memory = program
        self.input = input_array
        self.output = None
        self.halt = False

    def __str__(self):
        return json.dumps(
            {
                "mp": self.mp,
                "value": self.memory[self.mp],
            }
        )

    def __get(self, idx: int, mode: ParameterMode):
        if mode == ParameterMode.POSITION:
            return self.memory[self.memory[idx]]
        if mode == ParameterMode.IMMEDIATE:
            return self.memory[idx]
        raise ValueError("invalid parameter mode")

    def __set(self, idx: int, mode: ParameterMode, value: int):
        if mode == ParameterMode.POSITION:
            self.memory[self.memory[idx]] = value
        elif mode == ParameterMode.IMMEDIATE:
            self.memory[idx] = value
        else:
            raise ValueError("invalid parameter mode")

    def __adds(self, command: Command):
        idx = self.mp
        self.__set(
            idx + 3,
            command.mode_3(),
            (
                self.__get(idx + 1, command.mode_1())
                + self.__get(idx + 2, command.mode_2())
            ),
        )
        return command.size()

    def __multiplies(self, command: Command):
        idx = self.mp
        self.__set(
            idx + 3,
            command.mode_3(),
            (
                self.__get(idx + 1, command.mode_1())
                * self.__get(idx + 2, command.mode_2())
            ),
        )
        return command.size()

    def __read_input(self, command: Command):
        idx = self.mp
        self.__set(idx + 1, command.mode_1(), self.input.pop(0))
        return command.size()

    def __write_output(self, command: Command):
        idx = self.mp
        self.output = self.__get(idx + 1, command.mode_1())
        return command.size()

    def __jump_if_true(self, command: Command):
        idx = self.mp
        return (
            self.__get(idx + 2, command.mode_2()) - self.mp
            if self.__get(idx + 1, command.mode_1()) > 0
            else command.size()
        )

    def __jump_if_false(self, command: Command):
        idx = self.mp
        return (
            self.__get(idx + 2, command.mode_2()) - self.mp
            if self.__get(idx + 1, command.mode_1()) == 0
            else command.size()
        )

    def __less_than(self, command: Command):
        idx = self.mp
        self.__set(
            idx + 3,
            command.mode_3(),
            1
            if (
                self.__get(idx + 1, command.mode_1())
                < self.__get(idx + 2, command.mode_2())
            )
            else 0,
        )
        return command.size()

    def __equals(self, command: Command):
        idx = self.mp
        self.__set(
            idx + 3,
            command.mode_3(),
            1
            if (
                self.__get(idx + 1, command.mode_1())
                == self.__get(idx + 2, command.mode_2())
            )
            else 0,
        )
        return command.size()

    def execute(self, input_array: list[int]):
        self.input += input_array
        command = Command(self.memory[self.mp])

        while True:
            command = Command(self.memory[self.mp])
            delta_mp = 0

            if command.operation() == Operation.ADDS:
                delta_mp = self.__adds(command)
            elif command.operation() == Operation.MULTIPLIES:
                delta_mp = self.__multiplies(command)
            elif command.operation() == Operation.READ_INPUT:
                delta_mp = self.__read_input(command)
            elif command.operation() == Operation.JUMP_IF_TRUE:
                delta_mp = self.__jump_if_true(command)
            elif command.operation() == Operation.JUMP_IF_FALSE:
                delta_mp = self.__jump_if_false(command)
            elif command.operation() == Operation.LESS_THAN:
                delta_mp = self.__less_than(command)
            elif command.operation() == Operation.EQUALS:
                delta_mp = self.__equals(command)
            elif command.operation() == Operation.WRITE_OUTPUT:
                delta_mp = self.__write_output(command)
                self.mp += delta_mp
                break
            elif command.operation() == Operation.HALT:
                self.halt = True
                break

            self.mp += delta_mp

        return self.output
