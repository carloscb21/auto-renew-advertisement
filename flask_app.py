import time
from datetime import datetime
from flask import Flask, request, send_file
from browser_options import get_basic_setup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, \
    StaleElementReferenceException
from pathlib import Path
import utils.properties as properties

browser_setup = get_basic_setup()
options = browser_setup.options
web_home_path = browser_setup.web_home_path
driver_path = browser_setup.driver_path

app = Flask(__name__, static_url_path="")

with app.app_context():
    driver = webdriver.Chrome(executable_path=str(Path().absolute()) + driver_path, options=options)
    flag = True
    server_status = ""


@app.route("/")
def home():
    return send_file(str(Path().absolute()) + web_home_path)


@app.route("/status")
def status():
    return server_status


@app.route('/start')
def start():
    driver.get("https://www.milanuncios.com/")
    server_status = "started"
    return server_status


@app.route('/pause')
def pause():
    server_status = "pause"
    return server_status


@app.route('/stop')
def stop():
    if driver is not None:
        driver.quit()
    server_status = "stoped"
    flag = False
    return server_status


@app.route('/startAdvertisement')
def start_advertisement():
    """
        Start auto renew advertisement
    """
    timming = properties.timeHour * int(request.args.get(properties.label_timming))
    number_list = len(driver.find_elements_by_class_name(properties.list_items)) - 1
    while flag:
        try:
            get_current_time()
            print("Wait " + str(timming) + " seconds")
            time.sleep(timming)
            driver.refresh()
            time.sleep(4)
            driver.find_elements_by_xpath(properties.renew_item)[number_list].click()
            get_current_time()
            return server_status
        except ElementNotInteractableException:
            print("Error ElementNotInteractableException")
        except IndexError:
            print("Error IndexError")
        except StaleElementReferenceException:
            print("Error StaleElementReferenceException")
        except NoSuchElementException:
            print("Error NoSuchElementException")


def get_current_time():
    """
        Get Current date to register update advertisement
    """
    now = datetime.now()
    print("Renew advertisement at: " + now.strftime("%d/%m/%Y %H:%M:%S"))
