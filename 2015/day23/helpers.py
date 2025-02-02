class Computer:
    def __init__(self, program, register_a=0, register_b=0):
        self.program = [line.replace(",", "").split() for line in program]
        self.pointer = 0
        self.registers = {"a": register_a, "b": register_b}

    def run(self):
        while 0 <= self.pointer < len(self.program):
            instruction, *args = self.program[self.pointer]
            self.execute(instruction, *args)
        return self.registers["b"]

    def execute(self, instruction, *args):
        if instruction == "hlf":
            self.registers[args[0]] //= 2
            self.pointer += 1
        elif instruction == "tpl":
            self.registers[args[0]] *= 3
            self.pointer += 1
        elif instruction == "inc":
            self.registers[args[0]] += 1
            self.pointer += 1
        elif instruction == "jmp":
            self.pointer += int(args[0])
        elif instruction == "jie":
            if self.registers[args[0]] % 2 == 0:
                self.pointer += int(args[1])
            else:
                self.pointer += 1
        elif instruction == "jio":
            if self.registers[args[0]] == 1:
                self.pointer += int(args[1])
            else:
                self.pointer += 1
