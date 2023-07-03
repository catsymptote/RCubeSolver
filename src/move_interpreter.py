from src.cube import Cube
from src.move_translator import MoveTranslator

# cbe = cube.Cube()
# cbe.U_slice_rotation()
# cbe.Z()
# cbe.U_slice_rotation()
# cbe.show()


class Interpreter:
    def __init__(self):
        self.translator = MoveTranslator()

        self.cbe = Cube()
        self.cbe.show()
        # ["R", "R2", "X_", "B"]
        self.modifiers = "_2"
        self.move_chars = "UuRrFfLlBbDdMmEeSsXYZ"

    def add_moves(self, moves):
        for move in moves:
            self.translate_move(move)

    def add_str_moves(self, moves):
        # Translate moves to base moves.
        moves = self.translator.translate(moves)

        index = 0
        # print(len(moves))
        while index < len(moves):
            move = moves[index]
            if index + 1 < len(moves):
                # print("xxx")
                if moves[index + 1] in self.modifiers:
                    move += moves[index + 1]
                    index += 1
            index += 1
            # print(move)
            self.translate_move(move)

    def translate_move(self, move):
        # Modifier (2 or _)
        counter = 1
        if len(move) > 1:
            if move[1] == "2":
                counter = 2
            elif move[1] == "_" or move[1] == "'":
                counter = 3
        move = move[0]

        # Perform move
        for _ in range(counter):
            # Cube rotations
            if move == "X":
                self.cbe.X_cube_rotation()
            elif move == "Y":
                self.cbe.Y_cube_rotation()
            elif move == "Z":
                self.cbe.Z_cube_rotation()

            # Single slices
            elif move == "U":
                self.cbe.U_slice_rotation()
            elif move == "E":
                self.cbe.E_slice_rotation()
