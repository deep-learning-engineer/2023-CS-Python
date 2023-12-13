import random

from singleton import Singleton


def assert_singleton(lhs: Singleton, rhs: Singleton):
    assert lhs == rhs
    assert lhs is rhs
    assert id(lhs) == id(rhs)


class TestSingleton:
    @staticmethod
    def test_simple():
        lhs = Singleton()
        rhs = Singleton()

        assert_singleton(lhs, rhs)

    def test_hard(self):
        size = 100
        slist = [Singleton() for _ in range(size)]

        def rint():
            return random.randrange(size)  # noqa: S311

        for lhs_idx, rhs_idx in [(rint(), rint()) for _ in range(size**2)]:
            assert_singleton(slist[lhs_idx], slist[rhs_idx])
