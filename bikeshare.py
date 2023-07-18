import time
import pandas as pd
import numpy as np

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
    cities = ["chicago", "new york city", "washington"]
    months = ["january", "february", "march", "april", "may", "june", "all"]
    weekdays = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"]
    
    while True:
        city = input("Would you like to see data for Chicago, New York City or Washington?\n").lower()
        if city in cities:
            break
        else:
            print("Invalid entry. Please enter Chicago, New York City, or Washington.")
    
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Enter the month you want to see data for.  Enter "All" to see data for all months\n').lower()
        if month in months:
            break
        else:
            print("Invalid entry. Please select All, or January, February, March, April, May, or June.")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Enter the day you want to see data for. Enter "All" to see data for all days\n').lower()
        if day in weekdays:
            break
        else:
            print("Invalid input. Please enter All or a valid day of the week.")

    print('-'*40)
    return city, month, day

    print('-'*40)
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
  
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    # filter by month if applicable
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month.title()]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df, month, day, city):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (dataframe) df - filtered dataframe with after user entries
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing timestats for the city, month, and day entered.
    """
  
    """Displays statistics on the most frequent times of travel."""
    city_message = ('\nCalculating The Most Frequent Times of Travel in the city of {}: \n').format(city)
    print(city_message)
    
    start_time = time.time()
    
    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    if month != 'all':
        print('The most common month is not available since you have selected', popular_month)
    else:
        print('The most common month is:', popular_month)

    # TO DO: display the most common day of week
    popular_weekday = df['day_of_week'].mode()[0]
    if day != 'all':
        print('The most common day is not available since you have selected', popular_weekday)
    else:
        print('The most common day of the week is:', popular_weekday)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('The most common hour of the day is:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df, city):

    """Displays statistics on the most popular stations and trip."""
    station_stats_message = "Calculating The Most Popular Stations and Trip in {}:\n".format(city)
    print(station_stats_message)

    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('The most common start station is:\n', popular_start_station)

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('The most common end station is:\n', popular_end_station)

    # display most frequent combination of start station and end station trip
    start_end_station_combined = (df['Start Station'] + ' / ' + df['End Station']).mode()[0]
    print('The most frequent combination of start station and end station trip is:\n', start_end_station_combined)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df, city):
    
    """Displays statistics on the total and average trip duration."""
    trip_duration_stats_message = ("Calculating Trip Duration in the city of {}: \n").format(city)
    print(trip_duration_stats_message)
    
    start_time = time.time()
    
    # TO DO: display total travel time
    # Trip duration is in second so need to divide by 60 (seconds), then again by 60 (minutes)
    total_travel_time_hours = int((df['Trip Duration'].sum() / 60 / 60))
    print('The total travel time by hour is:', total_travel_time_hours)
    
    # Add stat for total travel time in days
    total_travel_time_days = int((total_travel_time_hours / 24))
    print('The total travel time in days is:', total_travel_time_days)
    
    # Add stat for total travel time in weeks
    total_travel_time_weeks = int((total_travel_time_days / 7))
    print('The total travel time in weeks is:', total_travel_time_weeks, 'weeks')
    
    # add stat for total travel time in months
    total_travel_time_months = int((total_travel_time_weeks / 12))
    print('The total travel time in month is:', total_travel_time_months, 'months')
    
    # TO DO: display mean travel time
    travel_time_avg = int((df['Trip Duration'].mean() / 60))
    print('The average travel time per ride is:', travel_time_avg, 'minutes')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    user_stats_message = ("Calculating User Stats in the city of {}: \n").format(city)
    print(user_stats_message)
    start_time = time.time()
    
    if city != 'washington':
        # Display counts of user types
        user_type_count = df['User Type'].value_counts().to_frame()
        print('The breakdown of Total User Types is: \n', user_type_count)

        # Display counts of gender
        gender_type_count = df['Gender'].value_counts().to_frame()
        print('The breakdown of Total Gender typs is: \n', gender_type_count)

        # Display earliest, most recent, and most common year of birth
        earliest_birth_year = int(df['Birth Year'].min())
        print('The earliest birth year is:', earliest_birth_year)

        most_recent_birth_year = int(df['Birth Year'].max())
        print('The most recent birth year is:', most_recent_birth_year)

        most_common_birth_year = int(df['Birth Year'].mode()[0])
        print('The most common birth year is:', most_common_birth_year)
    else:
        print('There is no gender or birth year data available for Washington')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def get_raw_data(df):

    pd.set_option("display.max_columns", 200)
    
    rows = 0
    raw_data = input('\nWould you like to see 5 lines of raw data? Enter yes or no.\n')
    while True:
        if raw_data.lower() == 'yes':
            print(df.iloc[rows:rows+5])
            rows+=5
            raw_data = input('\nWould you like to see 5 more lines of raw data? Enter yes or no.\n')
        else:
            break

def main():
 
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, month, day, city)
        station_stats(df, city)
        trip_duration_stats(df, city)
        user_stats(df, city)
        get_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
           break

if __name__ == "__main__":
	main()
