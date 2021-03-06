from .block import Block


class Cube:
    sticker_code_register = {
        # _ : (f1, s1, f2, s2, f3, s3 ), where f is face and s is sticker.
        # 1->2->3 should be ordered by clockwise rotation around the cube.
        # 1 (in both corners and edges) should always be the relevant sticker.
        'A' : (0, 0, 1, 0, 4, 2),
        'B' : (0, 2, 4, 0, 3, 2),
        'C' : (0, 4, 3, 0, 2, 2),
        'D' : (0, 6, 2, 0, 1, 2),
        'E' : (1, 0, 4, 2, 0, 0),
        'F' : (1, 2, 0, 6, 2, 0),
        'G' : (1, 4, 2, 6, 5, 0)
    }


    def __init__(self):
        self.faces = [
            ["Y"]*9,   # U, 0
            ["O"]*9,   # L, 1
            ["B"]*9,   # F, 2
            ["R"]*9,   # R, 3
            ["G"]*9,   # B, 4
            ["W"]*9    # D, 5
        ]

        # Should do a deepcopy of original self.faces instead of this.
        self.orig_faces = [
            ["Y"]*9,   # U, 0
            ["O"]*9,   # L, 1
            ["B"]*9,   # F, 2
            ["R"]*9,   # R, 3
            ["G"]*9,   # B, 4
            ["W"]*9    # D, 5
        ]


    def list_equality(self, a, b):
        """Check if two lists are equal,in that they have
        the same values, but not necessarily in order."""
        a.sort()
        b.sort()
        if len(a) != len(b) or type(a) != type(b):
            return False
        for i in range(len(a)):
            if a[i] != b[i] or type(a) != type(b):
                return False
        return True


    def get_block(self, sticker):
        """Return the block/piece based on the sticker code.
        The codes are 'A' -> 'X', both upper- and lowercase.
        * Uppercase letters -> corner stickers.
        * Lowercase letters -> edge stickers.
        * Center stickers are not lettered."""
        
        if sticker in Cube.sticker_code_register:
            pos = Cube.sticker_code_register[sticker]
            block_stickers = []
            for i in range(0, len(pos), 2):
                block_stickers.append(self.faces[pos[i]][pos[i+1]])

            blk = Block(block_stickers)
            return blk
        return None
        #if sticker == "A":
            #a = self.faces[0][0]
            #b = self.faces[1][0]
            #c = self.faces[4][2]
            #tmp = [a, b, c]
            #blk.construct(0, [
            #    self.faces[0][0],
            #    self.faces[1][0],
            #    self.faces[4][2]
            #])
        #    block.construct()
        #return blk





    def is_complete(self):
        #for i in range(len(self.faces)):
        #    for j in range(len(self.faces[i])):
        #        if self.faces[i][j] != self.orig_faces[i][j]:
        #            return False
        #return True
        if self.faces == self.orig_faces:
            return True
        return False


    def show(self):
        #print(self.faces)
        # print Y
        # print O-B-R-G x3
        # print w
        # Print Y
        for i in range(len(self.faces[0])):
            if (i)%3==0:
                for j in range(2):
                    print(end="\t")
            print(self.faces[0][i], end=" ")
            if (i+1)%3==0:
                print()
        print()


        for k in range(3):
            for i in range(4):
                for j in range(3):
                    print(self.faces[i+1][j+k*3], end=" ")
                print(end="\t")
            print()
        print()

        for i in range(len(self.faces[0])):
            if (i)%3==0:
                for j in range(2):
                    print(end="\t")
            print(self.faces[5][i], end=" ")
            if (i+1)%3==0:
                print()
        print()
        print()


    def simple_show(self):
        for face in self.faces:
            index = 0
            for sticker in face:
                print(sticker, end="")
                if((index+1)%3==0):
                    print(end=" ")
                print(end=" ")
                index += 1
            print()
        print()


    def altshow(self):
        """ For debug purposes only! Used for self.orig_faces. """
        for face in self.orig_faces:
            index = 0
            for sticker in face:
                print(sticker, end="")
                if((index+1)%3==0):
                    print(end=" ")
                print(end=" ")
                index += 1
            print()
        print()


    """ Cube rotations """
    def X_cube_rotation(self):
        # tmp << Y
        tmp = self.faces[0]

        # Y << B
        self.faces[0] = self.faces[2]

        # B << W
        self.faces[2] = self.faces[5]

        # W << G
        self.faces[5] = self.faces[4]
        self.faces[5] = self.face_flip(self.faces[5])

        # G << Y
        self.faces[4] = tmp
        self.faces[4] = self.face_flip(self.faces[4])

        # O rotate
        self.faces[1] = self.face_rotation(self.faces[1])
        self.faces[1] = self.face_rotation(self.faces[1])
        self.faces[1] = self.face_rotation(self.faces[1])

        # R rotate
        self.faces[3] = self.face_rotation(self.faces[3])


    def Y_cube_rotation(self):
        # tmp << O
        tmp = self.faces[1]

        # O << B
        self.faces[1] = self.faces[2]

        # B << R
        self.faces[2] = self.faces[3]

        # R << G
        self.faces[3] = self.faces[4]

        # G << tmp
        self.faces[4] = tmp

        # Y rotate
        self.faces[0] = self.face_rotation(self.faces[0])

        # W rotate
        self.faces[5] = self.face_rotation(self.faces[5])
        self.faces[5] = self.face_rotation(self.faces[5])
        self.faces[5] = self.face_rotation(self.faces[5])


    def Z_cube_rotation(self):
        # tmp << Y
        tmp = self.faces[0]

        # Y << O
        self.faces[0] = self.faces[1]
        self.faces[0] = self.face_rotation(self.faces[0])

        # O << W
        self.faces[1] = self.faces[5]
        self.faces[1] = self.face_rotation(self.faces[1])

        # W << R
        self.faces[5] = self.faces[3]
        self.faces[5] = self.face_rotation(self.faces[5])

        # R << tmp
        self.faces[3] = tmp
        self.faces[3] = self.face_rotation(self.faces[3])

        # B rotate
        self.faces[2] = self.face_rotation(self.faces[2])

        # G rotate
        self.faces[4] = self.face_rotation(self.faces[4])
        self.faces[4] = self.face_rotation(self.faces[4])
        self.faces[4] = self.face_rotation(self.faces[4])


    def U_slice_rotation(self):
        # Yellow face
        self.faces[0] = self.face_rotation(self.faces[0])

        # Other faces
        self.outer_slice_rotation()


    def E_slice_rotation(self):
        self.outer_slice_rotation(1)
        self.outer_slice_rotation(1)
        self.outer_slice_rotation(1)


    def outer_slice_rotation(self, modifier=0):
        idx0 = 0 + modifier*3
        idx1 = 1 + modifier*3
        idx2 = 2 + modifier*3

        tmp0 = self.faces[1][idx0]
        tmp1 = self.faces[1][idx1]
        tmp2 = self.faces[1][idx2]

        # O << B
        self.faces[1][idx0] = self.faces[2][idx0]
        self.faces[1][idx1] = self.faces[2][idx1]
        self.faces[1][idx2] = self.faces[2][idx2]

        # B << R
        self.faces[2][idx0] = self.faces[3][idx0]
        self.faces[2][idx1] = self.faces[3][idx1]
        self.faces[2][idx2] = self.faces[3][idx2]

        # R << G
        self.faces[3][idx0] = self.faces[4][idx0]
        self.faces[3][idx1] = self.faces[4][idx1]
        self.faces[3][idx2] = self.faces[4][idx2]

        # G << tmp
        self.faces[4][idx0] = tmp0
        self.faces[4][idx1] = tmp1
        self.faces[4][idx2] = tmp2


    def face_rotation(self, face):
        tmpList = face[:]

        face[0] = tmpList[6]
        face[1] = tmpList[3]
        face[2] = tmpList[0]

        face[3] = tmpList[7]
        face[4] = tmpList[4]
        face[5] = tmpList[1]

        face[6] = tmpList[8]
        face[7] = tmpList[5]
        face[8] = tmpList[2]

        return face


    def face_flip(self, face):
        tmpList = face[:]
        for i in range(9):
            face[i] = tmpList[9 -1 -i]
        """
        face[0] = tmpList[8]
        face[1] = tmpList[7]
        face[2] = tmpList[6]

        face[3] = tmpList[5]
        face[4] = tmpList[4]
        face[5] = tmpList[3]

        face[6] = tmpList[2]
        face[7] = tmpList[1]
        face[8] = tmpList[0]
        """
        return face
