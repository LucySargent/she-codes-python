#dictionaries behave differently to lists
#dictionaries have keys and values
#keys are unique
#elements are key:value pairs
#pairs are seperated with comma
#keys need to be unique, keys can only be immutable
#takes any data type -> string, int, flo, bool, list
#values don't need to be unique

students_dict = {"Angela": 1, "Jen": 2, "Bel": 3}

# print(students_dict.get("Bel")) #get is a function - calling a function here. Get function can take in two parameters

print(students_dict.get("Asli")) #this will give and error because Asli is not in the dictionary
print(students_dict.get("Asli", 0)) #Can use a message e.g. "not in dictionary"
print(students_dict.get("Bel"))

print(students_dict["Angela"]) #using the key of Angela to get the value
students_dict["Asli"] = 4 #adding element to dictionary
print(students_dict)
students_dict["Jen"] = 10 #overwriting the key
print(students_dict)

# del students_dict["Asli"]
# print(students_dict)

print(students_dict.keys())
print(students_dict.values())
print(students_dict.items()) #keys and values together

#iteration - the following are 2 examples are two ways of iterating over the dict
for key in students_dict:
    print(key, students_dict[key])

for key,value in students_dict.items():
    print(key,value)