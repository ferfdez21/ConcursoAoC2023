with open("input.txt") as puzzle:
    points = 0
    for line in puzzle:
        card_power = 0
        [win_numbers, my_numbers] = [l.strip().split(' ') for l in line.split(':')[1].split('|')]
        
        for num in win_numbers:
            if num == '': continue
            if num in my_numbers: card_power += 1
        
        points += 2**(card_power-1) if card_power > 0 else 0
    print(points)