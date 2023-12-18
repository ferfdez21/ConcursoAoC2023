with open("input.txt") as puzzle:
    scratchcards = 0
    card_amount = {key: 1 for key in range(1,207)}
    
    for line in puzzle:
        card_power = 0
        nth_game = int(line.split(':')[0].split(' ')[-1])
        [win_numbers, my_numbers] = [l.strip().split(' ') for l in line.split(':')[1].split('|')]
        
        for num in win_numbers:
            if num == '': continue
            if num in my_numbers: card_power += 1
        
        for i in range(1,card_power+1):
            if nth_game+i > 207: break
            card_amount[nth_game+i] += card_amount[nth_game]
    
    print(sum(list(card_amount.values())))