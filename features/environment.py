from selenium import webdriver


def before_scenario(context, scenario):
    print("Browser window gets open")
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()


def after_scenario(context, scenario):
    print("Browser get close")
    context.driver.close()
