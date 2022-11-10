# Hash Table

# Dictionaries

# my_dict = {"Dave": "001", "Ava": "002", "Joe": "003"}
# print(my_dict)
# type(my_dict)

my_dict = dict(Dave="001", Ava="002", Joe="003")
# print(my_dict)
# type(my_dict)

# Nested Dictionaries are basically dictionaries that lie within other dictionaries.
# emp_details = {
#     "Employee" : {
#         "Dave": {
#             "ID":" 001",
#             "Salary": "2000",
#             "Designation": "Team Lead",
#             },
#         "Ava": {
#             "ID": "002",
#             "Salary": "2000",
#             "Designation": "Associate",
#         },
#     }
# }
# print(emp_details)

# Performing Operations On Hash Table

# Accessing Value
print(my_dict["Dave"])
print(my_dict.keys())
print(my_dict.values())