import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import action_chains, keys

EMAIL = 'the_email_on_your_fitbit_account'
PASSWORD = 'the_password_of_your_fitbit_account'
MONTHS_TO_RETRIEVE = 60 # the number of months you want to go back

# start browser, log into Fitbit
browser = webdriver.Chrome('chromedriver')
browser.get('https://www.fitbit.com/logout')
action = action_chains.ActionChains(browser)
action.move_to_element(browser.find_element_by_name('email')).send_keys(EMAIL).send_keys(Keys.TAB).perform()
action.reset_actions()
action.move_to_element(browser.find_element_by_name('password')).send_keys(PASSWORD).perform()
browser.find_element_by_xpath("//*[contains(text(), 'Log In')]").click()

# loop through monthly intervals
for i in range(MONTHS_TO_RETRIEVE):

    # select month
    browser.get('https://www.fitbit.com/export/user/data')
    browser.find_element_by_id('CUSTOM').click()
    browser.find_element_by_id('showCalendarFrom').click()
    for e in range(i):
        browser.find_element_by_xpath('//*[@id="calendarFrom_t"]/thead/tr[1]/th/div/a[1]').click()
        time.sleep(1)
    browser.find_element_by_link_text('1').click() # start on day 1
    browser.find_element_by_id('showCalendarTo').click()
    for day in range(1, 32)[::-1]: # find last day of the month
        try:
            element = browser.find_element_by_link_text(str(day))
            browser.execute_script('arguments[0].click();', element)
            break
        except:
            continue

    # pick desired variables
    browser.find_element_by_xpath('//*[@id="dataExportForm"]/div[2]/div[2]/div[1]/div[3]/input').click()
    browser.find_element_by_xpath('//*[@id="dataExportForm"]/div[2]/div[2]/div[1]/div[4]/input').click()

    # download data
    browser.find_element_by_id('downloadButton').click()
    time.sleep(60)
