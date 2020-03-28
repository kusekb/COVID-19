This project is a python script (that updates daily) that will allow Mac/Linux users to run it in Terminal and view the current stats of coronavirus cases/deaths in any country, or worldwide. This task can also be automated in crontab for convenience.

The dataset is updated daily at 10:00 AM, and can be manually downloaded here: https://covid.ourworldindata.org/data/ecdc/full_data.csv

To get this process to run automatically, edit this line into crontab:
15 10 * * * current.sh

And make sure to use chmod -x current.sh so that the bash file becomes an executable. You can also edit current.sh to have any countries that you desire. Make sure to look at the dataset to see which countries are able to be entered in. Some don't have any reported cases!

To run this program on its own, type python3 coronavirus.py with all countries desired entered like so (with countries that have spaces entered with single quotes):

python3 coronavirus.py Italy Canada Mexico 'United States' 'Saudi Arabia' ...

To see worldwide data, type python3 coronavirus.py World

NOTE: PANDAS & CURL MUST BE INSTALLED, OTHERWISE THIS PROGRAM WILL NOT WORK CORRECTLY
