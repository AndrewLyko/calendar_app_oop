

# pp(data_1.values())


# meeting = data_1['meetings'][0]
# pp(meeting)

# owner = User(**meeting['owner'])
# print(owner)

#
# class DataObj:
#     def __init__(self, data):
#         self.data_obj = data
#         self.type = self._parse_data_keys(self.data_obj)
#         self.types_obj_data = self._parse_data_values(self.data_obj)
#         self.type_idx = 0
#         self.element_key_list = self._parse_element_keys()
#         # self.element_key_value = self._parse_element_value()
#
#     @staticmethod
#     def _parse_data_keys(data_obj):
#         type_elements = []
#         for types in data_obj.keys():
#             type_elements.append(types)
#         return type_elements
#
#     @staticmethod
#     def _parse_data_values(data_obj):
#         types_obj_data = []
#         for type_data in data_obj.values():
#             types_obj_data.append(type_data)
#         return types_obj_data
#
#     def _parse_element_keys(self):
#         element_key_list = []
#         idx = 0
#         for element in self.type:
#             element_key_list.append(self.data_obj[element][idx].keys())
#             idx += 1
#         return element_key_list

    # def _parse_element_value(self):
    #     idx = 0
    #     for c_type in self.type:
    #         for element in self.element_key_list:
    #             for key in element:
    #                 temp = []
    #                 temp.add_event(self.data_obj[c_type][idx][key])
    #                 idx += 1
    #                 return temp
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.type_idx >= len(self.type):
#             raise StopIteration("End of elements")
#         result = self.types_obj_data[self.type_idx]
#         self.type_idx += 1
#         return result
#
#
# a = DataObj(data_1)

# pp(a.element_key_value)
# for item in a:
#     pp(item[0])
#
# class TypeObj(DataObj):
#     def __init__(self, data):
#         super().__init__(data)
#
#
#     @staticmethod
#     def _parse_element():
#         se

# class DurationIterator:
#     def __init__(self, events):
#         self.idx = 0
#         self.events = self._sort_by_duration(events)
#
#     @staticmethod
#     def _sort_by_duration(events):
#         s_event = []
#         if events is not None:
#             for event in events:
#                 s_event.append(event)
#             s_event = sorted(s_event, key=lambda x: x.duration, reverse=False)
#             return s_event
#
#     def __iter__(self):
#         return Calendar(self.events)
#
#     def __next__(self):
#         if self.idx >= len(self.events):
#             raise StopIteration('Stop iteration')
#         event = self.events[self.idx]
#         self.idx += 1
#         return event

# aaa = 'aaa aaa'
# print(aaa.split(' '))