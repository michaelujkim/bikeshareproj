
import time
import pandas as pd
import numpy as np
import datetime as dt

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    # getting user input
    print('Hello! Let\'s explore some US bikeshare data!')

    city = input("Enter city (chicago, new york city, washington): ")
    month = input("Enter month as an integer (0=all,1=January,etc.): ")
    day = input("Enter day as integer(0=all, 1=monday, etc.): ")
    # all should return strings, some are cities, some are numbers
    return city, month, day


def load_data(city, month, day):
    # conditionals to account for wrong user input
    if city not in CITY_DATA:
        print("City is not in list")
        df = pd.DataFrame()  # empty data frames for conditionals in functions
    elif city == '':
        print("Please enter city")
        df = pd.DataFrame()
    elif month == '':
        print("Please enter month")
        df = pd.DataFrame()
    elif day == '':
        print("Please enter day")
        df = pd.DataFrame()
    else:
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


def time_stats(df):

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

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):

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

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):

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


def user_stats(df):

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

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
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
