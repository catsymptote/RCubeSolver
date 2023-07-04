from rcube.sticker_lookup import StickerLookup


def test_init():
    sl = StickerLookup()
    assert type(sl) is StickerLookup


def test_get_item():
    sl = StickerLookup()
    assert sl['a'] == (0, 0)
    assert sl['3'] == (2, 4)
    assert sl['Q'] == (4, 1)
    assert sl['x'] == (5, 6)
