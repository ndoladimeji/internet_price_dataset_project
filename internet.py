# importing the necessary packages
import pandas as pd
import numpy as np
#creating a dictionary containing the data files for the three csv files
DATA_FILES = {'wages': 'average_after_tax_wages.csv',
              'internet': 'average_monthly_internet.csv',
              'gdp': 'GDP_per_capita', 'adoption': 'internet_adoption.csv'}
print("Hello! Let's explore some internet prices data!")
'''
Getting user input to use as filters to display data.
While loop is being used to get a valid user input for wages, internet, gdp and adoption data
'''
def get_filter():
    """
    Asks user to specify whether to analyze wages, internet, gdp or adoption data.

    Returns:
        (str) city - name of the data file to analyze
    """
#creating an empty list for data files to avoid it being referenced before being defined
    data = ''
    while data not in DATA_FILES.keys():
        print("\nplease enter the data file you want to analyze (wages, internet, gdp, adoption).")
        print("You can use either upper or lower case for your inputs in this program.")
#using the lower() function to standardize user inputs
        data = input().lower()     
        if data not in DATA_FILES.keys():
            print("\nSorry, I didn't understand that. Enter a valid input.")
            print("\nTry again.")
#returning user inputs to increase interaction
    print("\nYou have selected {} as your data file".format(data.title()))
#returning city, month and day    
    return data

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
#returning the data frame   
    return df    

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
        data = get_filter()
        df = load_data(data)
          
        display_data(df)

#Getting user input to restart or not        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
	


