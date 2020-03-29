![Example output](https://kusekb.com/wp-content/uploads/2020/03/Screen-Shot-2020-03-28-at-7.44.58-PM.png)

**For those who prefer Jupyter notebooks, I have included one for convenience.**

This project is a python script (that updates daily) that will allow Mac/Linux users to run it in Terminal and view the current stats of coronavirus cases/deaths in any country, or worldwide. This task can also be automated in crontab.

The dataset is updated daily at 10:00 AM, and can be manually downloaded here: https://covid.ourworldindata.org/data/ecdc/full_data.csv

To get this process to run automatically, edit this line into crontab:
15 10 * * * current.sh

This will make the program run at 10:15 AM every day, which should account for any late uploads.

And make sure to use chmod +x current.sh so that the bash file becomes an executable. You can also edit current.sh to have any countries that you desire (also don't forget to edit the directories!). Make sure to look at the dataset to see which countries are able to be entered in. Some don't have any reported cases!

To run this program on its own, follow this guide or type python3 coronavirus.py to see this screen yourself:

![How to use](https://kusekb.com/wp-content/uploads/2020/03/Screen-Shot-2020-03-28-at-7.44.36-PM.png)

NOTE: PANDAS & CURL MUST BE INSTALLED, OTHERWISE THIS PROGRAM WILL NOT WORK CORRECTLY.

To install Pandas, follow this guide: https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html

If you are on a Mac and encounter the "no module named pandas" error while trying to install, you will need to fix this by installing pyenv. This error occurs because the default Python version for MacOS is 2.7. Follow this guide for pyenv: https://github.com/pyenv/pyenv and set your global version to 3.7.4 (or whatever the latest version is when you read this).

To install Curl on Linux (Macs come with Curl installed already), type sudo apt-get install curl
