#This version has all color codes removed in order to make .txt output look correct!
#If you want to play around with this program in Terminal, it's highly suggested to use the regular version!

import pandas as pd
import datetime as dt
import sys

covid_data = pd.read_csv('full_data.csv')

def COVID_TERROR_PANIC_RUN_FIRE_EVERYWHERE(country):
#Corrects the case of the country
	country = country.title()

#Fix for input as 'US' instead of 'United States'
	if country == 'Us':
		country = 'United States'

#Displays list of countries if you type 'Help'
	if country == 'Help':
		print(covid_data.location.unique())
		return False;

#If the country isn't valid then return False
	if country not in covid_data['location'].values:
		print('\n')
		print('Sorry, "{}" is either spelled incorrectly or is not in the list of countries with confirmed cases.'.format(country))
		print('\n')
		print("Make sure to put 'single quotes' around countries that contain spaces.")
		print("For example: python3 coronavirus.py 'United States'")
		print('\n')
		print("You can type 'Help' to see the list of countries like so:")
		print("python3 coronavirus.py Help")
		print('\n')
		return False;

#Grabs the rows from the table with the specified country
	country_rows = covid_data[covid_data['location'] == country]

#Gets the last date entry of the country
	max_date = country_rows.date.max()

#Formats the date into Month Day, Year
	formated_date = dt.datetime.strptime(max_date, '%Y-%m-%d')
	formated_date = formated_date.strftime('%B %d, %Y')

#Grabs the total cases and total deaths using max
	total_case = country_rows.total_cases.max()
	total_death = country_rows.total_deaths.max()

#Grabs the new_cases of the most recent date
	date_new_case = int(country_rows.new_cases.tail(1))

#Grabs the total new cases
	total_new_case = int(covid_data[covid_data['location'] == 'World'].new_cases.tail(1))

#Calculates the death rate using the total deaths and total cases
	death_rate = (total_death / total_case) * 100

#Grammar fix for "World"
	if country == "World":
		country = "the world"

#Prints up the information in a fancy way. Excludes the last line if you type "World"
	print('\n')
	print('The total number of cases in {} as of {}: {}.'.format(country, formated_date, total_case))
	print('The total number of deaths in {} as of {}: {:.0f}.'.format(country, formated_date, total_death))
	print('As of {}, the death rate in {} is {:.2f}%.'.format(formated_date, country, death_rate))
	print('On {}, there were {:.0f} new cases reported in {}.'.format(max_date, date_new_case, country))
	if country != "the world":
		print('On {}, there were {:.0f} new cases reported worldwide.'.format(max_date, total_new_case))
	print('\n')

#Main program that runs for each country you input
if __name__ == '__main__':
	print('Program Starting...')
	#If you type nothing at all, the program gives you some help
	if len(sys.argv) == 1:
		print('\n')
		print('Please enter the countries you would like to see data for.')
		print('\n')
		print("You can type 'Help' to see the list of countries like so:")
		print("python3 coronavirus.py Help")
		print('\n')
		print("You can also type 'World' to see worldwide data.")
		print("Make sure to put 'single quotes' around countries that contain spaces.")		
		print('\n')
		print("Here is an example of how to do it:")
		print("python3 coronavirus.py China Italy 'United States' World")
		print('\n')
	for i in sys.argv[1:]:
		COVID_TERROR_PANIC_RUN_FIRE_EVERYWHERE(i)
	print('...Program Ended')
