#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import date


class Person:
    """
    >>> p = Person("Ivan", "Ivanov", "male", date(1989, 4, 26))
    >>> print(p)
    Ivan Ivanov, male, 34 years

    >>> p.full_ages()
    34
    >>> Person("Ivan", "Ivanov", "man", "1989.4.26")
    Traceback (most recent call last):
        ...
    ValueError: bday must be date type
    """

    def __init__(self, name, surname, sex, b_day):
        self.name = name
        self.surname = surname
        self.sex = sex

        if isinstance(b_day, date):
            self.b_day = b_day
        else:
            raise ValueError("_day must be date type")

    def __str__(self):
        return f"{self.name} {self.surname}, " \
               f"{self.sex}, {self.full_ages()} years"

    def full_ages(self):
        return date.today().year - self.b_day.year


class Student(Person):
    """
    >>> s = Student("Ivan", "Ivanov", "male", date(1989, 4, 26), 161, 9)
    >>> print(s)
    Ivan Ivanov, male, 34 years, 161 group, 9 skill
    """
    def __init__(self, name, surname, sex, b_day, group, skill):
        super().__init__(name, surname, sex, b_day)

        self.group = group
        self.skill = skill

    def __str__(self):
        return f"{self.name} {self.surname}, " \
               f"{self.sex}, {self.full_ages()} years, " \
               f"{self.group} group, {self.skill} skill"


class Group:
    """
    Encapsulates list of students
    """
    def __init__(self, students):
        self.students = list(students)

    def __eq__(self, other):
        if len(self.students) != len(other.students):
            return False

        for ind in range(len(self.students)):
            if str(self.students[ind]) != str(other.students[ind]):
                return False
        else:
            return True

    def __str__(self):
        return f"Group({[f'Student({str(student)})' for student in self.students]})"

    def sort_by_age(self, reverse=False):
        self.students = sorted(self.students, key=lambda x: x.full_ages(),
                               reverse=reverse)

    def sort_by_skill(self, reverse=False):
        self.students = sorted(self.students, key=lambda x: x.skill,
                               reverse=reverse)

    def sort_by_age_and_skill(self, reverse=False):
        self.sort_by_skill(reverse)
        self.sort_by_age(reverse)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
