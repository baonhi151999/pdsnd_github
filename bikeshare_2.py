import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

city_list = ['chicago', 'new york city', 'washington']
month_list = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
day_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']

def check_validation_input(promt, validation_option)
    """
    Gets user input and validates it against a set of allowed choices.
    Args:
    prompt (str): The message to display to the user when requesting input.
    valid_options (list): A list containing the allowed input choices.
    Returns:
    str: The user's valid input converted to lowercase.
    """
   while True:
        user_input = input(promt).lower.()
        if user_input in validation_option:
            return user_input
        else:
            print(f"Invalid input. Please choose from: {','.join(validation_option)}")
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Greetings! Let\'s delve into some fascinating US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = check_validation_input('Please enter the city name: ', city_list)
        if city in city_list:
            break
        else:
            print('Oops! The city name you entered is invalid. Please provide a valid city name.')

    # get user input for month (all, january, february, ... , june)
    while True:
        month = check_validation_input('Please enter the month name: ', month_list)
        if month in month_list:
            break
        else:
            print('Oops! The month you entered is invalid. Please provide a valid month.')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = check_validation_input('Please enter the day name: ', day_list)
        if day in day_list:
            break
        else:
            print('Oops! The day you entered is invalid. Please provide a valid day.')

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads bikeshare data for the specified city and apllies filters for the month and day.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Day'] = df['Start Time'].dt.day_name()

    if month != 'all':
        month = month_list.index(month) + 1
        df = df[df['Month'] == month]
    
    if day != 'all':
        df = df[df['Day'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nAnalyzing the Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['Month'].mode()[0]
    print('The month with the highest frequency of bike rides is: '.format(common_month))

    # display the most common day of week
    common_day = df['Day'].mode()[0]
    print('The day with the most bike rides is: '.format(common_day))

    # display the most common start hour
    df['Hour'] = df['Start Time'].dt.hour
    common_hour = df['Hour'].mode()[0]
    print('The hour when bike rides are most frequent is: '.format(common_hour))

    print("\nThis analysis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nAnalyzing the Most Popular Stations and Trips...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('The most popular starting station for bike rides is: '.format(common_start_station))

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('The most popular ending station for bike rides is: '.format(common_end_station))

    # display most frequent combination of start station and end station trip
    df['Start End Station'] = df['Start Station'] + ' to ' + df['End Station']
    common_start_end_station = df['Start End Station'].mode()[0]
    print('The most frequent combination of start and end stations is: '.format(common_start_end_station))

    print("\nThis analysis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nAnalyzing Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time for bike rides is: '.format(total_travel_time))

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The average travel time for bike rides is: '.format(mean_travel_time))

    print("\nThis analysis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nAnalyzing User Statistics...\n')
    start_time = time.time()

    # Display counts of user types
    user_counts = df['User Type'].value_counts()
    print('The distribution of user types is as follows: '.format(user_counts))

    # Display counts of gender
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print('Here is the breakdown of gender: \n'.format(gender_counts))
    else:
        print('Unfortunately, gender data is not available for this city.')

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_birth_year = df['Birth Year'].min()
        print('The earliest birth year among users is: '.format(earliest_birth_year))

        most_recent_birth_year = df['Birth Year'].max()
        print('The most recent birth year among users is: '.format(most_recent_birth_year))

        common_birth_year = df['Birth Year'].mode()[0]
        print('The most common birth year among users is: '.format(common_birth_year))
    else:
        print('Unfortunately, birth year data is not available for this city.')

    print("\nThis analysis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df, start_loc=0):
    end_loc = start_loc + 5
    show_more = input("Would you like to see the next 5 rows of data? (yes/no): ")

    while show_more.lower() == 'yes':
        print(df.iloc[start_loc:end_loc])
        start_loc = end_loc 
        end_loc += 5

        if end_loc > len(df): 
            print("No more data available.")
            break

        show_more = input("Would you like to see the next 5 rows of data? (yes/no): ")

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        display_data(df)

        restart = input('\nWould you like to start over? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
