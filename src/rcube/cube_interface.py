from rcube.cube import Cube
from rcube.move_translator import MoveTranslator
from rcube.move_lookup import MoveLookup
from rcube.sticker_lookup import StickerLookup


class CubeInterface:
    def __init__(self, cube=None):
        self.translator = MoveTranslator()
        self.move_lookup = MoveLookup()
        self.sticker_lookup = StickerLookup()

        if cube is None:
            cube = Cube()
        self.cube = cube

    def apply_base_move(self, base_move):
        '''Only accepts a base move:
            X, Y, Z, U, E
        '''

        # Perform move
        # Cube rotations
        if base_move == "X":
            self.cube.X_cube_rotation()
        elif base_move == "Y":
            self.cube.Y_cube_rotation()
        elif base_move == "Z":
            self.cube.Z_cube_rotation()

        # Single slices
        elif base_move == "U":
            self.cube.U_slice_rotation()
        elif base_move == "E":
            self.cube.E_slice_rotation()

    def apply_moves(self, moves):
        base_moves = self.translator.translate(moves)
        for base_move in base_moves:
            self.apply_base_move(base_move)

    def is_complete(self):
        return self.cube.is_complete()

    def show(self):
        self.cube.show()

    def __getitem__(self, sticker: str) -> str:
        x, y = self.sticker_lookup[sticker]
        found_sticker = self.cube.get_sticker(x, y)
        return found_sticker
