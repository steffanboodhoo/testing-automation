from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json, pprint, time
# browser = webdriver.Firefox()
browser = webdriver.Chrome()
browser.get('https://bonline.bmobile.co.tt/guest/payment/inmate')

# elem.send_keys(Keys.RETURN)

# def test_account_search():
# elem = browser.find_element_by_id('account_number')
# elem = browser.find_element_by_xpath("//input[@id='account_number'")
# elem = elem = browser.find_element_by_xpath("//input[@id='account_number']")
# elem.send_keys('12345678')
# elem = browser.find_element_by_id('btn_check_account')
# elem.click()

COMMAND_MAP = {
    # 'open': 'get',
    'click':'click',
    'type':'send_keys'
}
def execute_command(command, *args):
    print command
    print args

# browser.execute_script('valid_check_account.side')
# browser.execute_script('checkaccount.spec.js')
# assert 'account does not exist' in browser.page_source
with open('valid_check_account.side') as json_file:
    data = json.load(json_file)
commands = data['tests'][0]['commands']

for obj in commands:
    if obj['command'] in COMMAND_MAP:
        xpath = obj['targets'][2][0]
        print 
        print obj['command'],xpath[6:]
        elem = browser.find_element_by_xpath(xpath[6:])
        func = getattr(elem, COMMAND_MAP[obj['command']])
        func() if obj['value'] == '' else func(obj['value'])
    time.sleep(1)
        # print obj['targets'][2] # assumes the 3rd/index-2, entry contains the xpath description for element

