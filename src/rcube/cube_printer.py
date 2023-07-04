from termcolor import colored


class CubePrinter:
    def __init__(self, cube):
        self.color_lookup = {
            'Y': 'yellow',
            'O': 'orange',
            'B': 'blue',
            'R': 'red',
            'G': 'green',
            'W': 'white'
        }
        self.cube = cube

    def get_color(self, sticker):
        return self.color_lookup[sticker]

    def show(self):
        for i in range(len(self.cube.faces[0])):
            if (i) % 3 == 0:
                for j in range(2):
                    print(end="\t")
            sticker = self.cube.faces[0][i]
            color = self.get_color(sticker)
            print(colored(sticker), end=" ")
            if (i + 1) % 3 == 0:
                print()
        print()

        for k in range(3):
            for i in range(4):
                for j in range(3):
                    sticker = self.cube.faces[i + 1][j + k * 3]
                    color = self.get_color(sticker)
                    print(colored(sticker), end=" ")
                print(end="\t")
            print()
        print()

        for i in range(len(self.cube.faces[0])):
            if (i) % 3 == 0:
                for j in range(2):
                    print(end="\t")
            sticker = self.cube.faces[5][i]
            color = self.get_color(sticker)
            print(colored(sticker), end=" ")
            if (i + 1) % 3 == 0:
                print()
        print()
        print()
