# Given the list of foods below, output:
# 1. The first item in the list.
# 2. The third item in the list.
# 3. The last item in the list.
# 4. The first three items in the list.
# 5. The last three items in the list.
# 6. The last item in the sublist.


foods = [
    "orange",
    "apple",
    "banana",
    "strawberry",
    "grape",
    "blueberry",
    ["carrot", "cauliflower", "pumpkin"],
    "passionfruit",
    "mango",
    "kiwifruit"
]

print(f"The first item in the list is {foods[0]}")    #orange
print(f"The third item in the list is {foods[2]}")    #banana
print(f"The last item in the list is {foods[-1]}")    #kiwifruit
print(f"The first three items in the list are {foods[0:3]}")  #orange apple banana
print(f"The last three items in the list are {foods[7:10]}")  #passionfruit, mango, kiwi
print(f"The last item in the sublist is {foods[6][2]}")       #pumpkin

print(f"The list has {len(foods)} items in it")  #gets number of items 10