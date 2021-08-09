from event import Event


class Calendar:

    def __init__(self, events=None):
        self.events = events
        self.idx = 0
        # self.data = self.sort_by_duration()

    @property
    def events(self):
        return self._events

    @events.setter
    def events(self, new_events):
        if new_events is not None:
            for event in new_events:
                if not isinstance(event, Event):
                    raise TypeError(f'{event} is not valid type')

        self._events = new_events or []
        self.sort_by_date()
        # self.sort_by_duration()

    def add_event(self, event):
        if not isinstance(event, Event):
            raise TypeError(f'{event} is not valid type')
        self.events.append(event)
        self.sort_by_date()
        # self.sort_by_duration()

    def sort_by_date(self):
        self.events.sort(key=lambda x: x.start_date, reverse=False)

    # def sort_by_duration(self):
    #     return self.events.sort(key=lambda x: int(x.duration.split(' ')[0]), reverse=False)

    def __str__(self):
        return f'{type(self).__name__} has {len(self.events)} events.'

    def __repr__(self):
        return f'{type(self).__name__}events={self.events}'

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx >= len(self.events):
            raise StopIteration('Stop iteration')
        event = self.events[self.idx]
        self.idx += 1
        return event

#
# class DurationIterator:
#     def __init__(self, events):
#         self.data = events
#
#     def __iter__(self):
#         return Calendar(self.data)
