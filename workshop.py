from event import Event


class Workshop(Event):
    def __init__(self, title, start_date, duration, localization, owner, members, trainer):
        super().__init__(title, start_date, duration, localization, owner, members)
        self.trainer = trainer
