from block import Block

class TestBlock:

    def test_block_creation__sets_starting_iaddr(self):
        start = 10
        end = 20
        b = Block(start, end)
        assert b.start == start

    def test_block_creation__sets_ending_iaddr(self):
        start = 10
        end = 20
        b = Block(start, end)
        assert b.end == end

