from datetime import datetime

from event import Event
from user import User


class Meeting(Event):

    def __init__(self, title, start_date, duration, localization, owner, members):
        super().__init__(title, start_date, duration, localization, owner)
        self.members = members


owner = User("Andrzej", "L", "a@a.pl")
m = Meeting(title="browarek", start_date=datetime(2021, 10, 5), duration=50, localization="Krakow", owner=owner,
            members=['Damian', 'Ala', 'Ewa'])

print(m)
# print(repr(m))

# Do klasy dziedziczacej trzeba przekazac ta sama sygnature
