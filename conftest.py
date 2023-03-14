import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture()
def setup():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    service_obj = Service("chromedriver_linux64/chromedriver")
    driver = webdriver.Chrome(service=service_obj, options=chrome_options)
    driver.implicitly_wait(3)
    driver.maximize_window()
    driver.get("http://127.0.0.1:5000/")
    yield driver
    driver.close()
    driver.quit()





@pytest.fixture(params=["Chrome", "Edge"])
def crossBrowser(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "edge":
        driver = webdriver.Edge()
    else:
        driver = None

    yield driver

    if driver:
        driver.quit()

