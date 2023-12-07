from datetime import date, datetime, timezone
from typing import List


class Person:
    """
    >>> person = Person("Ivan", "Ivanov", "male", date(1999, 8, 12))
    >>> person
    Person('Ivan', 'Ivanov', 'male', datetime.date(1999, 8, 12))

    >>> Person("Ivan", "Ivanov", "male", datetime.now(tz=timezone.utc).date()).full_ages()
    0
    >>> Person("Ivan", "Ivanov", "man", "1989.4.26")
    Traceback (most recent call last):
        ...
    ValueError: b_day must be date type
    """

    name: str
    surname: str
    sex: str
    b_day: date

    def __init__(self, name: str, surname: str, sex: str, b_day: date):
        self.name = name
        self.surname = surname
        self.sex = sex

        if isinstance(b_day, date):
            self.b_day = b_day
        else:
            raise ValueError("b_day must be date type")

    def __repr__(self) -> str:
        return f"Person({self.name!r}, {self.surname!r}, {self.sex!r}, {self.b_day!r})"

    def __eq__(self, other: "Person") -> bool:
        return self.__repr__() == other.__repr__()

    def full_ages(self):
        return date.today().year - self.b_day.year


class Student(Person):
    """
    >>> student = Student('Ivan', 'Ivanov', 'male', date(1999, 8, 12), 161, 9)
    >>> student
    Student('Ivan', 'Ivanov', 'male', datetime.date(1999, 8, 12), 161, 9)
    """

    name: str
    surname: str
    sex: str
    b_day: date
    group: int
    skill: int

    def __init__(self, name: str, surname: str, sex: str, b_day: date, group: int, skill: int):
        super().__init__(name, surname, sex, b_day)

        self.group = group
        self.skill = skill

    def __repr__(self) -> str:
        return f"Student({self.name!r}, {self.surname!r}, {self.sex!r}," \
               f" {self.b_day!r}, {self.group!r}, {self.skill!r})"

    def __eq__(self, other: "Student") -> bool:
        return self.__repr__() == other.__repr__()


class Group:
    """
    Encapsulates list of students
    """

    group: List[Student]

    def __init__(self, group: List[Student]):
        self.group = list(group)

    def __eq__(self, other: "Group") -> bool:
        if len(self.group) != len(other.group):
            return False

        for ind in range(len(self.group)):
            if str(self.group[ind]) != str(other.group[ind]):
                return False
        else:
            return True

    def __repr__(self) -> str:
        return f"Group([{', '.join([repr(group) for group in self.group])}])"

    def sort_by_age(self, *, reverse: bool = False):
        self.group = sorted(
            self.group,
            key=lambda student: student.full_ages(),
            reverse=reverse,
        )

    def sort_by_skill(self, *, reverse=False):
        self.group = sorted(
            self.group,
            key=lambda student: student.skill,
            reverse=reverse,
        )

    def sort_by_age_and_skill(self, *, reverse=False):
        self.sort_by_skill(reverse=reverse)
        self.sort_by_age(reverse=reverse)


if __name__ == "__main__":  # Start
    import doctest
    doctest.testmod()
