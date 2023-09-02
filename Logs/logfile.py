import logging
from datetime import date, datetime
import os
# pip install allure-behave/allure-pytest
import allure



class AllureLoggingHandler(logging.Handler):
    def log(self, level_name, message):
        with allure.step(f"Log ({level_name}) {message}"):
            if level_name.lower() == "error":
                attach_screenshot_in_report()

    def emit(self, record):
        self.log(record.levelname, record.getMessage())


def get_logs():
    logger = logging.getLogger()
    ## it clear log file before log writing
    if logger.hasHandlers():
        logger.handlers.clear()
    ##
    logging.basicConfig(format="%(asctime)s [%(levelname)s] %(message)s (%(filename)s:%(lineno)s)", datefmt='%d/%m/%Y %I:%M:%S %p')
    #allure_handler = AllureLoggingHandler()
    filehandler = logging.FileHandler("D://pariplay//facebdd//Logs//log_file.log", mode="w")
    formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(module)s: %(funcName)s: %(message)s',
                                  datefmt='%d/%m/%Y %I:%M:%S %p')
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)
    logger.setLevel(logging.INFO)
    #logger.addHandler(allure_handler)
    return logger


def attach_screenshot_in_report():
    driver = logging.FileHandler.selenium_driver
    current_date_time = str(f'({(date.today().strftime("%d %b"))} {(datetime.now().strftime("%H_%M_%S"))})')
    screenshot_path = os.path.join(os.path.abspath(__file__ + '/../../'), f"Failed_Screenshots/{current_date_time}.png")
    driver.get_screenshot_as_file(screenshot_path)
    allure.attach.file(source=screenshot_path, attachment_type=allure.attachment_type.PNG, name="Screenshot")
