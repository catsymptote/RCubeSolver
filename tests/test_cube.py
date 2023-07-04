from rcube.cube import Cube
from rcube.block import Block
from rcube.settings import Settings



def test_cube():
    Settings.use_BLD_notation = False

    c = Cube()

    assert type(c) is Cube

    assert type(c.faces) is list
    assert len(c.faces) == 6

    assert type(c.faces[0]) is list
    assert len(c.faces[0]) == 9

    assert type(c.faces[0][0]) is str
    assert c.faces[0][0] == "Y"


def test_list_equality():
    pass


def test_get_block():
    Settings.use_BLD_notation = False

    c = Cube()
    a = c.get_block("A")
    b = c.get_block("B")

    assert type(a) is Block
    assert a.block_type == "corner"
    assert a.stickers == ["Y", "O", "G"]

    assert type(b) is Block
    assert b.block_type == "corner"
    assert b.stickers == ["Y", "G", "R"]


def test_is_complete():
    c = Cube()
    assert c.is_complete()
    c.faces[0][0] = "O"
    assert not c.is_complete()


def test_show():
    pass


def test_simple_show():
    pass


def test_altshow():
    pass


def test_X_cube_rotation():
    pass


def test_Y_cube_rotation():
    pass


def test_Z_cube_rotation():
    pass


def test_U_slice_rotation():
    pass


def test_E_slice_rotation():
    pass


def test_outer_slice_rotation():
    pass


def test_face_rotation():
    pass


def test_face_flip():
    pass
