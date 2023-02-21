# Hash Table

import pandas as pd

# Dictionaries

# my_dict = {"Dave": "001", "Ava": "002", "Joe": "003"}
# print(my_dict)
# type(my_dict)

my_dict = dict(Dave="001", Ava="002", Joe="003")
# print(my_dict)
# type(my_dict)

# Nested Dictionaries are basically dictionaries that lie within other dictionaries.
emp_details = {
    "Employee" : {
        "Dave": {
            "ID":" 001",
            "Salary": "2000",
            "Designation": "Team Lead",
            },
        "Ava": {
            "ID": "002",
            "Salary": "2000",
            "Designation": "Associate",
        },
    }
}
# print(emp_details)

# Performing Operations On Hash Table

# Accessing Value

# print(my_dict["Dave"])
# print(my_dict.get("Ava"))
# print(my_dict.keys())
# print(my_dict.values())

# Accessing Values Using the for loop

for x in my_dict:
    print(x)

# Accessing Keys Using the for loop

for x in my_dict.values():
    print(x)

# Accessing Values and Keys Using the for loop

for x,y in my_dict.items():
    print(x,y)

# Updateing 

my_dict["Dave"]= "004"
my_dict["chris"] = "003"
# print(my_dict)

# Deleting

# print(my_dict.pop("Ava"))
# print(my_dict.popitem())
# del my_dict["Dave"]

# print(my_dict)

# CONVERTING DICTIONARY INTO A DATAFRAME 

# DICTIONARY TO DATAFRAME 
df = pd.DataFrame(emp_details["Employee"])
print(df)