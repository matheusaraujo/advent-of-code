def simulate(puzzle_input) -> int:
    circuit = {}

    for instruction in puzzle_input:
        operation, symbol = instruction.split(" -> ")
        circuit[symbol] = operation

    def get_value(symbol: str) -> int:
        if symbol.isdigit():
            return int(symbol)

        if isinstance(circuit[symbol], int):
            return circuit[symbol]

        parts = circuit[symbol].split()

        if len(parts) == 1:
            result = get_value(parts[0])
        elif parts[0] == "NOT":
            result = ~get_value(parts[1]) & 0xFFFF
        else:
            left, right = get_value(parts[0]), get_value(parts[2])
            operators = {
                "AND": lambda x, y: x & y,
                "OR": lambda x, y: x | y,
                "LSHIFT": lambda x, y: x << y,
                "RSHIFT": lambda x, y: x >> y,
            }
            result = operators[parts[1]](left, right)

        circuit[symbol] = result
        return result

    return get_value("a")
