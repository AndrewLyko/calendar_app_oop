from user import User


class Members:
    def __init__(self, members_list):
        self.members_list = members_list

    def __str__(self):
        return f'{self.members_list}'


user_1 = User("Andrzej", "L", "a@a.pl")
# print(type(user_1))
user_2 = User("Marcin", "U", "a@a.pl")
# # print(user_2)
user_3 = User("Artur", "L", "a@a.pl")
# # print(user_3)
m = Members([user_1, user_2, user_3])
print(m)
