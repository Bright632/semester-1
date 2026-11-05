# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """
    def __init__(self, name, birth):

    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)
        if not isinstance(name, str):
            raise TypeError
        if name == "":
            raise ValueError
        if not isinstance(birth, date):
            raise TypeError

        self.name = name
        self.birth = birth

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)
    def initials(self):
        """Return uppercase initial letters of each part of the name joined together."""
        parts = self.name.split()
        return "".join(p[0].upper() for p in parts)

    def is_birthday(self):
        """Return True if today is this person's birthday, False otherwise."""
        tody = date.today()
        return today.month == self.birth.month and today.day == self.birth.day