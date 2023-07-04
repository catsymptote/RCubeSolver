from rcube.cube_interface import CubeInterface


def test_init():
    intp = CubeInterface()
    assert type(intp) is CubeInterface


def test_full():
    intp = CubeInterface()
    intp.apply_moves(['L', 'F2', 'R', 'U2', 'F2', "R'", 'F2'])
    intp.apply_moves(['F2', 'R', 'F2', 'U2', "R'", 'F2', "L'"])
    intp.show()
    assert intp.is_complete()
