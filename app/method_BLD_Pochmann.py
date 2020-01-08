from .move_interpreter import Interpreter


algs = {
    'T_perm'    : "R U R' U' R' F R2 U' R' U' R U R' F'",
    'Y_perm'    : "F R U' R' U' R U R' F' (R U R' U') (R' F R F')"
}


def parse_alg(alg:str)
    "Replaces ' with _, and removes spaces."
    alg.replace("'", "_", 100)
    alg.replace(' ', '', 100)
    return alg


class Pochmann:
    setup = {
        'a' : '...',
        'b' : '...',
        'c' : '...',
        'd' : '',
        'e' : 'LE_L'
    }
    

    def get_moves(cube:Cube):
        """Get the moves needed to solve the cube."""
        pass


    def chose_alg(self, letter):
        """Chose alg. Atm, only T- or Y-perm is used, and edge setup
        is somewhat complicated. Can (and maybe should) be updated
        with J-perms, and a more proper/normal setup."""
        if letter.is_upper():
            return algs['Y_perm']
        else:
            return 'T_perm'


    def reverse(self, alg):
        """Reverse the algorithm."""
        letters = []
        for char in alg:
            letters += char
        for i in range(len(letters) - 1):
            if letters[i+1] in ["'", "_", "2"]:
                letters[i] += letters[i+1]
                del letters[i+1]
        return ''.join(letters)
