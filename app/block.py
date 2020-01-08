class Block:
    def __init__(self, stickers):
        self.stickers = stickers
        
        self.block_type = None
        if len(stickers) == 3:
            self.block_type = 'corner'
        elif len(stickers) == 2:
            self.block_type = 'edge'
        else:
            self.block_type == 'center'
    

    def construct(self, type, stickers):
        self.type = type
        self.stickers = stickers[:]


    def get_type(self):
        return self.type


    def get_stickers(self):
        return self.stickers


    def get_name(self):
        name = ''
        for sticker in stickers:
            name += sticker
