import re
from datetime import datetime, timedelta

from user import User


class Event:
    def __init__(self, title, start_date, duration, localization, owner):
        self.title = title
        self.start_date = start_date
        self.duration = duration
        self.localization = localization
        self.owner = owner

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, new_date):
        if new_date < datetime.now() + timedelta(minutes=float(10)):
            raise ValueError(f"You can enter a past date longer then 10 minutes for now: {new_date}")
        self._start_date = new_date

    @property
    def duration(self):
        return f'{self._duration} minutes'

    @duration.setter
    def duration(self, value):
        if value < 10:
            raise ValueError(f"Event has to last more than 10 minutes: {value}")
        self._duration = value

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, new_owner):
        if not isinstance(new_owner, User):
            raise TypeError(f"Incorrect user type: {new_owner}")
        self._owner = new_owner

    def __str__(self):
        return f'{type(self).__name__}: title: {self.title}, start_date: {self.start_date},' \
               f' duration: {self.duration}, localization: {self.localization}, owner: {self.owner}'

    def __repr__(self):
        return f'{type(self).__name__}(title="{self.title}", start_date={self.start_date}, duration={self.duration},' \
               f' localization="{self.localization}", owner="{self.owner}")'

# e = Event(title='browarek', start_date=datetime(2021, 7, 27), duration=50, localization='krakow', owner='Damian')
# e = Event(title='browarek', start_date=datetime(2021, 7, 27), duration=12, localization='krakow', owner='Damian')
# e.start_date = datetime(2022, 8, 27)
# e.duration = 12
# print(e.duration)
# print(e)
# print(repr(e))