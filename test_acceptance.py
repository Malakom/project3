import pytest
import time
from selenium.webdriver.common.by import By
from BaseClass import BaseClass

@pytest.mark.Acceptance
@pytest.mark.usefixtures("setup")
class Test_pages(BaseClass):
    def test_about_us(self, setup):
        log = self.getLogger()
        log.info("The page of 'about us' is opened")
        setup.find_element(By.CSS_SELECTOR, "a[href='/about_us']").click()
        assert "about_us" in setup.current_url, "page not founded"
        print("Passed")

    def test_contact_us(self, setup):
        log = self.getLogger()
        log.info("The page of 'contact us' is opened")
        setup.find_element(By.CSS_SELECTOR, "a[href='/contact']").click()
        assert "contact" in setup.current_url, "page not founded"
        print("Passed")


    def test_logo_button(self, setup):
        log = self.getLogger()
        log.info("The home page is opened")
        setup.find_element(By.XPATH, "//input[@name='search_string']").send_keys("France")
        setup.find_element(By.CSS_SELECTOR, "button[value='search']").click()
        setup.find_element(By.XPATH, "//img[@alt='good']").click()
        setup.find_element(By.XPATH, "//img[@src='/static//aiir.jpg']").click()
        assert setup.current_url == "http://127.0.0.1:5000/", "The logo button not display"
        print("Passed!")


    def test_same_image(self, setup):
        log = self.getLogger()
        log.warning("Something is in warning mode")
        setup.find_element(By.CSS_SELECTOR, "a[href='/add_data']").click()
        setup.find_element(By.XPATH, "//input[@name='filename']").send_keys("C://Users//windows11//Desktop//project 2//country//greece.jpeg")
        setup.find_element(By.CSS_SELECTOR, "input[name='country_name']").send_keys("China")
        setup.find_element(By.CSS_SELECTOR, "input[name='capital_name']").send_keys("Beijing")
        setup.find_element(By.XPATH, "//input[@name='official_language']").send_keys("Standard Chinese")
        setup.find_element(By.XPATH, "//input[@name='country_currency']").send_keys("Renminbi")
        setup.find_element(By.CSS_SELECTOR, "input[name='video']").send_keys("https://www.youtube.com/watch?v=vusOqZBKwek")
        setup.find_element(By.XPATH, "//input[@name='book']").send_keys("https://www.booking.cn/searchresults.en-gb.html?ss=china&ssne=Egypt&ssne_untouched=Egypt&label=gog235jc-1DCAEoggI46AdIM1gDaGqIAQGYAQG4ARfIAQzYAQPoAQGIAgGoAgO4ApTfhKAGwAIB0gIkMTc2NWViN2MtZGQxNS00ODMzLTg1YWUtMTBhMWI5MzYwMDZh2AIE4AIB&sid=f6c61854a2708dbd0802c8f63668bdc4&aid=397594&lang=en-gb&sb=1&src_elem=sb&src=searchresults&checkin=2023-03-06&checkout=2023-03-10&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure")
        setup.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        setup.find_element(By.XPATH, "//input[@name='search_string']").send_keys("China")
        setup.find_element(By.CSS_SELECTOR, "button[value='search']").click()
        setup.find_element(By.XPATH, "//img[@alt='good']")
        assert setup.find_element(By.XPATH, "//img[@alt='good']").is_displayed(), "The image is already exists, change the image "
        print("Passed!")

    def test_capital_name(self, setup):
        log = self.getLogger()
        log.warning("Something is in warning mode")
        setup.find_element(By.CSS_SELECTOR, "a[href='/add_data']").click()
        setup.find_element(By.XPATH, "//input[@name='filename']").send_keys(
            "C://Users//windows11//Desktop//project 2//country//images.jpeg")
        setup.find_element(By.CSS_SELECTOR, "input[name='country_name']").send_keys("example capital")
        setup.find_element(By.CSS_SELECTOR, "input[name='capital_name']").send_keys("cairo")
        setup.find_element(By.XPATH, "//input[@name='official_language']").send_keys("Standard Chinese")
        setup.find_element(By.XPATH, "//input[@name='country_currency']").send_keys("Renminbi")
        setup.find_element(By.CSS_SELECTOR, "input[name='video']").send_keys(
                "https://www.youtube.com/watch?v=vusOqZBKwek")
        setup.find_element(By.XPATH, "//input[@name='book']").send_keys(
                "https://www.booking.cn/searchresults.en-gb.html?ss=china&ssne=Egypt&ssne_untouched=Egypt&label=gog235jc-1DCAEoggI46AdIM1gDaGqIAQGYAQG4ARfIAQzYAQPoAQGIAgGoAgO4ApTfhKAGwAIB0gIkMTc2NWViN2MtZGQxNS00ODMzLTg1YWUtMTBhMWI5MzYwMDZh2AIE4AIB&sid=f6c61854a2708dbd0802c8f63668bdc4&aid=397594&lang=en-gb&sb=1&src_elem=sb&src=searchresults&checkin=2023-03-06&checkout=2023-03-10&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure")

        setup.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        setup.find_element(By.XPATH, "//input[@name='search_string']").send_keys("example capital")

        setup.find_element(By.CSS_SELECTOR, "button[value='search']").click()
        setup.find_element(By.XPATH, "//img[@alt='good']")
        assert setup.find_element(By.XPATH,
                                       "//img[@alt='good']").is_displayed(), "The Capital name is already exists, change the capital name "
        print("Error!The Capital name is already exists")


def test_crossBrowser(crossBrowser):
    print(crossBrowser)



