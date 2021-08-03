# from datetime import datetime
# weather = [
#             ["2021-07-02T07:00:00+08:00", 49, 67],
#             ["2021-07-03T07:00:00+08:00", 57, 68],
#             ["2021-07-04T07:00:00+08:00", 56, 62],
#             ["2021-07-05T07:00:00+08:00", 55, 61],
#             ["2021-07-06T07:00:00+08:00", 53, 62],
#             ["2021-07-06T07:00:00+08:00", 34, 62]
# ]

# DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

# def convert_date(iso_string):
#     new_date = datetime.strptime(iso_string,"%Y-%m-%dT%H:%M:%S%z")
#     return new_date.strftime("%A %d %B %Y")

# def format_temperature(temp):
#     return f"{temp}{DEGREE_SYBMOL}"

# def find_min(weather):
#     if len(weather)== 0:
#         return ()
#     min_value = float(weather[0]) #setting first value as the min so we can compare against it
#     index = 0
#     for index, element in enumerate(weather):  #creating an index for each element
#         if float(element) <= min_value:
#             min_value = float(element)
#             min_position = index
#     return min_value, min_position

# def convert_f_to_c(temp_in_farenheit):

   
#     temp_in_farenheit = float(temp_in_farenheit)
#     convert_f_to_c = (temp_in_farenheit - 32) *5/9
#     convert_f_to_c = round(convert_f_to_c, 1)
#     return convert_f_to_c


# def calculate_mean(weather_data):
#     sum = 0
#     for temp in weather_data:
#         sum = sum + float(temp)

#     avg = sum / len(weather_data)
#     return avg



# def load_data_from_csv(csv_file):
#     # """Reads a csv file and stores the data in a list.

#     # Args:
#     #     csv_file: a string representing the file path to a csv file.
#     # Returns:
#     #     A list of lists, where each sublist is a (non-empty) line in the csv file.
#     # """

import csv

weather_list = []
with open('csv_file')as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    for index, row in enumerate(csv_reader):
        if index != 0 and len(row) != 0:  #iow if there's content in the row 
            weather_list.append([row[0], int(row[1]), int(row[2])])
print(weather_list)

    

# def find_min(weather_data):
#     if len(weather_data)== 0:
#         return ()
#     min_value = float(weather_data[0]) #setting first value as the min so we can compare against it
#     index = 0
#     for index, element in enumerate(weather_data):  #creating an index for each element
#         if float(element) <= min_value:
#             min_value = float(element)
#             min_position = index
#     return min_value, min_position
  

# def find_max(weather_data):
#     if len(weather_data)== 0:
#         return ()
#     max_value = float(weather_data[0])
#     index = 0
#     for index, element in enumerate(weather_data):  #creating an index for each element
#         if float(element) >= max_value:
#             max_value = float(element)
#             max_position = index
#     return max_value, max_position

# ####summary
# min_new_list = []
# max_new_list = []
# date_list = []
# row_count = 0
# for row in (weather):
#     if len(row) != 0:
#         min_new_list.append(row[1])
#         max_new_list.append(row[2])
#         date_list.append(row[0])
#         row_count += 1
# min,min_position = find_min(min_new_list)
# max,max_position = find_max(max_new_list)
# date_min = date_list[min_position]
# date_max = date_list[max_position]
# print(f"{row_count} Day Overview")
# print(f"  The lowest temperature will be {format_temperature(convert_f_to_c(min))}, and will occur on {convert_date(date_min)}.")
# print(f"  The highest temperature will be {format_temperature(convert_f_to_c(max))}, and will occur on {convert_date(date_max)}.")
# print(f"  The average low this week is {format_temperature(convert_f_to_c(calculate_mean(min_new_list)))}.")
# print(f"  The average high this week is {format_temperature(convert_f_to_c(calculate_mean(max_new_list)))}.")




# L = ['apples', 'bananas', 'oranges']
# for idx, val in enumerate(L):
#   print("index is %d and value is %s" % (idx, val))


# def find_min(weather_data):         
# xy = [49, 57, 56, 55, 53]
# minval = min(xy)
# valpos = xy.index(min(xy))
# if minval:
#     print(minval, valpos)

# weather_data = [49, 57, 56, 55, 53]
# minvalue = min(weather_data)
# index = weather_data.index(minvalue)
# print(f"{minvalue},{index}")


# weather_data.index(min)
# print(min+weather_data.index)
# for idx, val in enumerate(weather_data): 
# print((idx, val))



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

# from datetime import datetime
# iso_string = "2021-07-05T07:00:00+08:00"
# new_date = datetime.strptime(iso_string,"%Y-%m-%dT%H:%M:%S%z")
# print(new_date.strftime("%A %d %B %Y"))

## A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021


# def generate_daily_summary(weather_data):
#     """Outputs a daily summary for the given weather data.

#     Args:
#         weather_data: A list of lists, where each sublist represents a day of weather data.
#     Returns:
#         A string containing the summary information.
#     """
# ["2021-07-02T07:00:00+08:00", 49, 67],  

# ---- Friday 02 July 2021 ----
#   Minimum Temperature: 9.4°C
#   Maximum Temperature: 19.4°

# def load_data_from_csv(csv_file):
    # """Reads a csv file and stores the data in a list.

    # Args:
    #     csv_file: a string representing the file path to a csv file.
    # Returns:
    #     A list of lists, where each sublist is a (non-empty) line in the csv file.
    # # """
    
    # weather_list = []
    # with open(csv_file)as csv_file:
    #     csv_reader = csv.reader(csv_file, delimiter = ",")
    #     for index, row in enumerate(csv_reader):
    #         if index !=0 and len(row) != 0:  #iow if there's content in the row 
    #             weather_list.append([row[0], int(row [1]), int(row[2])])
    # return weather_list

# a = [
#         ["2021-07-02T07:00:00+08:00", 49, 67],
#         ["2021-07-03T07:00:00+08:00", 57, 68],
#         ["2021-07-04T07:00:00+08:00", 56, 62],
#         ["2021-07-05T07:00:00+08:00", 55, 61],
#         ["2021-07-06T07:00:00+08:00", 53, 62]
# ]
# # for list in a:
# #     for x in list:
# #         print([0]

# # print(a[0][0])
# print(a[:0],a[:4])

# header = ("5 Day Overview")
# print(header)

weather_data = [
    ["2021-07-02T07:00:00+08:00", 49, 67],
    ["2021-07-03T07:00:00+08:00", 57, 68],
    ["2021-07-04T07:00:00+08:00", 56, 62],
       ["2021-07-05T07:00:00+08:00", 55, 61],
    ["2021-07-06T07:00:00+08:00", 53, 62]
]
print("hello")

# for x in range(len(weather_data)):
#     min = min(weather_data[0][1])
#     if x > min:
#         min = x
#         print(min)