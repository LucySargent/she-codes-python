############# LOOPS: Exercises extension

groceries = [
    ["Baby Spinach", 2.78],
    ["Hot Chocolate", 3.70],
    ["Crackers", 2.10],
    ["Bacon", 9.00],
    ["Carrots", 0.56],
    ["Oranges", 3.08]
]
expenditure = [] 
for element in groceries: 
    value = int(input("How many units of " + element[0] + " did you buy? "))* element[1] 
    expenditure.append([element[0], value]) 
 
print("====Izzy's Food Emporium====")
total = 0
newlist = []
for newlist in expenditure: 
    print(str(newlist[0]) + str(newlist[1]))
    total = total + newlist[1]   
    print("============================")
    print(total)



# print(f"{item[0]:<20} $  {item[1]:.2f}")
# print(f"{'$':>22} {total:.2f}")