# fitbit
[Fitbit](https://www.fitbit.com)'s interface only lets you export one month of data at time. This Python script exports all months.

Python script that retrieves your Fitbit data

You'll need:
- [Selenium](http://selenium-python.readthedocs.io/) (`pip install selenium` should do it).
- An empty `Downloads` folder (there will be one CSV file for every month of data the script retrieves).
- [Chromedriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) on the same folder your script is (or provide the full path to it on line 11).
- Tweak lines 6, 7, 8 to provide your e-mail, password, and how many months back you want to go.
