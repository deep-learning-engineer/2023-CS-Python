from typing import Optional


class Singleton:
    single: Optional["Singleton"] = None

    def __new__(cls, *args, **kwargs):  # noqa: ARG003
        if not cls.single:
            cls.single = super().__new__(cls)

        return cls.single
