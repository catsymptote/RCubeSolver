from rcube.scrambler import Scrambler
from rcube.cube_interface import CubeInterface
from rcube.pochmann_solver import PochmannSolver


def test_integration():
    results = {
        'fails': 0,
        'successes': 0,
        'recursions_errors': 0
    }
    runs = 100

    for _ in range(runs):
        # Initialize and scramble
        scr = Scrambler()
        cube = scr.scramble()
        # cube = CubeInterface()
        ps = PochmannSolver(cube)
        assert not cube.is_complete()
        
        # Solve
        solution = ps.get_solution()
        solution_moves = solution['moves']
        cube.apply_moves(solution_moves)

        # Log result
        if cube.is_complete():
            results['successes'] += 1
        else:
            results['fails'] += 1

    print(results)
    assert results['successes'] == runs
    assert results['fails'] == 0
    assert results['recursions_errors'] == 0
