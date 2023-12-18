import re

number_dict = {
    "one":'1',
    "two":'2',
    "three":'3',
    "four":'4',
    "five":'5',
    "six":'6',
    "seven":'7',
    "eight":'8',
    "nine":'9'
}

with open("input.txt") as puzzle:
    result = 0
    for line in puzzle:
        result_line = []
        
        # The pattern looks for sequences of digits or spelled out numbers from one to nine
        pattern = r'\d|one|two|three|four|five|six|seven|eight|nine'

        # Find all matches
        result_line = re.findall(pattern, line)

        for i,match in enumerate(result_line):
            if not match.isdigit():
                result_line[i] = number_dict[match]
        print(line, result_line)
        result_line = result_line[::len(result_line)-1] if len(result_line) >= 2 else result_line*2

        result += int("".join(result_line))
        break
    print(result)