# importing the necessary packages
import pandas as pd
import numpy as np
import time
#creating a dictionary containing the data files for the three csv files
DATA_FILES = {'wages': 'average_after_tax_wages_cleaned.csv',
              'internet': 'average_monthly_internet_cleaned.csv',
              'gdp': 'GDP_per_capita_cleaned.csv', 'adoption': 'internet_adoption_cleaned.csv'}
print("\nHello! Let's explore some internet prices data!")
'''
Getting user input to use as filters to display data.
While loop is being used to get a valid user input for wages, internet, gdp and adoption data
'''
def get_filters():
    """
    Asks user to specify whether to analyze wages, internet, gdp or adoption data.

    Returns:
        (str) city - name of the data file to analyze
    """
#creating an empty list for data files to avoid it being referenced before being defined
    data = ''
    while data not in DATA_FILES.keys():
        print("\nPlease enter the data file you want to analyze (wages, internet, gdp, adoption).")
        print("You can use either upper or lower case for your inputs in this program.")
#using the title() function to standardize user inputs
        data = input().lower()     
        if data not in DATA_FILES.keys():
            print("\nSorry, I didn't understand that. Enter a valid input.")
            print("\nTry again.")
#returning user inputs to increase interaction
    print("\nYou have selected {} as your data file".format(data.title()))

#Creating a dictionary for available countries
   
    COUNTRY_DATA = {'Albania': 0, 'Algeria': 1, 'Argentina': 2, 'Australia': 3, 'Austria': 4, 'Azerbaijan': 5, 'Bahrain': 6, 'Bangladesh': 7, 'Belarus': 8, 'Belgium': 9, 'Bosnia And Herzegovina': 10, 'Brazil': 11, 'Bulgaria': 12, 'Canada': 13, 'Chile': 14, 'China': 15, 'Colombia': 16, 'Costa Rica': 17, 'Croatia': 18, 'Cyprus': 19, 'Czech Republic': 20, 'Denmark': 21, 'Dominican Republic': 22, 'Ecuador': 23, 'Egypt': 24, 'Estonia': 25, 'Finland': 26, 'France': 27, 'Georgia': 28, 'Germany': 29, 'Greece': 30, 'Hong Kong': 31, 'Hungary': 32, 'Iceland': 33, 'India': 34, 'Indonesia': 35, 'Iraq': 36, 'Ireland': 37, 'Israel': 38, 'Italy': 39, 'Japan': 40, 'Jordan': 41, 'Kazakhstan': 42, 'Kenya': 43, 'Latvia': 44, 'Lebanon': 45, 'Lithuania': 46, 'Luxembourg': 47, 'Malaysia': 48, 'Malta': 49, 'Mexico' : 50, 'Morocco': 51, 'Nepal': 52, 'Netherlands': 53, 'New Zealand': 54, 'Nigeria': 55, 'Norway': 56, 'Oman': 57, 'Pakistan': 58, 'Peru': 59, 'Philippines': 60, 'Poland': 61, 'Portugal': 62, 'Qatar': 63, 'Romania': 64, 'Russia': 65, 'Saudi Arabia': 66, 'Serbia': 67, 'Singapore': 68, 'Slovakia': 69, 'Slovenia': 70, 'South Africa': 71, 'South Korea': 72, 'Spain': 73, 'Sri Lanka': 74, 'Sweden': 75, 'Switzerland': 76, 'Thailand': 77, 'Trinidad And Tobago': 78, 'Tunisia': 79, 'Turkey': 80, 'Ukraine': 81, 'United Arab Emirates': 82, 'United Kingdom': 83, 'United States': 84, 'Uruguay': 85, 'Vietnam': 86}
    country = ''
    while country not in COUNTRY_DATA.keys():
        print("\nPlease enter the country you want to see data for (Albania, Algeria, Argentina, Australia, Austria, Azerbaijan, Bahrain, Bangladesh, Belarus, Belgium, Bosnia And Herzegovina, Brazil, Bulgaria, Canada, Chile, China, Colombia, Costa Rica, Croatia, Cyprus, Czech Republic, Denmark, Dominican Republic, Ecuador, Egypt, Estonia, Finland, France, Georgia, Germany, Greece, Hong Kong, Hungary, Iceland, India, Indonesia, Iraq, Ireland, Israel, Italy, Japan, Jordan, Kazakhstan, Kenya, Latvia, Lebanon, Lithuania, Luxembourg, Malaysia, Malta, Mexico, Morocco, Nepal, Netherlands, New Zealand, Nigeria, Norway, Oman, Pakistan, Peru, Philippines, Poland, Portugal, Qatar, Romania, Russia, Saudi Arabia, Serbia, Singapore, Slovakia, Slovenia, South Africa, South Korea, Spain, Sri Lanka, Sweden, Switzerland, Thailand, Trinidad And Tobago, Tunisia, Turkey, Ukraine, United Arab Emirates, United Kingdom, United States, Uruguay, Vietnam)")
        country = input().title()      
        if country not in COUNTRY_DATA.keys():
            print("Sorry, I didn't understand that. Try another country name")
            print("Try Again")
    print("\n You have chosen country as {}".format(country))
    country = COUNTRY_DATA[country]
#returning data, and country    
    return data, country

#Defining a function to load data based on user inputs
def load_data(data):
    """
    Loads data for the specified data file.

    Args:
        (str) data - name of the data file to analyze

    Returns:
        df - Pandas DataFrame containing data file
    """
    print("\nLoading your data now......")
#Getting the data frame from the source files    
    df = pd.read_csv(DATA_FILES[data])
    df = df.transpose()
#returning the data frame   
    return df

#Defining function to calculate internet price statistics  
def file_stats(df, country):
    """Displays statistics on the mode, min and mean data over the years."""
    print('\nCalculating The Mode, Min and Mean Data Over The Years...\n')
#Asigning a variable to the present time. Employing time() method
#This will be used in calculating the time spent on generating the statistics
#You will see this occur throughout the program    
    start_time = time.time()
#Using mode() method to generate modal price    
    Highest = max(df[country][1:])
    print("\nThe max is {}".format(Highest))
    Lowest = min(df[country][1:])
    print("\nThe min is {}".format(Lowest))
    Avg = np.mean(df[country][1:])
    print("\nThe average is {}".format(Avg))
    print("\nThis took {} seconds".format(time.time() - start_time))
    print('-'*40)



#Defining function to display raw data to the user    
def display_data(df):
#Creating a list of possible responses    
    possible_response = ['yes','no']
    raw_data = ''
#Setting a variable 'counter' to zero to track the number of raw data displayed at once    
    counter = 0
#Using a while loop to get valid user input    
    while raw_data not in possible_response:
        print("\nDo you want to view the raw data?")
        print("\nEnter 'yes' or 'no'.")
#Getting user response to view raw data or not        
        raw_data = input().lower()
#Using if statement to display raw data to user    
        if raw_data == 'yes':
            print(df.head())
        elif raw_data not in possible_response:
            
            print("\nSorry, I didn't understand that.\nEnter a valid input.")
            print("\nTry again....")
#Emloying another while loop to display more rows of raw data            
    while raw_data == 'yes':
        print("\nDo you want to view more raw data?")
        print("\nEnter 'yes' or 'no'.")
        counter += 5
        raw_data = input().lower()
        if raw_data == 'yes':
            print(df[counter:counter+5])

        elif raw_data != 'yes':
            break
    print('-'*40) 


#Defining a main function that calls all other functions in the program
def main():
    while True:
        data, country = get_filters()
        df = load_data(data)
          
        file_stats(df, country)
        display_data(df)

#Getting user input to restart or not        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
	

