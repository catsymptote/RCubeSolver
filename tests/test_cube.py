from rcube.cube import Cube
from rcube.block import Block
from rcube.settings import Settings


def to_list(string):
    if type(string) is list:
        return string
    
    string = list(string)
    return string


def test_to_list():
    assert to_list(['a', 'A', 'b']) == ['a', 'A', 'b']
    assert to_list('aAb') == ['a', 'A', 'b']


def get_cube(bld = True):
    Settings.use_BLD_notation = bld

    cube = Cube()

    if bld:
        assert cube.faces == [
            ['a', 'A', 'b', 'D', '0', 'B', 'd', 'C', 'c'],
            ['e', 'E', 'f', 'H', '1', 'F', 'h', 'G', 'g'],
            ['i', 'I', 'j', 'L', '2', 'J', 'l', 'K', 'k'],
            ['m', 'M', 'n', 'P', '3', 'N', 'p', 'O', 'o'],
            ['q', 'Q', 'r', 'T', '4', 'R', 't', 'S', 's'],
            ['u', 'U', 'v', 'X', '5', 'V', 'x', 'W', 'w']
        ]
    else:
        assert cube.faces == [
                ["Y"] * 9,  # U, 0
                ["O"] * 9,  # L, 1
                ["B"] * 9,  # F, 2
                ["R"] * 9,  # R, 3
                ["G"] * 9,  # B, 4
                ["W"] * 9,  # D, 5
            ]

    return cube


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


def test_letters():
    cube = get_cube()
    all_stickers = []
    for face in cube.faces:
        all_stickers += face
    assert len(all_stickers) == len(set(all_stickers))

    cube = get_cube(bld=False)
    all_stickers = []
    for face in cube.faces:
        all_stickers += face
    for letter in 'YOBRGW':
        assert all_stickers.count(letter) == 9


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
    cube = get_cube()

    cube.X_cube_rotation()

    assert cube.faces == [
        ['b', 'B', 'c', 'A', '0', 'C', 'a', 'D', 'd'],
        # ['a', 'A', 'b', 'D', '0', 'B', 'd', 'C', 'c'],
        ['q', 'Q', 'r', 'T', '4', 'R', 't', 'S', 's'],
        ['e', 'E', 'f', 'H', '1', 'F', 'h', 'G', 'g'],
        ['i', 'I', 'j', 'L', '2', 'J', 'l', 'K', 'k'],
        ['m', 'M', 'n', 'P', '3', 'N', 'p', 'O', 'o'],
        # ['u', 'U', 'v', 'X', '5', 'V', 'x', 'W', 'w']
        ['x', 'X', 'u', 'W', '5', 'U', 'w', 'V', 'v']
    ]


def test_Y_cube_rotation():
    cube = get_cube()

    cube.Y_cube_rotation()

    assert cube.faces == [
        to_list('sStR4TrQq'),
        to_list('hHeG1EgFf'),
        to_list('aAbD0BdCc'),
        to_list('nNoM3OmPp'),
        to_list('wWxV5XvUu'),
        to_list('iIjL2JlKk')
    ]


def test_Z_cube_rotation():
    cube = get_cube()

    cube.Z_cube_rotation()

    assert cube.faces == [
        to_list('hHeG1EgFf'),
        to_list('xXuW5UwVv'),
        to_list('lLiK2IkJj'),
        to_list('dDaC0AcBb'),
        to_list('rRsQ4SqTt'),
        to_list('pPmO3MoNn')
    ]


def test_U_slice_rotation():
    cube = get_cube()

    cube.U_slice_rotation()

    assert cube.faces == [
        # ['a', 'A', 'b', 'D', '1', 'B', 'd', 'C', 'c'],
        ['d', 'D', 'a', 'C', '0', 'A', 'c', 'B', 'b'],
        ['i', 'I', 'j', 'H', '1', 'F', 'h', 'G', 'g'],
        ['m', 'M', 'n', 'L', '2', 'J', 'l', 'K', 'k'],
        ['q', 'Q', 'r', 'P', '3', 'N', 'p', 'O', 'o'],
        ['e', 'E', 'f', 'T', '4', 'R', 't', 'S', 's'],
        ['u', 'U', 'v', 'X', '5', 'V', 'x', 'W', 'w']
    ]


