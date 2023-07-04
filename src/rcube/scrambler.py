from rcube.cube_interface import CubeInterface
from rcube.move_lookup import MoveLookup


class Scrambler:
    def __init__(self, cube: CubeInterface | None = None):
        if cube is None or type(cube) is not CubeInterface:
            cube = CubeInterface()
        self.cube = cube
        self.move_lookup = MoveLookup()

    def scramble(self, number=20) -> CubeInterface:
        moves = [self.move_lookup.get_random_move() for _ in range(number)]
        self.cube.apply_moves(moves)
        return self.cube
