from colorama import init as colorama_init
from colorama import Back, Fore, Style


class CubePrinter:
    def __init__(self, cube, background=False):
        # Initialze colorama
        colorama_init()

        # Decide whether to color background or foreground
        ground = Back if background else Fore

        self.color_lookup = {
            'Y': ground.YELLOW,
            'O': ground.MAGENTA,  # Change later
            'B': ground.BLUE,
            'R': ground.RED,
            'G': ground.GREEN,
            'W': ground.WHITE
        }
        self.cube = cube

    def print_sticker(self, sticker, addon: str = ''):
        color = self.color_lookup[sticker]
        print(f'{color}{sticker}{Style.RESET_ALL}', end=addon)

    def show(self):
        for i in range(len(self.cube.faces[0])):
            if (i) % 3 == 0:
                for j in range(2):
                    print(end="\t")
            sticker = self.cube.faces[0][i]
            self.print_sticker(sticker)
            if (i + 1) % 3 == 0:
                print()
        print()

        for k in range(3):
            for i in range(4):
                for j in range(3):
                    sticker = self.cube.faces[i + 1][j + k * 3]
                    self.print_sticker(sticker)
                print(end="\t")
            print()
        print()

        for i in range(len(self.cube.faces[0])):
            if (i) % 3 == 0:
                for j in range(2):
                    print(end="\t")
            sticker = self.cube.faces[5][i]
            self.print_sticker(sticker)
            if (i + 1) % 3 == 0:
                print()
        print()
        print()
