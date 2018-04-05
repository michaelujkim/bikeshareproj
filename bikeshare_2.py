
import time
import pandas as pd
import numpy as np
import datetime as dt

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    # get user input for month (all, january, february, ... , june)

    # get user input for day of week (all, monday, tuesday, ... sunday)
    city = input("Enter city: ")
    month = input("Enter month: ")
    day = input("Enter day: ")

    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    raw_csv = CITY_DATA[city]
    raw_df = pd.read_csv(raw_csv)
    raw_df['Start Time'] = pd.to_datetime(raw_df['Start Time'])
    raw_df['month'] = raw_df['Start Time'].dt.month

    raw_df['day'] = raw_df['Start Time'].dt.weekday
    raw_df['hour'] = raw_df['Start Time'].dt.hour
    month_int = int(month)
    day_int = int(day)
    if month_int == 0:
        month_sorted_df = raw_df
    else:
        month_df = raw_df['month'] == month_int
        month_sorted_df = raw_df[month_df]
    if day_int == 0:
        df = raw_df
    else:

        day_df = month_sorted_df['day'] == day_int
        df = month_sorted_df[day_df]

    print(df)
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    print(df['month'].value_counts().idxmax())

    print(df['day'].value_counts().idxmax())

    print(df['hour'].value_counts().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    print(df['Start Station'].value_counts().idxmax())

    print(df['End Station'].value_counts().idxmax())

    print(df.groupby(['Start Station', 'End Station']
                     ).size().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    print(df['Trip Duration'].sum())

    print(df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    print(df['User Type'].value_counts().idxmax())

    print(df['Gender'].value_counts().idxmax())

    # Display earliest, most recent, and most common year of birth
    print(df['Birth Year'].max())
    print(df['Birth Year'].min())
    print(df['Birth Year'].value_counts().idxmax())

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
