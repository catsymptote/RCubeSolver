class Block:
    letter_code = {"YOG": "A", "YGR": "B", "YRB": "C", "YBO": "D"}

    def __init__(self, stickers: list[str]):
        self.stickers = stickers

        self.block_type = None

        if len(stickers) == 3:
            self.block_type = "corner"
        elif len(stickers) == 2:
            self.block_type = "edge"
        else:
            self.block_type = "center"

    def construct(self, type, stickers):
        self.type = type
        self.stickers = stickers[:]

    def get_type(self):
        return self.type

    def get_stickers(self):
        return self.stickers

    def get_name(self):
        name = ""
        for sticker in self.stickers:
            name += sticker
        return name

    def get_letter(self):
        return Block.letter_code[self.get_letter()]
