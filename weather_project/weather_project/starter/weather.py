import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    pass


def convert_f_to_c(temp_in_farenheit):
    """Converts a temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
   
    temp_in_farenheit = float(temp_in_farenheit)
    convert_f_to_c = (temp_in_farenheit - 32) *5/9
    convert_f_to_c = round(convert_f_to_c, 1)
    return convert_f_to_c



def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
     
    sum = 0
    for temp in weather_data:
        sum = sum + float(temp)

    avg = sum / len(weather_data)
    return avg



def load_data_from_csv(csv_file):
    # """Reads a csv file and stores the data in a list.

    # Args:
    #     csv_file: a string representing the file path to a csv file.
    # Returns:
    #     A list of lists, where each sublist is a (non-empty) line in the csv file.
    # """
    
    weather_list = []
    with open(csv_file)as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ",")
        for index, row in enumerate(csv_reader):
            if index !=0 and len(row) != 0:  #iow if there's content in the row 
                weather_list.append([row[0], int(row [1]), int(row[2])])
    return weather_list

    
    # weather_list = []
    # with open(csv_file, newline='')as csv_file:
    #     csv_reader = csv.reader(csv_file, delimiter = ",")
    #     for line in (csv_reader):      
    #         weather_list.append(line)
    #         weather_list.pop(0)
    #         return weather_list

    # weather_list = []
    # with open("tests/data/example_one.csv") as csv_file:
    #     csv_reader = csv.reader(csv_file, delimiter = ",")
    #     next(csv_reader)
    #     rows = csv.reader(csv_file)
    #     for row in rows:
    #         weather_list.append(row)
    # print(weather_list)

    

def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    if len(weather_data)== 0:
        return ()
    min_value = float(weather_data[0]) #setting first value as the min so we can compare against it
    index = 0
    for index, element in enumerate(weather_data):  #creating an index for each element
        if float(element) <= min_value:
            min_value = float(element)
            min_position = index
    return min_value, min_position
  

def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    if len(weather_data)== 0:
        return ()
    max_value = float(weather_data[0])
    index = 0
    for index, element in enumerate(weather_data):  #creating an index for each element
        if float(element) >= max_value:
            max_value = float(element)
            max_position = index
    return max_value, max_position


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass
