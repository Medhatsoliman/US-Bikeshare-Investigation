# Mentioned below the websites links and refrences I used in coding this application.
# https://docs.python.org/3/library/datetime.html
# https://www.geeksforgeeks.org/difference-between-list-and-dictionary-in-python/
# https://www.w3schools.com/python/python_for_loops.asp
# https://www.datacamp.com/community/tutorials/functions-python-tutorial
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html

import time
import pandas as pd
import numpy as np

CITY_DATA_LIST = { 'chicago' : 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


"""Defining the list of Days"""
DAYS_DATA_LIST = [ "saturday","sunday","monday","tuesday","wednesday","thursday","friday","all_days"]

"""Defining the list of Months"""

MONTHS_DATA_LIST = ["january", "february", "march", "april", "may", "june","all_months"]



def get_filters():
    """
   For the purpose of analyzing,the user will be required to enter city,month and day.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    name_of_city = ''
    while name_of_city.lower() not in CITY_DATA_LIST:
        name_of_city = input("\nWhat is the name of the city to analyze data? (E.g. Input either chicago, new york city, washington)\n")
        if name_of_city.lower() in CITY_DATA_LIST:
            #We were able to get the name of the city to analyze data.
            city = CITY_DATA_LIST[name_of_city.lower()]
        else:
            #In case we were not able to get the name of the city to analyze data,  we will continue the loop.
            print("Sorry we were not able to get the name of the city to analyze data, Please enter one the following choices : chicago, new york city or washington.\n")

    # TO DO: get user input for month (all, january, february, ... , june)
    name_of_month = ''
    while name_of_month.lower() not in MONTHS_DATA_LIST:
        name_of_month = input("\nWhat is the name of the month to filter data? (E.g. Input either 'all_months' to apply no month filter or january, february, ... , june)\n")
        if name_of_month.lower() in MONTHS_DATA_LIST:
            #We were able to get the name of the month to analyze data.
            month = name_of_month.lower()        
        else:
            #We were not able to get the name of the month to analyze data so we continue the loop.
            print("Sorry we were not able to get the name of the month to filter data, Please input either 'all_months' to apply no month filter or january, february, ... , june.\n")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    name_of_day = ''
    while name_of_day.lower() not in DAYS_DATA_LIST:
        name_of_day = input("\nWhat is the name of the day to filter data? (E.g. Input either 'all_days' to apply no day filter or monday, tuesday, ... sunday)\n")
        if name_of_day.lower() in DAYS_DATA_LIST:
            #We were able to get the name of the month to analyze data.
            day = name_of_day.lower()
        else:
            #We were not able to get the name of the month to analyze data so we continue the loop.
            print("Sorry we were not able to get the name of the day to filter data, Please input either 'all_days' to apply no day filter or monday, tuesday, ... sunday.\n")

    return city, month, day


def load_data(city, month, day):
    """
    We are going to pass the acquired arguments gained from the above function(get_filters)
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe according to the user's input.pandas dataframe will be used
    df = pd.read_csv(city)

    # convert the Start Time column to datetime
    """After loading the dataframe from the csv file,the code will start to extract the dataset and putting them in a user defined columns"""
    df['Start Time'] = pd.to_datetime(df['Start Time'])  
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour


    # filter by month if applicable
    if month != 'all_months':
        # use the index of the months list to get the corresponding int
        month = MONTHS_DATA_LIST.index(month)

        # filter by month to create the new dataframe
        df = df.loc[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all_days':
        # filter by day of week to create the new dataframe
        df = df.loc[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel.

    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    month_mode = df['month'].mode()[0]
    print("The most frequent month from the given filtered data is: " + MONTHS_DATA_LIST[month_mode].title())

    # TO DO: display the most common day of week
    day_of_week_mode = df['day_of_week'].mode()[0]
    print("The most frequent day of week from the given filtered data is: " + day_of_week_mode)

    # TO DO: display the most common start hour
    start_hour_mode = df['hour'].mode()[0]
    print("The most frequent start hour from the given filtered data is: " + str(start_hour_mode))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-*-'*60)

def station_stats(df):
    """Displays statistics on the most popular stations and trip.

    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: Starting station most used to be displayed
    common_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station from the given filtered data is: " + common_start_station)

    # TO DO: end station most commonly used to be displayed
    common_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station from the given filtered data is: " + common_end_station)

    # TO DO: most frequent combination of start station and end station trip to be displayed
    frequent_combination = (df['Start Station'] + "||" + df['End Station']).mode()[0]
    print("The most frequent combination of start station and end station trip is : " + str(frequent_combination.split("||")))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-*-'*60)

""" The following function will be used to return statistics of the trip duration according to the dataframe gained throgh connecting with the csv file"""
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration.

    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    overall_travel_time = df['Trip Duration'].sum()
    print("The total travel time from the given fitered data is: " + str(overall_travel_time))

    # TO DO:  mean travel time to be displayed
    travel_time_mean = df['Trip Duration'].mean()
    print("The mean travel time from the given fitered data is: " + str(travel_time_mean))

    print("\nThis calculation took %s seconds." % (time.time() - start_time))
    print('-*-'*60)

""" The following function will be used to return statistics of the bikeshare user according to the dataframe gained throgh connecting with the csv file"""
def user_stats(df, city):
    """Displays statistics on the bikeshare users.

    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating the User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    types_of_user = df['User Type'].value_counts()
    print("The count of the user types from the given filtered data is: \n" + str(types_of_user))

    if city == 'chicago.csv' or city == 'new_york_city.csv':
        # TO DO: Display counts of gender
        the_user_gender = df['Gender'].value_counts()
        print("The count of user gender from the given filtered data is: \n" + str(the_user_gender))

        # TO DO: Display earliest, most recent, and most common year of birth
        the_earliest_birth = df['Birth Year'].min()
        the_most_recent_birth = df['Birth Year'].max()
        the_most_common_birth = df['Birth Year'].mode()[0]
        print('Earliest birth from the given fitered data is: {}\n'.format(the_earliest_birth))
        print('Most recent birth from the given fitered data is: {}\n'.format(the_most_recent_birth))
        print('Most common birth from the given fitered data is: {}\n'.format(the_most_common_birth) )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-*-'*60)


def display_raw_data(df):
    """Displays raw data on user request.

    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """
    print(df.head())
    next = 0
    while True:
        raw_data_display = input('\nWould you like to view next five row of raw data? Enter YES or NO.\n')
        if raw_data_display != 'YES':
            return
        next = next + 5
        print(df.iloc[next:next+5])


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        while True:
            view_raw_data = input('\nWould you like to view first five row of raw data? Enter YES or NO.\n')
            if view_raw_data != 'YES':
                break
            display_raw_data(df)
            break

        restart = input('\nWould you like to restart? Enter YES or NO.\n')
        if restart != 'YES':
            break


if __name__ == "__main__":
    main()
