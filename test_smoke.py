import pytest
from selenium.webdriver.support import expected_conditions
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from BaseClass import BaseClass



@pytest.mark.smoke
@pytest.mark.usefixtures("setup")
class Test_country(BaseClass):
    def test_add_country(self, setup):
        log = self.getLogger()
        log.critical("Critical issue")
        #click on add page
        setup.find_element(By.CSS_SELECTOR, "a[href='/add_data']").click()
        #upload image
        setup.find_element(By.XPATH, "//input[@name='filename']").send_keys(
            "C://Users//windows11//Desktop//project 2//country//italy.jpeg")
        #upload data of country:(name, capital name, official language,country currency)
        setup.find_element(By.CSS_SELECTOR, "input[name='country_name']").send_keys("Italy")
        setup.find_element(By.CSS_SELECTOR, "input[name='capital_name']").send_keys("Rome")
        setup.find_element(By.XPATH, "//input[@name='official_language']").send_keys("Italian")
        setup.find_element(By.XPATH, "//input[@name='country_currency']").send_keys("Euro")
        #short video for 10 beste places in country
        setup.find_element(By.CSS_SELECTOR, "input[name='video']").send_keys(
            "https://www.youtube.com/embed/zS4AP0Q8L8g")
        #link for booking website
        setup.find_element(By.XPATH, "//input[@name='book']").send_keys(
            "https://www.booking.cn/searchresults.en-gb.html?ss=Italy&ssne=China&ssne_untouched=China&label=gog235jc-1DCAEoggI46AdIM1gDaGqIAQGYAQG4ARfIAQzYAQPoAQGIAgGoAgO4ApTfhKAGwAIB0gIkMTc2NWViN2MtZGQxNS00ODMzLTg1YWUtMTBhMWI5MzYwMDZh2AIE4AIB&sid=f6c61854a2708dbd0802c8f63668bdc4&aid=397594&lang=en-gb&sb=1&src_elem=sb&src=searchresults&dest_id=104&dest_type=country&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=9054065ed8cd006a&ac_meta=GhA5MDU0MDY1ZWQ4Y2QwMDZhIAAoATICZW46BGl0YWxAAEoAUAA%3D&checkin=2023-03-06&checkout=2023-03-10&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure")
        time.sleep(1)
        #add
        setup.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(3)
        #search for the new country
        setup.find_element(By.XPATH, "//input[@name='search_string']").send_keys("Italy")
        time.sleep(1)
        setup.find_element(By.CSS_SELECTOR, "button[value='search']").click()
        setup.find_element(By.XPATH, "//img[@alt='good']")
        name = setup.find_element(By.CSS_SELECTOR, ".card-title").text
        assert name == "Italy", "Error, the country not upload "
        print("Passed")


    def test_delete_country(self, setup):
        log = self.getLogger()
        log.critical("Critical issue")
        setup.find_element(By.XPATH, "//input[@name='search_string']").send_keys("Turkey")
        setup.find_element(By.CSS_SELECTOR, "button[value='search']").click()
        setup.find_element(By.XPATH, "//img[@alt='good']").click()
        setup.find_element(By.CSS_SELECTOR, "#delete").click()
        setup.find_element(By.XPATH, "//input[@name='search_string']").send_keys("Turkey")
        setup.find_element(By.CSS_SELECTOR, "button[value='search']").click()
        assert setup.find_element(By.XPATH, "//img[@alt='good']").is_displayed(), "Error, the country not upload "
        print("Passed")

    def test_add_review(self, setup):
        log = self.getLogger()
        log.critical("Critical issue")
        setup.find_element(By.XPATH, "//input[@name='search_string']").send_keys("Emirates")
        time.sleep(5)
        setup.find_element(By.CSS_SELECTOR, "button[value='search']").click()
        time.sleep(5)
        setup.find_element(By.XPATH, "//img[@alt='good']").click()
        time.sleep(5)
        setup.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Raed")
        time.sleep(5)
        setup.find_element(By.XPATH, "//textarea[@name='review_text']").send_keys("like")
        time.sleep(15)
        setup.find_element(By.CSS_SELECTOR, "label[title='Very good']").click()
        setup.execute_script("window.scrollBy(0, 500)")
        wait = WebDriverWait(setup, 10)
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[@id='review_add']")))
        setup.find_element(By.XPATH, "//button[@id='review_add']").click()
        review = setup.find_element(By.XPATH, "//div//div[@class='body-review']")
        assert review.is_displayed(), "Error, the review not added"
        print("The review is added")


    def test_search_country(self, setup):
        log = self.getLogger()
        log.critical("Critical issue")
        setup.find_element(By.XPATH, "//input[@name='search_string']").send_keys("Egypt")
        time.sleep(1)
        setup.find_element(By.CSS_SELECTOR, "button[value='search']").click()
        name = setup.find_element(By.CSS_SELECTOR, ".card-title").text
        assert name == "Egypt", "Error, the country not upload "
        print("Passed")

    def test_change_img(self, setup):
        log = self.getLogger()
        log.critical("Critical issue")
        setup.find_element(By.XPATH, "//input[@name='search_string']").send_keys("France")
        setup.find_element(By.CSS_SELECTOR, "button[value='search']").click()
        setup.find_element(By.XPATH, "//img[@alt='good']").click()
        setup.find_element(By.XPATH, "//i[@id='alter']").click()
        setup.find_element(By.XPATH, "//input[@name='filename']").send_keys(
            "C://Users//windows11//Desktop//project 2//country//france.jpeg")
        setup.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        assert setup.find_element(By.CSS_SELECTOR, "button[type='submit']").is_selected(), "Must add country currency!! "
        print("Passed")


def test_crossBrowser(crossBrowser):
    print(crossBrowser)

