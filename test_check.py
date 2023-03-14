import pytest
import time
from selenium.webdriver.common.by import By
from BaseClass import BaseClass
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.Functional
@pytest.mark.usefixtures("setup")
class Test_func(BaseClass):

    def test_review_no_text(self, setup):
        log = self.getLogger()
        log.debug("Add a text for review")
        setup.find_element(By.XPATH, "//input[@name='search_string']").send_keys("Egypt")
        setup.find_element(By.CSS_SELECTOR, "button[value='search']").click()
        setup.find_element(By.XPATH, "//img[@alt='good']").click()
        setup.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Raed")
        setup.find_element(By.CSS_SELECTOR, "label[title='Very good']").click()
        element = setup.find_element(By.ID, "review_add")
        setup.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(7)
        element.click()
        assert setup.find_element(By.XPATH, "//textarea[@name='review_text']").is_selected(), "Error, the review not added"
        print("The review is added")


    def test_review_no_name(self, setup):
        log = self.getLogger()
        log.debug("Add the name for review")
        setup.find_element(By.XPATH, "//input[@name='search_string']").send_keys("Egypt")
        setup.find_element(By.CSS_SELECTOR, "button[value='search']").click()
        setup.find_element(By.XPATH, "//img[@alt='good']").click()
        setup.find_element(By.XPATH, "//textarea[@name='review_text']").send_keys("Nice")
        time.sleep(7)
        setup.find_element(By.CSS_SELECTOR, "label[title='Very good']").click()
        element = setup.find_element(By.ID, "review_add")
        setup.execute_script("arguments[0].scrollIntoView()", element)
        time.sleep(7)
        element.click()
        assert not setup.find_element(By.CSS_SELECTOR, "input[name='name']").is_displayed(), "Error, add the name"
        print("The review is added")



    def test_search_letter(self, setup):
        log = self.getLogger()
        log.info("the search is display")
        setup.find_element(By.XPATH, "//input[@name='search_string']").send_keys("F")
        time.sleep(1)
        setup.find_element(By.CSS_SELECTOR, "button[value='search']").click()
        actual_list = ['France']
        list_countries = []
        countries = setup.find_elements(By.CLASS_NAME, "card-title")
        for country in countries:
            list_countries.append(country.text)
        assert actual_list == list_countries, "The search filed, write again! "
        print("Passed")

    def test_without_video(self, setup):
        log = self.getLogger()
        log.error("A major error has happend")
        setup.find_element(By.CSS_SELECTOR, "a[href='/add_data']").click()
        setup.find_element(By.XPATH, "//input[@name='filename']").send_keys(
            "C://Users//windows11//Desktop//project 2//country//mor.jpg")
        setup.find_element(By.CSS_SELECTOR, "input[name='country_name']").send_keys("Morocco")
        setup.find_element(By.CSS_SELECTOR, "input[name='capital_name']").send_keys("Rabat")
        setup.find_element(By.XPATH, "//input[@name='official_language']").send_keys("Arabic")
        setup.find_element(By.XPATH, "//input[@name='country_currency']").send_keys("Moroccan dirham (MAD)")
        setup.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        setup.find_element(By.XPATH, "//input[@name='search_string']").send_keys("Morocco")
        setup.find_element(By.CSS_SELECTOR, "button[value='search']").click()
        actual_list = ['Morocco']
        list_countries = []
        countries = setup.find_elements(By.CLASS_NAME, "card-title")
        for country in countries:
            list_countries.append(country.text)
        assert actual_list == list_countries, "The upload for country is filed "
        print("Passed")



    def test_without_image(self, setup):
        log = self.getLogger()
        log.error("A major error has happend")
        setup.find_element(By.CSS_SELECTOR, "a[href='/add_data']").click()
        setup.find_element(By.CSS_SELECTOR, "input[name='country_name']").send_keys("China1")
        setup.find_element(By.CSS_SELECTOR, "input[name='capital_name']").send_keys("Beijing")
        setup.find_element(By.XPATH, "//input[@name='official_language']").send_keys("Standard Chinese")
        setup.find_element(By.XPATH, "//input[@name='country_currency']").send_keys("Renminbi")
        setup.find_element(By.XPATH, "//input[@name='country_currency']").send_keys("Renminbi")
        setup.find_element(By.CSS_SELECTOR, "input[name='video']").send_keys(
            "https://www.youtube.com/watch?v=vusOqZBKwek")
        setup.find_element(By.XPATH, "//input[@name='book']").send_keys(
            "https://www.booking.cn/searchresults.en-gb.html?ss=china&ssne=Egypt&ssne_untouched=Egypt&label=gog235jc-1DCAEoggI46AdIM1gDaGqIAQGYAQG4ARfIAQzYAQPoAQGIAgGoAgO4ApTfhKAGwAIB0gIkMTc2NWViN2MtZGQxNS00ODMzLTg1YWUtMTBhMWI5MzYwMDZh2AIE4AIB&sid=f6c61854a2708dbd0802c8f63668bdc4&aid=397594&lang=en-gb&sb=1&src_elem=sb&src=searchresults&checkin=2023-03-06&checkout=2023-03-10&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure")

        setup.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        setup.get("http://127.0.0.1:5000")
        setup.find_element(By.XPATH, "//input[@name='search_string']").send_keys("China1")
        setup.find_element(By.CSS_SELECTOR, "button[value='search']").click()
        countries = setup.find_elements(By.CLASS_NAME, "card-title")
        expected_list = ["China1"]
        actual_list = []
        for country in countries:
            actual_list.append(country.text)
        assert expected_list == actual_list, "The upload for country is filed"
        print("Passed")

    def test_title(self, setup):
        setup.find_element(By.XPATH, "//input[@name='search_string']").send_keys("Egypt")
        setup.find_element(By.CSS_SELECTOR, "button[value='search']").click()
        setup.find_element(By.XPATH, "//img[@alt='good']").click()
        time.sleep(4)
        country = setup.find_element(By.CSS_SELECTOR, "section[class='header'] h1").text
        country = country.strip("Hello")
        country = country.strip("In ")
        print(country)
        setup.switch_to.frame("booking")
        time.sleep(10)
        loc = setup.find_element(By.XPATH, "//input[@id=':Rp5:']").get_attribute("value")
        print(loc)
        assert loc == country, "title not match"
        print("Passed")

def test_crossBrowser(crossBrowser):
    print(crossBrowser)
