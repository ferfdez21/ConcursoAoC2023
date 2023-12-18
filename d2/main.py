with open("input.txt") as puzzle:
    result = 0
    for line in puzzle:
        [nth_game,cube_sets] = line.split(':')
        nth_game = int(nth_game.split(' ')[1])
        for cube_set in cube_sets.split(';'):
            possible = True
            cube_count = {'red': 0, 'green': 0, 'blue': 0}
            for cube_selection in cube_set.split(', '):
                [n_cubes, cube_type] = cube_selection.strip().split(' ')
                cube_count[cube_type] = int(n_cubes)
            possible = cube_count['red'] <= 12 and cube_count['green'] <= 13 and cube_count['blue'] <= 14
            if not possible: break
        if possible:
            result += nth_game
    print(result)