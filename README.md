**For those who prefer Jupyter notebooks, I have included one for convenience. To download it, click on "Raw" and then copy the text into your favorite text editor. Then save the file with the extension .ipynb and open it in Jupyter Notebooks.**

This project is a python script (that updates daily) that will allow Mac/Linux users to run it in Terminal and view the current stats of coronavirus cases/deaths in any country, or worldwide. This task can also be automated in crontab.

The dataset is updated daily at 10:00 AM, and can be manually downloaded here: https://covid.ourworldindata.org/data/ecdc/full_data.csv

To get this process to run automatically, edit this line into crontab:
15 10 * * * current.sh

This will make the program run at 10:15 AM every day, which should account for any late uploads.

And make sure to use chmod -x current.sh so that the bash file becomes an executable. You can also edit current.sh to have any countries that you desire (also don't forget to edit the directories!). Make sure to look at the dataset to see which countries are able to be entered in. Some don't have any reported cases!

To run this program on its own, type python3 coronavirus.py with all countries desired entered like so (with countries that have spaces entered with single quotes):

python3 coronavirus.py Italy Canada Mexico 'United States' 'Saudi Arabia' ...

To see worldwide data, type python3 coronavirus.py World

NOTE: PANDAS & CURL MUST BE INSTALLED, OTHERWISE THIS PROGRAM WILL NOT WORK CORRECTLY.

To install Pandas, follow this guide: https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html

To install Curl on Linux (Macs come with Curl installed already), type sudo apt-get install curl
