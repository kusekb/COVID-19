#This version has color codes and is meant to be run from the terminal! 
#It has colors to make the output more friendly and readable.
#If you want to have crontab output to a .txt file, do NOT use this version!
#Instead, use basic_coronavirus.py

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
		print('Sorry, "\033[1;31m{}\033[0;0m" is either spelled incorrectly or is not in the list of countries with confirmed cases.'.format(country))
		print('\n')
		print("Make sure to put '\033[1;36msingle quotes\033[0;0m' around countries that contain spaces.")
		print("For example: \033[1;40mpython3 coronavirus.py 'United States'\033[0;0m")
		print('\n')
		print("You can type '\033[1;33mHelp\033[0;0m' to see the list of countries like so:")
		print("\033[1;40mpython3 coronavirus.py Help\033[0;0m")
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
	print('The total number of cases in {} as of {}: \033[1;31m{}\033[0;0m.'.format(country, formated_date, total_case))
	print('The total number of deaths in {} as of {}: \033[1;31m{:.0f}\033[0;0m.'.format(country, formated_date, total_death))
	print('As of {}, the death rate in {} is \033[1;31m{:.2f}%\033[0;0m.'.format(formated_date, country, death_rate))
	print('On {}, there were \033[1;31m{:.0f}\033[0;0m new cases reported in {}.'.format(max_date, date_new_case, country))
	if country != "the world":
		print('On {}, there were \033[1;31m{:.0f}\033[0;0m new cases reported worldwide.'.format(max_date, total_new_case))
	print('\n')

#Main program that runs for each country you input
if __name__ == '__main__':
	print('Program Starting...')
	#If you type nothing at all, the program gives you some help
	if len(sys.argv) == 1:
		print('\n')
		print('Please enter the countries you would like to see data for.')
		print('\n')
		print("You can type '\033[1;33mHelp\033[0;0m' to see the list of countries like so:")
		print("\033[1;40mpython3 coronavirus.py Help\033[0;0m")
		print('\n')
		print("You can also type '\033[1;32mWorld\033[0;0m' to see worldwide data.")
		print("Make sure to put '\033[1;36msingle quotes\033[0;0m' around countries that contain spaces.")		
		print('\n')
		print("Here is an example of how to do it:")
		print("\033[1;40mpython3 coronavirus.py China Italy 'United States' World\033[0;0m")
		print('\n')
	for i in sys.argv[1:]:
		COVID_TERROR_PANIC_RUN_FIRE_EVERYWHERE(i)
	print('...Program Ended')
