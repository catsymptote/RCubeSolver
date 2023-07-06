import pytest

from rcube.pochmann_solver import PochmannSolver
from rcube.cube_interface import CubeInterface
from rcube.scrambler import Scrambler


def get_ps(scramble=None):
    if scramble is None:
        scramble = ['U']

    cube = CubeInterface()
    cube.apply_moves(scramble)
    ps = PochmannSolver(cube)
    return ps


def to_list(scramble):
    if type(scramble) is list:
        return scramble
    if scramble.count(' ') == 0 and "'" not in scramble and "2" not in scramble:
        return list(scramble)
    scramble = scramble.split()
    return scramble


def test_to_list():
    assert to_list("U R U' R'") == ['U', 'R', "U'", "R'"]
    assert to_list("U") == ['U']
    assert to_list("U'") == ["U'"]
    assert to_list(['a', 'A', 'b']) == ['a', 'A', 'b']
    assert to_list('aAb') == ['a', 'A', 'b']


def test_init():
    ps = get_ps()
    assert type(ps) is PochmannSolver
    assert type(ps.cube) is CubeInterface


def test_get_piece_letters():
    ps = get_ps()
    assert ps.get_piece_letters('U') == 'KU'
    assert ps.get_piece_letters('q') == 'bqn'
    assert ps.get_piece_letters('y') is None


def test_is_same_piece():
    ps = get_ps()
    assert ps.is_same_piece('U', 'K')
    assert ps.is_same_piece('e', 'a')
    assert not ps.is_same_piece('U', 'V')
    assert not ps.is_same_piece('e', 'b')


def test_shot_finished():
    ps = get_ps()
    assert ps.shot_finished('U', ['K'])
    assert ps.shot_finished('K', ['K'])
    assert ps.shot_finished('q', ['K', 'b', 'v'])
    assert not ps.shot_finished('q', ['K', 't', 'v'])
    assert ps.shot_finished('A', ['A', 'D', 'C'])


@pytest.mark.parametrize('scramble, shots, corner, exp_poss_shots, exp_buffer, exp_current_buffer', [
    (['U'], [], False, 'ACDEFGHIJKLMNOPQRSTUVWX', 'B', 'A'),
    (['U'], ['A'], False, 'ACDEFGHIJKLMNOPQRSTUVWX', 'B', 'D'),
    (['U'], ['A', 'D'], False, 'ACDEFGHIJKLMNOPQRSTUVWX', 'B', 'C'),
    (['U'], ['A', 'D', 'C'], False, 'ACDEFGHIJKLMNOPQRSTUVWX', 'B', 'B'),
    (['U'], ['A', 'D', 'C'], True, 'bcdefghijklmnopqrstuvw', 'a', 'd'),
    (['U'], ['A', 'D', 'C', 'd'], True, 'bcdefghijklmnopqrstuvw', 'a', 'c'),

    (['U2'], [], False, 'ACDEFGHIJKLMNOPQRSTUVWX', 'B', 'D'),
    (['U2'], ['D'], False, 'ACDEFGHIJKLMNOPQRSTUVWX', 'B', 'B'),
    (['U2'], ['D', 'A'], False, 'ACDEFGHIJKLMNOPQRSTUVWX', 'B', 'C'),
    (['U2'], ['D', 'A', 'C'], False, 'ACDEFGHIJKLMNOPQRSTUVWX', 'B', 'A'),
    (['U2'], ['D', 'A', 'C', 'A'], True, 'bcdefghijklmnopqrstuvw', 'a', 'c')
])
def test_get_next_shot_setup(scramble, shots, corner, exp_poss_shots, exp_buffer, exp_current_buffer):
    ps = get_ps(scramble)
    poss_shots, buffer, current_buffer = ps.get_next_shot_setup(shots, corner)
    assert buffer == exp_buffer
    assert current_buffer == exp_current_buffer
    assert poss_shots == exp_poss_shots


@pytest.mark.parametrize('scramble, shots, corner, exp_next_shot', [
    (['U'], [], False, 'A'),
    (['U'], ['A'], False, 'D'),
    (['U'], ['A', 'D'], False, 'C'),
    (['U'], ['A', 'D', 'C'], False, None),
    (['U'], ['A', 'D', 'C'], True, 'd'),
    (['U'], ['A', 'D', 'C', 'd'], True, 'c'),

    (['U2'], [], False, 'D'),
    (['U2'], ['D'], False, 'A*'),  # New loop
    (['U2'], ['D', 'A*'], False, 'C'),
    (['U2'], ['D', 'A*', 'C'], False, 'A'),
    (['U2'], ['D', 'A', 'C', 'A'], False, None),
    (['U2'], ['D', 'A', 'C', 'A'], True, 'c'),
    (['U2'], ['D', 'A', 'C', 'A', 'c'], True, 'b*'),
    (['U2'], ['D', 'A', 'C', 'A', 'c', 'b*'], True, 'd'),
    (['U2'], ['D', 'A', 'C', 'A', 'c', 'b*', 'd'], True, 'b'),
    (['U2'], ['D', 'A', 'C', 'A', 'c', 'b', 'd', 'b'], True, None),
])
def test_get_next_shot(scramble, shots, corner, exp_next_shot):
    ps = get_ps(scramble)
    next_shot = ps.get_next_shot(shots, corner)
    assert next_shot == exp_next_shot



@pytest.mark.parametrize('scramble, exp_solution', [
    (to_list("U"), to_list('ADC-dcb')),
    (to_list("R"), to_list('JVT-bjvtb')),
    (to_list("F"), to_list('CFUPC-cfupc')),
    (to_list("D"), to_list('GSOKG-gsokg')),
    (to_list("L"), to_list('DRXLD-sui')),
    (to_list("B"), to_list('ANWHA-nwh')),
    (to_list("U2"), to_list('DACAcbdb')),
    (to_list("U'"), to_list('CDA-bcd')),
    (to_list("R U"), to_list('ADCJVTdkwqcj')),
    (['L', 'F2', 'R', 'U2', 'F2', "R'", 'F2', 'R', 'F2', 'D2', 'F2', "D'", "R'", "B'", 'U2', "L'", "B'", 'U2', 'R2', "U'", 'B'], ['A', 'O', 'H', 'J', 'S', 'A', 'C', 'D', 'G', 'T', 'K', 'F', 'I', '-', 'u', 'w', 'c', 'b', 'x', 'q', 'd', 'v', 'f'])
])
def test_get_pochmann_shots(scramble, exp_solution):
    ps = get_ps(scramble)
    assert ps.get_pochmann_shots() == exp_solution


def test_get_solution():
    scrambler = Scrambler()
    scramble = scrambler.get_scramble()
    ps = get_ps(scramble)
    assert not ps.cube.is_complete()
    solution = ps.get_solution()
    ps.cube.apply_moves(solution['moves'])
    assert ps.cube.is_complete()