def test_E_slice_rotation():
    cube = get_cube()

    cube.E_slice_rotation()

    assert cube.faces == [
        ['a', 'A', 'b', 'D', '0', 'B', 'd', 'C', 'c'],
        ['e', 'E', 'f', 'T', '4', 'R', 'h', 'G', 'g'],
        ['i', 'I', 'j', 'H', '1', 'F', 'l', 'K', 'k'],
        ['m', 'M', 'n', 'L', '2', 'J', 'p', 'O', 'o'],
        ['q', 'Q', 'r', 'P', '3', 'N', 't', 'S', 's'],
        ['u', 'U', 'v', 'X', '5', 'V', 'x', 'W', 'w']
    ]


def test_outer_slice_rotation():
    cube = get_cube()

    # One full round goes back to complete
    assert cube.is_complete()
    for _ in range(4):
        cube.outer_slice_rotation()
    assert cube.is_complete()

    # Single rotation
    cube.outer_slice_rotation(0)
    assert cube.faces == [
        ['a', 'A', 'b', 'D', '0', 'B', 'd', 'C', 'c'],
        ['i', 'I', 'j', 'H', '1', 'F', 'h', 'G', 'g'],
        ['m', 'M', 'n', 'L', '2', 'J', 'l', 'K', 'k'],
        ['q', 'Q', 'r', 'P', '3', 'N', 'p', 'O', 'o'],
        ['e', 'E', 'f', 'T', '4', 'R', 't', 'S', 's'],
        ['u', 'U', 'v', 'X', '5', 'V', 'x', 'W', 'w']
    ]


def test_face_rotation():
    cube = get_cube()

    # One full round goes back to complete
    assert cube.is_complete()
    for _ in range(4):
        cube.faces[0] = cube.face_rotation(cube.faces[0])
    assert cube.is_complete()

    # Single rotation
    cube.faces[0] = cube.face_rotation(cube.faces[0])
    assert cube.faces == [
        # ['a', 'A', 'b', 'D', '0', 'B', 'd', 'C', 'c'],
        to_list('dDaC0AcBb'),
        ['e', 'E', 'f', 'H', '1', 'F', 'h', 'G', 'g'],
        ['i', 'I', 'j', 'L', '2', 'J', 'l', 'K', 'k'],
        ['m', 'M', 'n', 'P', '3', 'N', 'p', 'O', 'o'],
        ['q', 'Q', 'r', 'T', '4', 'R', 't', 'S', 's'],
        ['u', 'U', 'v', 'X', '5', 'V', 'x', 'W', 'w']
    ]


def test_face_flip():
    cube = get_cube()

    # One full round goes back to complete
    assert cube.is_complete()
    for _ in range(2):
        cube.faces[0] = cube.face_flip(cube.faces[0])
    assert cube.is_complete()

    # Single rotation
    cube.faces[0] = cube.face_flip(cube.faces[0])
    assert cube.faces == [
        # ['a', 'A', 'b', 'D', '0', 'B', 'd', 'C', 'c'],
        to_list('cCdB0DbAa'),
        ['e', 'E', 'f', 'H', '1', 'F', 'h', 'G', 'g'],
        ['i', 'I', 'j', 'L', '2', 'J', 'l', 'K', 'k'],
        ['m', 'M', 'n', 'P', '3', 'N', 'p', 'O', 'o'],
        ['q', 'Q', 'r', 'T', '4', 'R', 't', 'S', 's'],
        ['u', 'U', 'v', 'X', '5', 'V', 'x', 'W', 'w']
    ]
