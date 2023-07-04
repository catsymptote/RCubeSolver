from cube_interface import CubeInterface
from scrambler import Scrambler
from pochmann_solver import PochmannSolver


# Make cube
cube = CubeInterface()

print('### New cube')
print('Solved:', cube.is_complete())
print(cube.show())

# Scramble cube
scrambler = Scrambler(cube)
cube = scrambler.scramble()

print('### Scrabmled cube')
print('Solved:', cube.is_complete())
print(cube.show())

# Find solution
solver = PochmannSolver(cube)
moves = solver.get_moves()

# Solve cube
cube.apply_moves(moves)

print('### Solved cube')
print('Solved:', cube.is_complete())
print(cube.show())
