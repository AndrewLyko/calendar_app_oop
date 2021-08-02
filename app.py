import json
from datetime import datetime
from my_calendar import Calendar
from generate_data import GenerateData
from user import User
from meeting import Meeting
from pprint import pprint as pp

from workshop import Workshop

data_1 = GenerateData.load_data()

m_list = Calendar()

a = data_1['meetings']

for meeting in data_1['meetings']:
    owner = User(**meeting['owner'])
    members_list = []
    for member in meeting['members']:
        members_list.append(User(**member))
    start_date = datetime.strptime(meeting['start_date'], '%Y-%m-%d %H:%M:%S.%f')
    m_list.add_event(Meeting(meeting['title'], start_date, int(meeting['duration']), meeting['localization'],
                             owner, members_list))

for workshop in data_1['workshops']:
    owner = User(**workshop['owner'])
    trainer = User(**workshop['trainer'])
    start_date = datetime.strptime(workshop['start_date'], '%Y-%m-%d %H:%M:%S.%f')
    m_list.add_event(Workshop(workshop['title'], start_date, int(workshop['duration']), workshop['localization'],
                              owner, trainer))

pp(str(m_list))
pp(repr(m_list))

for item in m_list:
    print(item)
