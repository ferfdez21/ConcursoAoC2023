with open("input.txt") as puzzle:
    result = 0
    for line in puzzle:
        result_line = [c for c in line if c.isdigit()]
        result_line = result_line[::len(result_line)-1] if len(result_line) >= 2 else result_line*2
        result += int("".join(result_line))
    print(result)