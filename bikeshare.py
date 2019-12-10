import time
import pandas as pd
import numpy as np
from datetime import datetime

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ['chicago', 'new york', 'washington']
    while True:
        city = input("Pick which US city's bikeshare data you would like to see - we only have data for Chicago, New York, or Washington:").lower()
        if city not in ('chicago', 'new york', 'washington'):
            print("Not an appropriate choice.")
        else:
            break
    print('City'+ ' '+city + ' ' + 'selected')

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ["January", "February", "March", "April", "May", "June", "all"]
    
    while True:
        month = input("Which month would you like to see data for January, February, March, April, May, June? or all: ")
        if month not in ("January", "February", "March", "April", "May", "June", "all"):
            print('please select a valid option')
        else:
            break
    print('Your selection has been applied')
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = ["Mon", "Tues", "Weds", "Thurs", "Fri", "Sat", "Sun", "all"]
    while True:
        day = input("Which day of the week would you like to see data for Mon, Tues, Weds, Thurs, Fri, Sat, Sun or all?: ")
        if day not in ("Mon", "Tues", "Weds", "Thurs", "Fri", "Sat", "Sun", "all"):
            print('please select valid option')
        else:
            break
    #print('no specfic week filtering applied')

    print('-'*40)
    print('Let\'s explore the United States bikeshare data of {} filtered by {} '.format(city, month))
    return city, day, month

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
    print("Your bikeshare data is loading data ...")
   
    df = pd.read_csv(CITY_DATA[city])

#Convert [Sart Time] column to datetime module

    d#f['Start Time'] = pd.datetime.timestamp(df['Start Time'])
    df['Start Time'] = date_series
    df.head()

#Create new column of DOW - Day of week and Month, by extracting Month and DOW from Start Time

    df['month'] = df['Start Time'].dt.month

    df['day_of_week'] = df['Start Time'].dt.day_name()

# filter by month if applicable
    if month != 'all':
# use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

    # filter by month to create the new dataframe
    df = df.loc[df['month'] == month,:]
    # filter by day of week if applicable
    if day != 'all':
# filter by day of week to create the new dataframe
        df = df.loc[df['day_of_week'] == day,:]

#def time_stats(df):
    #"""Displays statistics on the most frequent times of travel."""

    print("\nCalculating the most frequent times of travel...\n")
    start_time = time.time()
     # TO DO: display the most common month
    frequent_month = df["month"].mode()[0]
    print("Most frequent month:", frequent_month)
        
     # TO DO: display the most common day of week
    frequent_day = df["day_of_week"].mode()[0]
    print("Most frequent day:", frequent_day)
    
    # TO DO: display the most common start hour
    df['hour'] = df["Start Time"].dt.hour
    frequent_hour = df['hour'].mode()[0]
    print("Most frequent hour:", frequent_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print("\n Calculating the most Popular stations and trip...\n")
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = str(df['start_station'].mode()[0])
    print('The most popular starting bikeshare station is {}'.format(popular_start_station))
    # TO DO: display most commonly used end station
    popular_end_station = str(df['end_station'].mode()[0])
    print('The most popular ending bikeshare station is {}'.format(popular_end_station))
    # TO DO: display most frequent combination of start station and end station trip
    print('Most frequently used combination of start station and end station trip:', combination_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = sum(df['Trip Duration'])
    print("The total travel time is:", total_travel_time/86400, "Days")

    # TO DO: display mean travel time
    mean_travel_time = df["Trip Duration"].mean()
    print("The mean travel time is:", mean_travel_time/60, "Minutes")
          
     
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    #"""Displays statistics on bikeshare users."""
    print('\n We are calculating the bikeshare User Statistics...\n')
    start_time = time.time()
    
          
    # TO DO: Display counts of user types 
    user_types = df["User Type"].value_counts()

    # TO DO: Display counts of gender
    while (city != "washington"):
        male = int(df[df["gender"] == "Male"].gender.value_counts())
        female = int(df[df["gender"] == "Female"].gender.value.counts())
        print("Gender Types {}{}:")
    
    # TO DO: Display earliest year of birth        
    while (city != "washington"):
        try:
            earliest_year = int(df['birth_year']).min()
            print('The oldest bikeshare user was born in  {}'.format(earliest_year))
        except:
            print("exception")
    # TO DO: Display most recent year of birth  
    recent_year = int(df['birth_year']).max()
    print('Youngest user was born in {}'.format(recent_year))
    # TO DO: Display most common year of birth
        
    common_year = int(df['birth_year']).mode()
    print('Users born in the year {} are the most common bikeshare users'.format(common_year))
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