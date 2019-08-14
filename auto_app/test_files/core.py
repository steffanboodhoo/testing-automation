from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import json, pprint, time
import traceback

COMMAND_MAP = {
    # 'open': 'get',
    'click':'click',
    'type':'send_keys'
}

def run_test(application_uri, test_file_path, expected_text, timeout=5, browser='CHROME'):
    browser = webdriver.Chrome()
    browser.get(application_uri)

    #load json test file into data
    with open(test_file_path) as json_file:
        data = json.load(json_file)
    #grab the commands from the file
    commands = data['tests'][0]['commands']

    for obj in commands:
        if obj['command'] in COMMAND_MAP:
            #path of element
            xpath = obj['targets'][2][0] #xpath[6:]
            #try to see if element can be found
            try:
                element_present = EC.presence_of_element_located((By.XPATH, xpath[6:]))
                WebDriverWait(browser, timeout).until(element_present)
            except TimeoutException:
                return {'status':'error', 'message':'execution could not be completed'}
            #element can be found so get it
            elem = browser.find_element_by_xpath(xpath[6:])
            func = getattr(elem, COMMAND_MAP[obj['command']])
            func() if obj['value'] == '' else func(obj['value'])
    
    for i in range(timeout):
        print expected_text
        if expected_text in browser.page_source:
            return {'status':'success', 'delay':i}
        time.sleep(1)
    return {'status':'failure', 'message':'expected text was not found'}
    # except Exception as e:
    #     traceback.print_exc()
    #     return {'status':'error', 'message':'execution could not be completed'}
    #print obj['targets'][2] # assumes the 3rd/index-2, entry contains the xpath description for element