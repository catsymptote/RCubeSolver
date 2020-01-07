class Block:
    type = 0    # 0 -> corner, 1 -> edge, 2 -> center
    stickers = []

    #def Block(self, type, stickers):
    #    self.type = type
    #    self.stickers = stickers[:]

    def Block(self):
        pass

    def construct(self, type, stickers):
        self.type = type
        self.stickers = stickers[:]

    def get_type(self):
        return self.type

    def get_stickers(self):
        return self.stickers
