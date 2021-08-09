l = ['a', 'b', 'c', 'd']
i = iter(l)
print(i)


# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# for item in i:
#     print(item)
def gen():
    yield 'a'
    yield 'b'
    yield 'c'


g = gen()


# print(g)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# for item in gen():
#     print(item)
class MyFancyIterator:
    def __init__(self):
        self.data = ['a', 'b', 'c']
        self.idx = len(self.data) - 1

    # żeby klasa stałą się iteratorem potrzebuje 2 metod:
    def __iter__(self):
        return self

    def __next__(self):
        if self.idx < 0:
            raise StopIteration("Iteration end")
        b = self.data[self.idx]
        self.idx -= 1
        return b


# for item in MyFancyIterator():
#     print(item)
# m = MyFancyIterator()
# n = iter(m)
# print(m == n)
# print(m is n)
#
# print(next(n))
# print(next(n))
# print(next(n))
# try:
#     print(next(n))
# except StopIteration:
#     print("end of iterables")
# finally:
#     print("bede z toba na dobre i zle")
data = {
    "africa": {
        "egypt": "cairo",
        "libya": "tripoli"
    },
    "europe": {
        "poland": "warsaw",
        "island": "reykjavik"
    }
}


class MyBetterIterator:
    def __init__(self, input_data):
        self.data = self._parse_data(input_data)
        self.idx = 0

    @staticmethod
    def _parse_data(input_data):
        temp = []
        for countries in input_data.values():
            for capital in countries.values():
                temp.append(capital)
        return sorted(temp)

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx >= len(self.data):
            raise StopIteration("end of elements")
        result = self.data[self.idx]
        self.idx += 1
        return result


class MyBetterIteratorEx:
    def __init__(self, input_data):
        self.data = self._parse_data(input_data)
        self.idx = 0

    @staticmethod
    def _parse_data(input_data):
        temp = []
        for countries in input_data.values():
            for capital in countries.values():
                temp.append(capital)
        return sorted(temp, reverse=True)

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx >= len(self.data):
            raise StopIteration("end of elements")
        result = self.data[self.idx]
        self.idx += 1
        return result


class MyIterable:
    def __init__(self, input_data):
        self.data = input_data

    def __iter__(self):
        return MyBetterIterator(self.data)


#
# x = MyIterable(data)
# # # # x.__iter__ = lambda self: MyBetterIteratorEx(self.data)
# for item in x:
#     print(item)
# m = MyIterable(data)
# n = iter(MyIterable(data))
#
# print(next(n))
# print(next(n))
# print(next(n))
# print(next(n))
