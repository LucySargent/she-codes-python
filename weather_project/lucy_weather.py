
# # L = ['apples', 'bananas', 'oranges']
# # for idx, val in enumerate(L):
# #   print("index is %d and value is %s" % (idx, val))

# # def find_min(weather_data):
# #     """Calculates the minimum value in a list of numbers.

# #     Args:
# #         weather_data: A list of numbers.
# #     Returns:
# #         The minium value and it's position in the list.
# #     """

# # def find_min(weather_data):         
# # xy = [49, 57, 56, 55, 53]
# # minval = min(xy)
# # valpos = xy.index(min(xy))
# # if minval:
# #     print(minval, valpos)

# weather_data = [49, 57, 56, 55, 53]
# minvalue = min(weather_data)
# index = weather_data.index(minvalue)
# print(f"{minvalue},{index}")


# # weather_data.index(min)
# # print(min+weather_data.index)
# # for idx, val in enumerate(weather_data): 
# # print((idx, val))



# weather_data = [49, -5, - 2, 4, '6', '8', 10.4, 11.7]
# min_value = (min(weather_data))
# position = weather_data.index(min_value)
# print(min_value, position)



# print([float(x) for x in weather_data])
# min_value = min(weather_data)
# position = weather_data.index(min_value)
# print(min_value,position)

# weather_data = [-5, - 2, 4, '6', '8', 10.4, 11.7]
# floats = []
# for element in weather_data:
#     floats.append(float(element))
# print(floats)
# min_value = min(floats)
# position = floats.index(min_value)
# print(min_value,position)


# weather_data = [-5, - 2, 4, '6', '8', 10.4, 11.7]
# min_value = float(weather_data[0]) #setting first value as the min so we can compare against it
# index = 0 #setting up the index so we can re-define it later
# for index, element in enumerate(weather_data):  #creating an index for each element
#     if float(element) <= min_value:
#         min_value = float(element)
#         min_position = index
# print(min_value, min_position)

from datetime import datetime
iso_string = "2021-07-05T07:00:00+08:00"
new_date = datetime.strptime(iso_string,"%Y-%m-%dT%H:%M:%S%z")
print(new_date.strftime("%A" "%d" "%B"
"%Y"))

## A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021