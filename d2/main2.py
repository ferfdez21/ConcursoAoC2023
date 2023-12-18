import numpy as np

with open("input.txt") as puzzle:
    result = 0
    for line in puzzle:
        [nth_game,cube_sets] = line.split(':')
        nth_game = int(nth_game.split(' ')[1])
        cube_min = {'red': 0, 'green': 0, 'blue': 0}
        for cube_set in cube_sets.split(';'):
            for cube_selection in cube_set.split(', '):
                [n_cubes, cube_type] = cube_selection.strip().split(' ')
                if cube_min[cube_type] < int(n_cubes): cube_min[cube_type] = int(n_cubes)
        result += np.prod(list(cube_min.values()))
    print(result)