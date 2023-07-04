from colorama import init as colorama_init
from colorama import Back, Fore, Style

from rcube.settings import Settings

class CubePrinter:
    def __init__(self, cube, background: bool = False):
        # Initialze colorama
        colorama_init()

        # Decide whether to color background or foreground
        ground = Back if background else Fore

        self.sticker_lookup = {
            'Y': '1abcd',
            'O': '2efgh',  # Change later
            'B': '3ijkl',
            'R': '4mnop',
            'G': '5qrst',
            'W': '6uvwx'
        }

        self.color_lookup = {
            'Y': ground.YELLOW,
            'O': ground.MAGENTA,  # (Orange)
            'B': ground.BLUE,
            'R': ground.RED,
            'G': ground.GREEN,
            'W': ground.WHITE
        }
        self.cube = cube
        self.BLD_notation = Settings.use_BLD_notation

    def get_color(self, sticker: str):
        '''Sticker is A-X, a-x. Color index is YOBRGW'''
        color_index = sticker
        if self.BLD_notation:
            sticker = sticker.lower()
            for k, v in self.sticker_lookup.items():
                if sticker in v:
                    color_index = k

        ANSI_color = self.color_lookup[color_index]
        return ANSI_color        

    def print_sticker(self, sticker, addon: str = ''):
        color = self.get_color(sticker)
        print(f'{color}{sticker}{Style.RESET_ALL}', end=addon)

    def show(self):
        for i in range(len(self.cube.faces[0])):
            if (i) % 3 == 0:
                for j in range(1):
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
                for j in range(1):
                    print(end="\t")
            sticker = self.cube.faces[5][i]
            self.print_sticker(sticker)
            if (i + 1) % 3 == 0:
                print()
        print()
        print()
