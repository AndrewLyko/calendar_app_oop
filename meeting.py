from datetime import datetime

from event import Event
from user import User


class Meeting(Event):

    def __init__(self, title, start_date, duration, localization, owner, members):
        super().__init__(title, start_date, duration, localization, owner)
        self.members = members

    @property
    def members(self):
        return self._members

    @members.setter
    def members(self, new_members):
        for new_member in new_members:
            if not isinstance(new_member, User):
                raise TypeError(f'Incorrect member type: {new_members}')
        self._members = new_members


# members1 = ('Janek', 'Aneta', 'Janina')
# owner1 = User("Andrzej", "L", "andrzej45@a.pl")
# m = Meeting(title='browarek', start_date=datetime(2021, 10, 5), duration=50, localization='krakow', owner=owner1,
#             members=members1)
# print(owner1)
# print(members1)
# print(repr(m))