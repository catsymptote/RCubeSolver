import sys

from rcube.cube_interface import CubeInterface
from rcube.pochmann_solver import PochmannSolver
from rcube.scrambler import Scrambler
from rcube.logger import Logger
from rcube.algorithm import Algorithm

import time


def time_function(nums):
    durations = []
    for _ in range(nums):
        scramble = Scrambler().get_scramble()
        cube = CubeInterface()
        cube.apply_moves(scramble)
        ps = PochmannSolver(cube)
        _ = ps.get_solution()
        before = time.time()
        _ = ps.get_solution()
        after = time.time()
        duration = after - before
        durations.append(duration)
    average = sum(durations) / len(durations)
    print(f'Average duration: {average} s')


def main():
    # Timing
    if len(sys.argv) > 1 and sys.argv[1] == 'timeit':
        nums = 100
        if len(sys.argv) > 2:
            nums = int(sys.argv[2])
        time_function(nums)
        sys.exit(0)

    do_print = True
    if 'doprint' in sys.argv:
        sys.argv.remove('doprint')
        do_print = False

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
        if do_print:
            print(stats["len_shots"])
        sys.exit(0)

    else:
        if do_print:
            print(f'Scramble: {Algorithm(scramble)}')
            cube.show()

    # Find solution
    ps = PochmannSolver(cube)
    solution = ps.get_solution()
    stats = ps.get_stats()
    if do_print:
        print(f'Number of shots: {stats["len_shots"]}')
        print(f'Number of moves: {len(solution["moves"])}')
        print()
        print(f'OP shots: {solution["shots"]}')
        # print(f'Moves: {" ".join(solution["moves"])}')
        print(Logger.base_moves)

    # Solve
    cube.apply_moves(solution['moves'])
    if do_print:
        cube.show()
    assert cube.is_complete()

    # print(Logger().print_moves())


if __name__ == '__main__':
    main()
