from app.block import Block


def test_block():
    corner = Block(['Y', 'O', 'G'])
    edge = Block(['Y', 'O'])
    center1 = Block(['Y'])
    center2 = Block(['Y', 'O', 'G', 'R'])

    assert type(corner.stickers) is list
    assert len(corner.stickers) == 3
    assert corner.stickers == ['Y', 'O', 'G']
    assert corner.block_type == 'corner'

    assert type(edge.stickers) is list
    assert len(edge.stickers) == 2
    assert edge.stickers == ['Y', 'O']
    assert edge.block_type == 'edge'

    assert type(center1.stickers) is list
    assert len(center1.stickers) == 1
    assert center1.stickers == ['Y']
    assert center1.block_type == 'center'

    assert type(center2.stickers) is list
    assert len(center2.stickers) == 4
    assert center2.stickers == ['Y', 'O', 'G', 'R']
    assert center2.block_type == 'center'
