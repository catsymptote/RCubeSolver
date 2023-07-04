from rcube.cube_interface import CubeInterface
# from rcube.scrambler import Scrambler
from rcube.pochmann_solver import PochmannSolver


# Make cube
cube = CubeInterface()

print('### New cube')
print('Solved:', cube.is_complete())
cube.show()

cube.apply_moves(["R'"])
# cube.apply_moves(['L', 'F2', 'R', 'U2', 'F2', "R'", 'F2', 'R', 'F2', 'D2', 'F2', "D'", "R'", "B'", 'U2', "L'", "B'", 'U2', 'R2', "U'", 'B'])  # noqa
# Scramble cube
# scrambler = Scrambler(cube)
# cube = scrambler.scramble()

print('### Scrabmled cube')
print('Solved:', cube.is_complete())
cube.show()

# Find solution
solver = PochmannSolver(cube)
moves = solver.get_solution()

# Solve cube
cube.apply_moves(moves)

print('### Solved cube')
print('Solved:', cube.is_complete())
cube.show()
