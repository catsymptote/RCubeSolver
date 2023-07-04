from rcube.solver import Solver


def test_init():
    solv = Solver()
    assert type(solv) is Solver
