import pytest

from rcube.pochmann_solver import PochmannSolver
from rcube.cube_interface import CubeInterface


def get_ps(scramble=None):
    if scramble is None:
        scramble = ['U']

    cube = CubeInterface()
    cube.apply_moves(scramble)
    ps = PochmannSolver(cube)
    return ps


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
