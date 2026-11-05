   # Worksheet 1.5: Person class
from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """
    def __init__(self, name, birth):
        
        if type(name) is not str:
            raise TypeError
        if name == "":
            raise ValueError
        if type(birth) is not date:
            raise TypeError

        self.name = name
        self.birth = birth

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)
    def initials(self):
        """
        Return uppercase initial letters of each part of the name joined together.
        """
        parts = self.name.split()
        return "".join(p[0].upper() for p in parts)

    def is_birthday(self):
        """
        Return True if today is this person's birthday, False otherwise.
        """
        today = date.today()
        return self.birth.month == today.month and self.birth.day == today.day