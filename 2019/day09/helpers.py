from dataclasses import dataclass
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
        }[self]


@dataclass
class Parameter:
    def __init__(self, address: int, mode: ParameterMode):
        self.address = address
        self.mode = mode


@dataclass
class Command:
    def __init__(self, __pointer, memory_value):
        self.address = __pointer
        self.value = memory_value
        self.operation = Operation(self.value % 100)
        self.parameter_1 = Parameter(
            self.address + 1, ParameterMode((self.value // 100) % 10)
        )
        self.parameter_2 = Parameter(
            self.address + 2, ParameterMode((self.value // 1000) % 10)
        )
        self.parameter_3 = Parameter(
            self.address + 3, ParameterMode((self.value // 10000) % 10)
        )
        self.size = self.operation.size()


class IntCode:
    def __init__(self, program: list[int], input_array: list[int]):
        self.__pointer = 0  # memory pointer
        self.__relative_base = 0
        self.__command = None
        self.__memory = dict(enumerate(program))
        self.__input = input_array
        self.__output = None
        self.__halted = False

    def run(self, input_array: list[int]):
        self.__input += input_array

        while True:
            self.__command = Command(self.__pointer, self.__memory[self.__pointer])
            self.__pointer += self.__execute_command()

            if self.__command.operation in (Operation.WRITE_OUTPUT, Operation.HALT):
                break

        return self.__output

    def halted(self) -> bool:
        return self.__halted

    def __execute_command(self):
        functions = {
            Operation.ADDS: self.__adds,
            Operation.MULTIPLIES: self.__multiplies,
            Operation.READ_INPUT: self.__read_input,
            Operation.JUMP_IF_TRUE: self.__jump_if_true,
            Operation.JUMP_IF_FALSE: self.__jump_if_false,
            Operation.LESS_THAN: self.__less_than,
            Operation.EQUALS: self.__equals,
            Operation.ADJUST_RELATIVE_BASE: self.__adjust_relative_base,
            Operation.WRITE_OUTPUT: self.__write_output,
            Operation.HALT: self.__halt,
        }

        if self.__command.operation not in functions:
            raise ValueError("invalid operation")

        return functions[self.__command.operation]()

    def __adds(self):
        self.__set(
            self.__command.parameter_3,
            (
                self.__get(self.__command.parameter_1)
                + self.__get(self.__command.parameter_2)
            ),
        )
        return self.__command.size

    def __multiplies(self):
        self.__set(
            self.__command.parameter_3,
            (
                self.__get(self.__command.parameter_1)
                * self.__get(self.__command.parameter_2)
            ),
        )
        return self.__command.size

    def __read_input(self):
        self.__set(self.__command.parameter_1, self.__input.pop(0))
        return self.__command.size

    def __write_output(self):
        self.__output = self.__get(self.__command.parameter_1)
        return self.__command.size

    def __jump_if_true(self):
        return (
            self.__get(self.__command.parameter_2) - self.__pointer
            if self.__get(self.__command.parameter_1) > 0
            else self.__command.size
        )

    def __jump_if_false(self):
        return (
            self.__get(self.__command.parameter_2) - self.__pointer
            if self.__get(self.__command.parameter_1) == 0
            else self.__command.size
        )

    def __less_than(self):
        self.__set(
            self.__command.parameter_3,
            (
                1
                if (
                    self.__get(self.__command.parameter_1)
                    < self.__get(self.__command.parameter_2)
                )
                else 0
            ),
        )
        return self.__command.size

    def __equals(self):
        self.__set(
            self.__command.parameter_3,
            (
                1
                if (
                    self.__get(self.__command.parameter_1)
                    == self.__get(self.__command.parameter_2)
                )
                else 0
            ),
        )
        return self.__command.size

    def __adjust_relative_base(self):
        self.__relative_base += self.__get(self.__command.parameter_1)
        return self.__command.size

    def __halt(self):
        self.__halted = True
        return self.__command.size

    def __get(self, parameter: Parameter):
        idx = -1
        if parameter.mode == ParameterMode.IMMEDIATE:
            idx = parameter.address
        elif parameter.mode == ParameterMode.POSITION:
            idx = self.__memory[parameter.address]
        elif parameter.mode == ParameterMode.RELATIVE:
            idx = self.__relative_base + self.__memory[parameter.address]
        else:
            raise ValueError("invalid parameter mode")

        if idx not in self.__memory:
            self.__memory[idx] = 0
        return self.__memory[idx]

    def __set(self, parameter: Parameter, value: int):
        if parameter.mode == ParameterMode.IMMEDIATE:
            self.__memory[parameter.address] = value
        elif parameter.mode == ParameterMode.POSITION:
            self.__memory[self.__memory[parameter.address]] = value
        elif parameter.mode == ParameterMode.RELATIVE:
            self.__memory[
                self.__relative_base + self.__memory[parameter.address]
            ] = value
        else:
            raise ValueError("invalid parameter mode")
