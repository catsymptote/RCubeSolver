class StickerLookup:
    def __init__(self):
        self.lookup_table = {
            'Y': {"list_index": 0, "color_code": "Y", "stickers": "aAbD1BdCc"},
            'O': {"list_index": 1, "color_code": "O", "stickers": "eEfH2FhGg"},
            'B': {"list_index": 2, "color_code": "B", "stickers": "iIjL3JlKk"},
            'R': {"list_index": 3, "color_code": "R", "stickers": "mMnP4NpOo"},
            'G': {"list_index": 4, "color_code": "G", "stickers": "qQrT5RtSs"},
            'W': {"list_index": 5, "color_code": "W", "stickers": "uUvX6VxWw"}
        }

    def get_col_idx(self, sticker):
        for col, items in self.lookup_table.items():
            if sticker in items["stickers"]:
                return col
        raise KeyError(f"Invalid sticker: {sticker}")

    def get_list_idx(self, sticker: str) -> str:
        for _, items in self.lookup_table.items():
            if sticker in items["stickers"]:
                return items["list_index"]
        raise KeyError(f"Invalid sticker: {sticker}")

    def get_xy(self, sticker: str) -> tuple[int, int]:
        for _, items in self.lookup_table.items():
            if sticker in items["stickers"]:
                x_index = items["list_index"]
                y_index = items["stickers"].index(sticker)
                return (x_index, y_index)
        raise KeyError(f"Invalid sticker: {sticker}")

    def __getitem__(self, sticker: str):
        return self.get_xy(sticker)
