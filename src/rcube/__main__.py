import sys

from rcube.cube_interface import CubeInterface
from rcube.pochmann_solver import PochmannSolver
from rcube.scrambler import Scrambler
from rcube.logger import Logger


def main():
    if len(sys.argv) > 1 and sys.argv[1] != 'shots':
        scramble = sys.argv[1].split()
    else:
        scramble = Scrambler().get_scramble()

    # Set up cube (cubeInterface)
    cube = CubeInterface()
    assert cube.is_complete()

    cube.apply_moves(scramble)

    assert not cube.is_complete()

    # Only-print-shots mode
    if len(sys.argv) > 1 and sys.argv[1] == "shots":
        ps = PochmannSolver(cube)
        solution = ps.get_solution()
        stats = ps.get_stats()
        print(stats["len_shots"])
        sys.exit(0)

    else:
        print(f'Scramble: {scramble}')
        cube.show()

    # Find solution
    ps = PochmannSolver(cube)
    solution = ps.get_solution()
    stats = ps.get_stats()
    print(f'Number of shots: {stats["len_shots"]}')
    print(f'Number of moves: {len(solution["moves"])}')
    print()
    print(f'OP shots: {solution["shots"]}')
    # print(f'Moves: {" ".join(solution["moves"])}')
    print(Logger.base_moves)

    # Solve
    cube.apply_moves(solution['moves'])
    cube.show()
    assert cube.is_complete()

    # print(Logger().print_moves())


if __name__ == '__main__':
    main()
