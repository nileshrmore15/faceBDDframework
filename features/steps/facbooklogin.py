from behave import *
# import bdb
# bdb.set_trace()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators import fbloginLocators
## for get log function
from Logs import logfile
log = logfile.get_logs()
##

@given('page open')
def step_impl(context):
    context.driver.get('https://www.facebook.com')
    log.info('facebook link get open')


@when('I enter invalid username and password')
def step_impl(context):
    # context.driver.find_element(By.XPATH, '//input[contains(@name,"mail")]').send_keys("nileshrmore15@gmail.com")
    # context.driver.find_element(By.XPATH, '//input[contains(@name,"pass")]').send_keys('djdjd')
    #
    context.driver.find_element(list(fbloginLocators.input_field_login.keys())[0],
                                list(fbloginLocators.input_field_login.values())[0]).send_keys('ifjrycfse32ws@gmail.com')
    log.info('username entered')
    context.driver.find_element(list(fbloginLocators.input_field_password.keys())[0],
                                list(fbloginLocators.input_field_password.values())[0]).send_keys('dheuh')
    log.info('password entered')


@when('I click the login button')
def step_impl(context):
    #context.driver.find_element(By.XPATH, '//button[contains(@name,"login")]').click()
    context.driver.find_element(list(fbloginLocators.button_login.keys())[0], list(fbloginLocators.button_login.values())[0]).click()
    log.info('login button pressed')
    print("test pass")

#
# @then('It should be failed')
# def step_impl(context):
#     try:
#         # Wait up to 10 seconds for either element to be visible
#         wait = WebDriverWait(context.driver, 20)
#         element1 = wait.until(EC.visibility_of_element_located((By.XPATH, '//a[contains(@href,"https://facebook.com/login/identify/")]')))
#         print("Element 1 is visible")
#     except:
#         try:
#             element2 = wait.until(
#                 EC.visibility_of_element_located((By.XPATH, '//a[contains(text(),"Forgotten password?")]')))
#             print("Element 2 is visible")
#         except:
#             print("Neither element 1 nor element 2 is visible")


@then('It should be failed')
def step_impl(context):
    print("test failed scanerio")
    try:
        element = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//a[contains(text(),"Forgotten password?")]'))
        )
        log.info('invalid password entered message displayed as expected')
        print('test case pass')
    except:
        log.error('invalid username entered or invalid password getting successful login')
        print('test case failed')

    # try:
    #     ele = context.driver.find_element(By.XPATH, '//a[contains(text(),"Forgotten password?")]')
    #     if ele.is_displayed():
    #         log.info('invalid password entered message displayed as expected')
    #         print("test pass")
    # except:
    #     log.error('invalid username entered or invalid password getting successful login')
    #
