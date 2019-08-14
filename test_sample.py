from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Firefox()
browser.get('https://bonline.bmobile.co.tt/guest/payment/inmate')

# elem.send_keys(Keys.RETURN)
print browser.title

def test_account_search():
    elem = browser.find_element_by_id('account_number')
    elem.send_keys('12345678')
    elem = browser.find_element_by_id('btn_check_account')
    elem.click()
    print browser.page_source
    time.sleep(1)
    assert 'account does not exist' in browser.page_source

