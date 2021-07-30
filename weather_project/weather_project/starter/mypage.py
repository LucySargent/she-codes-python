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
    
#     weather_list = []
#     with open(csv_file)as csv_file:
#         csv_reader = csv.reader(csv_file, delimiter = ",")
#         #next(csv_reader)
#         for index, row in enumerate(csv_reader):
#             if index != 0 and len(row) != 0:  #iow if there's content in the row 
#                 weather_list.append([row[0], int(row[1]), int(row[2])])
#     return weather_list

    

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




