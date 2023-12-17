import json
from enum import Enum


class ParameterMode(Enum):
    POSITION = 0
    IMMEDIATE = 1
    RELATIVE = 2


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
    ADJUST_RELATIVE_BASE = 9


class Parameter:
    def __init__(self, address: int, mode: ParameterMode):
        self.__address = address
        self.__mode = mode

    def address(self):
        return self.__address

    def mode(self):
        return self.__mode


class Command:
    def __init__(self, pointer, memory_value):
        self.address = pointer
        self.value = memory_value

    def __str__(self):
        return json.dumps({"operation": self.operation().name})

    def operation(self) -> Operation:
        return Operation(self.value % 100)

    def parameter_1(self) -> Parameter:
        return Parameter(self.address + 1, ParameterMode((self.value // 100) % 10))

    def parameter_2(self) -> Parameter:
        return Parameter(self.address + 2, ParameterMode((self.value // 1000) % 10))

    def parameter_3(self) -> Parameter:
        return Parameter(self.address + 3, ParameterMode((self.value // 10000) % 10))

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
            Operation.ADJUST_RELATIVE_BASE: 2,
        }[self.operation()]


class IntCode:
    def __init__(self, program: list[int], input_array: list[int]):
        self.pointer = 0  # memory pointer
        self.relative_base = 0
        self.command = None
        self.memory = {idx: val for idx, val in enumerate(program)}
        self.input = input_array
        self.output = None
        self.halt = False

    def execute(self, input_array: list[int]):
        self.input += input_array

        while True:
            self.command = Command(self.pointer, self.memory[self.pointer])

            if self.command.operation() == Operation.ADDS:
                self.pointer += self.__adds()
            elif self.command.operation() == Operation.MULTIPLIES:
                self.pointer += self.__multiplies()
            elif self.command.operation() == Operation.READ_INPUT:
                self.pointer += self.__read_input()
            elif self.command.operation() == Operation.JUMP_IF_TRUE:
                self.pointer += self.__jump_if_true()
            elif self.command.operation() == Operation.JUMP_IF_FALSE:
                self.pointer += self.__jump_if_false()
            elif self.command.operation() == Operation.LESS_THAN:
                self.pointer += self.__less_than()
            elif self.command.operation() == Operation.EQUALS:
                self.pointer += self.__equals()
            elif self.command.operation() == Operation.ADJUST_RELATIVE_BASE:
                self.pointer += self.__adjust_relative_base()
            elif self.command.operation() == Operation.WRITE_OUTPUT:
                self.pointer += self.__write_output()
                break
            elif self.command.operation() == Operation.HALT:
                self.pointer += self.__halt()
                break

        return self.output

    def __str__(self):
        return json.dumps(
            {
                "pointer": self.pointer,
                "value": self.memory[self.pointer],
            }
        )

    def __adds(self):
        self.__set(
            self.command.parameter_3(),
            (
                self.__get(self.command.parameter_1())
                + self.__get(self.command.parameter_2())
            ),
        )
        return self.command.size()

    def __multiplies(self):
        self.__set(
            self.command.parameter_3(),
            (
                self.__get(self.command.parameter_1())
                * self.__get(self.command.parameter_2())
            ),
        )
        return self.command.size()

    def __read_input(self):
        self.__set(self.command.parameter_1(), self.input.pop(0))
        return self.command.size()

    def __write_output(self):
        self.output = self.__get(self.command.parameter_1())
        return self.command.size()

    def __jump_if_true(self):
        return (
            self.__get(self.command.parameter_2()) - self.pointer
            if self.__get(self.command.parameter_1()) > 0
            else self.command.size()
        )

    def __jump_if_false(self):
        return (
            self.__get(self.command.parameter_2()) - self.pointer
            if self.__get(self.command.parameter_1()) == 0
            else self.command.size()
        )

    def __less_than(self):
        self.__set(
            self.command.parameter_3(),
            1
            if (
                self.__get(self.command.parameter_1())
                < self.__get(self.command.parameter_2())
            )
            else 0,
        )
        return self.command.size()

    def __equals(self):
        self.__set(
            self.command.parameter_3(),
            1
            if (
                self.__get(self.command.parameter_1())
                == self.__get(self.command.parameter_2())
            )
            else 0,
        )
        return self.command.size()

    def __adjust_relative_base(self):
        self.relative_base += self.__get(self.command.parameter_1())
        return self.command.size()

    def __halt(self):
        self.halt = True
        return self.command.size()

    def __get(self, parameter: Parameter):
        idx = -1
        if parameter.mode() == ParameterMode.IMMEDIATE:
            idx = parameter.address()
        elif parameter.mode() == ParameterMode.POSITION:
            idx = self.memory[parameter.address()]
        elif parameter.mode() == ParameterMode.RELATIVE:
            idx = self.relative_base + self.memory[parameter.address()]
        else:
            raise ValueError("invalid parameter mode")

        if idx not in self.memory:
            self.memory[idx] = 0
        return self.memory[idx]

    def __set(self, parameter: Parameter, value: int):
        if parameter.mode() == ParameterMode.IMMEDIATE:
            self.memory[parameter.address()] = value
        elif parameter.mode() == ParameterMode.POSITION:
            self.memory[self.memory[parameter.address()]] = value
        elif parameter.mode() == ParameterMode.RELATIVE:
            self.memory[self.relative_base + self.memory[parameter.address()]] = value
        else:
            raise ValueError("invalid parameter mode")
