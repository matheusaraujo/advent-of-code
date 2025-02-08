class Computer {
  constructor(instructions, initialState = {}) {
    this.instructions = instructions.map((instruction) =>
      instruction.split(" "),
    );
    this.registers = { a: 0, b: 0, c: 0, d: 0, ...initialState };
    this.operations = {
      cpy: (arg1, arg2) => {
        this.registers[arg2] = isNaN(arg1)
          ? this.registers[arg1]
          : parseInt(arg1);
      },
      inc: (arg1) => {
        this.registers[arg1]++;
      },
      dec: (arg1) => {
        this.registers[arg1]--;
      },
      jnz: (arg1, arg2) => {
        const value = isNaN(arg1) ? this.registers[arg1] : parseInt(arg1);
        return value !== 0 ? parseInt(arg2) : 1;
      },
    };
  }

  execute() {
    let memPointer = 0;

    while (memPointer < this.instructions.length) {
      const [instruction, arg1, arg2] = this.instructions[memPointer];
      const jumpOffset = this.operations[instruction](arg1, arg2);
      memPointer += jumpOffset || 1;
    }

    return this.registers.a;
  }
}

module.exports = Computer;
