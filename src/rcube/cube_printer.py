from colorama import init as colorama_init
from colorama import Back, Fore, Style

from rcube.settings import Settings
from rcube.sticker_lookup import StickerLookup


class CubePrinter:
    colorama_is_uninitialized = False

    def __init__(self, cube, background: bool = False):
        # Initialze colorama
        if CubePrinter.colorama_is_uninitialized:
            CubePrinter.colorama_is_uninitialized = False
            colorama_init()

        # Decide whether to color background or foreground
        ground = Back if background else Fore

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
        self.sticker_lookup = StickerLookup()

    def get_color(self, sticker: str):
        '''Sticker is A-X, a-x. Color index is YOBRGW'''
        color_index = sticker
        if self.BLD_notation:
            color_index = self.sticker_lookup.get_color_index(sticker)

        ANSI_color = self.color_lookup[color_index]
        return ANSI_color

    def print_sticker(self, sticker, addon: str = ''):
        color = self.get_color(sticker)
        print(f'{color}{sticker}{Style.RESET_ALL}', end=addon)

    def show(self):
        print()

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
