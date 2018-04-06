
import time
import pandas as pd
import numpy as np
import datetime as dt

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    '''runs the program to get user input'''
    # getting user input
    print('Hello! Let\'s explore some US bikeshare data!')
    while True:
        raw_city = input("Enter city (chicago, new york city, washington): ")
        '''city as string in input, not case sensitive'''
        city = raw_city.lower()
        month = input("Enter month as an integer (0=all,1=January,etc.): ")
        '''inputs month as integer, but technically a string until next function'''
        day = input("Enter day as integer(0=all, 1=monday, etc.): ")
        '''inputs day as integer, but technically a string until next function'''
    # all should return strings, some are cities, some are numbers
        if city not in CITY_DATA:
            print("error in city")
            continue
        elif int(month) < 0 or int(month) > 12:
            print("error in month")
            continue
        elif int(day) < 0 or int(day) > 7:
            print("error in day")
            continue
        break
    return city, month, day
    '''returns the users input for city, month and day as strings'''


def load_data(city, month, day):
    '''accepts city, month, day as integers, from previous function'''
    # conditionals to account for wrong user input
    # empty data frames for conditionals in functions

    raw_csv = CITY_DATA[city]  # gets the city that was inputted
    raw_df = pd.read_csv(raw_csv)  # turns csv into datafram
    # converts the 'Start Time into date time
    raw_df['Start Time'] = pd.to_datetime(raw_df['Start Time'])
    raw_df['month'] = raw_df['Start Time'].dt.month  # creates month column

    # creates day column as day of the week
    raw_df['day'] = raw_df['Start Time'].dt.weekday
    raw_df['hour'] = raw_df['Start Time'].dt.hour  # creates hour column
    month_int = int(month)  # converts input into integer
    day_int = int(day)
    if month_int == 0:
        month_sorted_df = raw_df  # wrong input conditional
    elif month_int > 12:  # wrong input conditional
        print("Not a valid month")
        df = pd.DataFrame()
    else:
        # checks if input month corresponds to data in column
        month_df = raw_df['month'] == month_int
        # filters them based on above criteria
        month_sorted_df = raw_df[month_df]
    if day_int == 0:  # similar structure for the day
        df = raw_df
    elif day_int > 7:
        print("Not a valid day")
        df = pd.DataFrame()
    else:

        day_df = month_sorted_df['day'] == day_int
        df = month_sorted_df[day_df]

    return df
    '''returns a pandas dataframe with the specific city csv data and filtered by month and day specified by user in get_filters function'''


def time_stats(df):
    '''accepts filtered and city specified dataframe'''
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    if df.empty:  # conditional to show error if input is wrong
        print("Something went wrong")

    else:
        print("Most popular month as an integer (1=January, 2= February, etc.):")
        # counts all values for and shows key of most common
        print(df['month'].value_counts().idxmax())
        print("Most popular day as an integer (1=Mon, 2= Tues, etc.):")
        print(df['day'].value_counts().idxmax())
        print("Most popular hour as an integer in 24 hour clock (1=1am, 13=1pm, etc.):")
        print(df['hour'].value_counts().idxmax())
    '''prints Most popular month, Most popular day, and Most popular hour on the terminal console, also prints the time it took to run the function, also prints error if there is an empty dataframe'''
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):

'''accepts filtered and city specified dataframe'''
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    if df.empty:
        print("Something went wrong")
    else:
        print("Most popular starting station:")
        print(df['Start Station'].value_counts().idxmax())
        print("Most popular ending station:")
        print(df['End Station'].value_counts().idxmax())
        print("Most popular combination of stations:")
        print(df.groupby(['Start Station', 'End Station']
                         ).size().idxmax())  # groups start and end station and counts the most common and identifies the key
'''prints Most popular starting station, Most popular ending station, and Most popular combination of stations on the terminal console, also prints the time it took to run the function, also prints error if there is an empty dataframe'''
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):

'''accepts filtered and city specified dataframe'''
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    if df.empty:
        print("Something went wrong")
    else:
        print("Total trip duration:")
        print(df['Trip Duration'].sum())  # adds all in column for total
        print("Average trip duration:")
        print(df['Trip Duration'].mean())  # averages all in column for average

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
'''prints Total trip duration and Average trip duration of stations on the terminal console, also prints the time it took to run the function, also prints error if there is an empty dataframe'''


def user_stats(df):

'''accepts filtered and city specified dataframe'''
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    if df.empty:
        print("Something went wrong")
    else:
        print("Most common user type:")
        print(df['User Type'].value_counts().idxmax())
    if 'Birth Year' in df.columns:
        print("Most recent birthyear:")
        # finds maximum year, which is most recent
        print(df['Birth Year'].max())
        print("Earliest birthyear:")
        print(df['Birth Year'].min())  # finds minimum year, which is earliest
        print("Most common birthyear:")
        # counts birth year occurence and shows the most common
        print(df['Birth Year'].value_counts().idxmax())
    else:
        print("No birth year info")
    if 'Gender' in df.columns:
        print("Most common gender:")
        print(df['Gender'].value_counts().idxmax())
    else:
        print("No gender info")
'''prints Most common user type, Most recent birthyear (if it exists in data), Earliest birthyear (if it exists in data), Most common birthyear(if it exists in data), and Most common gender (if it exists in data) on the terminal console, also prints the time it took to run the function, also prints error if there is an empty dataframe'''
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    '''runs all the functions and restarts if input is yes'''
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
