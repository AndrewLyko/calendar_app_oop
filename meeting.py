from event import Event


class Meeting(Event):

    def __init__(self, title, start_date, duration, localization, owner, members):
        super().__init__(title, start_date, duration, localization, owner, members)
        self.members = members


# m = Meeting(title="browarek", start_date="2021-05-05", duration=50, localization="Krakow", owner="Andrzej",
#             members=['Damian', 'Ala', 'Ewa'])
#
# print(m)
# print(repr(m))

# Do klasy dziedziczacej trzeba przekazac ta sama sygnature