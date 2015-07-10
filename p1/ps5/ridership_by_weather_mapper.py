import sys
import string
import logging

# from util import mapper_logfile
# logging.basicConfig(filename=mapper_logfile, format='%(message)s',
#                     level=logging.INFO, filemode='w')

# RUN:
# > cat ../ps4/turnstile_data_master_with_weather.csv | python ridership_by_weather_mapper.py | sort | python ridership_by_weather_reducer.py
# fog-norain	1315.57980681
# fog-rain	1115.13151799
# nofog-norain	1078.54679697
# nofog-rain	1098.95330076


def mapper():
    '''
    For this exercise, compute the average value of the ENTRIESn_hourly column 
    for different weather types. Weather type will be defined based on the 
    combination of the columns fog and rain (which are boolean values).
    For example, one output of our reducer would be the average hourly entries 
    across all hours when it was raining but not foggy.

    Each line of input will be a row from our final Subway-MTA dataset in csv format.
    You can check out the input csv file and its structure below:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv
    
    Note that this is a comma-separated file.

    This mapper should PRINT (not return) the weather type as the key (use the 
    given helper function to format the weather type correctly) and the number in 
    the ENTRIESn_hourly column as the value. They should be separated by a tab.
    For example: 'fog-norain\t12345'
    
    Since you are printing the output of your program, printing a debug 
    statement will interfere with the operation of the grader. Instead, 
    use the logging module, which we've configured to log to a file printed 
    when you click "Test Run". For example:
    logging.info("My debugging message")
    Note that, unlike print, logging.info will take only a single argument.
    So logging.info("my message") will work, but logging.info("my","message") will not.
    '''

    # Takes in variables indicating whether it is foggy and/or rainy and
    # returns a formatted key that you should output.  The variables passed in
    # can be booleans, ints (0 for false and 1 for true) or floats (0.0 for
    # false and 1.0 for true), but the strings '0.0' and '1.0' will not work,
    # so make sure you convert these values to an appropriate type before
    # calling the function.
    def format_key(fog, rain):
        return '{}fog-{}rain'.format(
            '' if fog else 'no',
            '' if rain else 'no'
        )

    header = False
    for line in sys.stdin:
        # your code here
        if not header:
            header = True
            continue

        data = line.split(',')
        # Find out the data indices:
        # cat ../ps4/turnstile_data_master_with_weather.csv | head -n 1 | tr , '\n' | cat -n
        fog = data[14] == "1.0"
        rain = data[15] == "1.0"
        entries_hourly = data[6]
        print '{0}\t{1}'.format(format_key(fog, rain), entries_hourly)


mapper()

