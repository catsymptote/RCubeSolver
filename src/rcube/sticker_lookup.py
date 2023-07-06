class StickerLookup:
    def __init__(self):
        self.lookup_table = {
            'Y': {"list_index": 0, "color_code": "Y", "stickers": "aAbD0BdCc"},
            'O': {"list_index": 1, "color_code": "O", "stickers": "eEfH1FhGg"},
            'B': {"list_index": 2, "color_code": "B", "stickers": "iIjL2JlKk"},
            'R': {"list_index": 3, "color_code": "R", "stickers": "mMnP3NpOo"},
            'G': {"list_index": 4, "color_code": "G", "stickers": "qQrT4RtSs"},
            'W': {"list_index": 5, "color_code": "W", "stickers": "uUvX5VxWw"}
        }

    def get_color_index(self, sticker):
        for col, items in self.lookup_table.items():
            if sticker in items["stickers"]:  # type: ignore
                return col
        raise KeyError(f"Invalid sticker: {sticker}")

    def get_list_idx(self, sticker: str) -> int:
        for _, items in self.lookup_table.items():
            if sticker in items["stickers"]:  # type: ignore
                return items["list_index"]  # type: ignore
        raise KeyError(f"Invalid sticker: {sticker}")

    def get_xy(self, sticker: str) -> tuple[int, int]:
        for _, items in self.lookup_table.items():
            if sticker in items["stickers"]:  # type: ignore
                x_index = items["list_index"]
                y_index = items["stickers"].index(sticker)  # type: ignore
                return (x_index, y_index)  # type: ignore
        raise KeyError(f"Invalid sticker: {sticker}")

    def __getitem__(self, sticker: str):
        return self.get_xy(sticker)
