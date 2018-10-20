import cube

#cbe = cube.Cube()
#cbe.U_slice_rotation()
#cbe.Z()
#cbe.U_slice_rotation()
#cbe.show()

class Interpreter:
    cbe = cube.Cube()
    cbe.show()
    # ["R", "R2", "X_", "B"]

    def add_moves(self, moves):
        for move in moves:
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

        for i in range(counter):
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
            elif move == "D":
                self.translate_move("X2")
                self.translate_move("U")
                self.translate_move("X2")
            elif move == "R":
                self.translate_move("Z_")
                self.translate_move("U")
                self.translate_move("Z")
            elif move == "L":
                self.translate_move("Z")
                self.translate_move("U")
                self.translate_move("Z_")
            elif move == "F":
                self.translate_move("X")
                self.translate_move("U")
                self.translate_move("X_")
            elif move == "B":
                self.translate_move("X_")
                self.translate_move("U")
                self.translate_move("X")

            # Mid-slices
            elif move == "M":
                self.translate_move("Z_")
                self.cbe.E_slice_rotation()
                self.translate_move("Z")
            elif move == "E":
                self.cbe.E_slice_rotation()
            elif move == "S":
                self.translate_move("X")
                self.cbe.E_slice_rotation()
                self.translate_move("X_")

            # Double slices
            elif move == "u":
                self.translate_move("U")
                self.translate_move("E_")
            elif move == "d":
                self.translate_move("U")
            elif move == "r":
                self.translate_move("R")
                self.translate_move("M_")
            elif move == "l":
                self.translate_move("L")
                self.translate_move("M")
            elif move == "f":
                self.translate_move("F")
                self.translate_move("S")
            elif move == "b":
                self.translate_move("B")
                self.translate_move("S_")

intp = Interpreter()

intp.add_moves(["R", "U", "R_", "U_"])
intp.cbe.show()