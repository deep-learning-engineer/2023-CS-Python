import pytest

from ocean import Ocean


class TestOcean:
    init_state = [[0, 2, 0, 1, 3],
                  [0, 2, 0, 3, 3],
                  [0, 2, 2, 2, 1],
                  [2, 1, 2, 0, 3],
                  [3, 3, 1, 3, 3]]

    next_state = [[0, 0, 0, 1, 3],
                  [2, 2, 0, 3, 3],
                  [2, 0, 0, 2, 1],
                  [0, 1, 2, 2, 3],
                  [0, 0, 1, 3, 3]]

    ocean = Ocean(init_state)

    def test_ocean_init(self):
        assert str(self.ocean) == "\n".join(["".join(str(el) for el in row) for row in self.init_state])

    def test_ocean_repr(self):
        assert self.ocean.__repr__() == f"Ocean({self.init_state!r})"

    def test_ocean_step(self):
        self.ocean.gen_next_quantum()
        assert str(self.ocean) == "\n".join(["".join(str(el) for el in row) for row in self.next_state])
