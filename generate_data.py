import json
import random
from datetime import datetime, timedelta
from pprint import pprint as pp


class GenerateData:
    def __init__(self):
        self.first_name = ['Andrzej', 'Damian', 'Paweł']
        self.last_name = ['D', 'K', 'Z']
        self.email = ['a@a.pl', 'd@d.pl', 'p@p.pl']
        self.title = ['browarek', 'wodeczka', 'conieco']
        self.localization = ['krk', 'wro', 'waw']

    def generate_user_data(self):
        return {
            'first_name': random.choice(self.first_name),
            'last_name': random.choice(self.last_name),
            'email': random.choice(self.email)
        }

    def generate_meeting_data(self):
        return {
            'title': random.choice(self.title),
            'start_date': str(datetime.now() + timedelta(minutes=float(random.randint(1000, 10000)))),
            'localization': random.choice(self.localization),
            'duration': random.randint(15, 10000),
            'owner': self.generate_user_data(),
            'members': [self.generate_user_data() for _ in range(random.randint(1, 5))]
        }

    def generate_workshop_data(self):
        return {
            'title': random.choice(self.title),
            'start_date': str(datetime.now() + timedelta(minutes=float(random.randint(1000, 10000)))),
            'localization': random.choice(self.localization),
            'duration': random.randint(15, 10000),
            'owner': self.generate_user_data(),
            'trainer': self.generate_user_data()
        }

    def generate_data(self, amount):
        with open('data.json', 'w') as file:
            data = {
                'meetings': [],
                'workshops': []
            }
            for _ in range(1, amount + 1):
                data['meetings'].append(self.generate_meeting_data())
                data['workshops'].append(self.generate_workshop_data())

            json.dump(data, file)

    @staticmethod
    def load_data():
        with open("data.json", "r") as file:
            data_obj = json.load(file)
            return data_obj

#
# a = GenerateData()
# pp(a.load_data())
# a.generate_data(30)


#
# data = {
#     'meetings': [
#         {
#             'title': '',
#             'start_date': '',
#             'localization': '',
#             'duration': '',
#             'owner': {
#                 'first_name': "Andrzej",
#                 'last_name': "L",
#                 'email': 'a@a.pl'
#             },
#             'members': [
#                 {
#                     'first_name': "Andrzej",
#                     'last_name': "L",
#                     'email': 'a@a.pl'
#                 }
#             ]
#         }
#     ],
#     'workshops': [
#         {
#             'title': '',
#             'start_date': '',
#             'localization': '',
#             'duration': '',
#             'owner': '',
#             'trainer': ''
#         }
#     ]
# }
