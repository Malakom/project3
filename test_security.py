import pytest
import time
from selenium.webdriver.common.by import By
from BaseClass import BaseClass


@pytest.mark.Security
@pytest.mark.usefixtures("setup")
class Test_security(BaseClass):
    def test_login(self, setup):
        log = self.getLogger()
        log.info("log-in statement")
        setup.find_element(By.CSS_SELECTOR, "a[href='/open_login']").click()
        setup.find_element(By.XPATH, "//input[@placeholder='Name']").send_keys("Omar")
        setup.find_element(By.XPATH, "//input[@placeholder='password']").send_keys("102030")
        setup.find_element(By.XPATH, "//input[@value='Log-in']").click()
        msg = setup.find_element(By.XPATH, "//h1[normalize-space()='Not Found']").text
        assert "Not Found" in msg, "page not founded"
        print("Passed")


    def test_send_msg(self, setup):
        log = self.getLogger()
        log.info("sending message")
        setup.find_element(By.CSS_SELECTOR, "a[href='/contact']").click()
        setup.find_element(By.XPATH, "//input[@placeholder='Enter your name']").send_keys("Malak")
        setup.find_element(By.CSS_SELECTOR, "input[placeholder='Enter your email']").send_keys(
            "Malak2021994@gmail.com")
        setup.find_element(By.CSS_SELECTOR, "input[placeholder='Enter your message']").send_keys(
            "I want to send  me information about Egypt")
        setup.find_element(By.XPATH, "//input[@value='Send Now']").click()
        time.sleep(1)
        assert setup.find_element(By.XPATH, "//input[@value='Send Now']").is_displayed(), "The message not sending"
        print("The message is send")

    def test_review_no_rating(self, setup):
        log = self.getLogger()
        log.debug("a debug statement is executed")
        setup.find_element(By.XPATH, "//input[@name='search_string']").send_keys("france")
        time.sleep(1)
        setup.find_element(By.CSS_SELECTOR, "button[value='search']").click()
        setup.find_element(By.XPATH, "//img[@alt='good']").click()
        setup.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Raed")
        setup.find_element(By.XPATH, "//textarea[@name='review_text']").send_keys("Nice")
        time.sleep(5)
        element = setup.find_element(By.ID, "review_add")
        setup.execute_script("arguments[0].scrollIntoView()", element)
        time.sleep(7)
        element.click()
        assert setup.find_element(By.XPATH, "//div[@class='body-review']").is_displayed(), "Error, add rating"
        print("The review is added")

    def test_format(self,setup):
        log = self.getLogger()
        log.critical("Critical issue")
        # click on add page
        setup.find_element(By.CSS_SELECTOR, "a[href='/add_data']").click()
        # upload image
        setup.find_element(By.XPATH, "//input[@name='filename']").send_keys(
            "C://Users//windows11//Desktop//project 2//country//format.webp")
        # upload data of country:(name, capital name, official language,country currency)
        setup.find_element(By.CSS_SELECTOR, "input[name='country_name']").send_keys("image")
        setup.find_element(By.CSS_SELECTOR, "input[name='capital_name']").send_keys("Ankra")
        setup.find_element(By.XPATH, "//input[@name='official_language']").send_keys("T")
        setup.find_element(By.XPATH, "//input[@name='country_currency']").send_keys("TU")
        # short video for 10 beste places in country
        setup.find_element(By.CSS_SELECTOR, "input[name='video']").send_keys(
            "https://www.youtube.com/embed/zS4AP0Q8L8g")
        # link for booking website
        setup.find_element(By.XPATH, "//input[@name='book']").send_keys(
            "https://www.booking.cn/searchresults.en-gb.html?ss=Italy&ssne=China&ssne_untouched=China&label=gog235jc-1DCAEoggI46AdIM1gDaGqIAQGYAQG4ARfIAQzYAQPoAQGIAgGoAgO4ApTfhKAGwAIB0gIkMTc2NWViN2MtZGQxNS00ODMzLTg1YWUtMTBhMWI5MzYwMDZh2AIE4AIB&sid=f6c61854a2708dbd0802c8f63668bdc4&aid=397594&lang=en-gb&sb=1&src_elem=sb&src=searchresults&dest_id=104&dest_type=country&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=9054065ed8cd006a&ac_meta=GhA5MDU0MDY1ZWQ4Y2QwMDZhIAAoATICZW46BGl0YWxAAEoAUAA%3D&checkin=2023-03-06&checkout=2023-03-10&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure")
        time.sleep(1)
        # add
        setup.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(3)
        # search for the new country
        setup.find_element(By.XPATH, "//input[@name='search_string']").send_keys("image")
        time.sleep(1)
        setup.find_element(By.CSS_SELECTOR, "button[value='search']").click()
        setup.find_element(By.XPATH, "//img[@alt='good']")
        name = setup.find_element(By.CSS_SELECTOR, ".card-title").text
        assert name == "image", "Error, the country not upload "
        print("Passed, no image")



    def test_delete_same_image(self, setup):
        log = self.getLogger()
        log.debug("a debug statement is executed")
        # same image for china and thailand, test if the image of thailand is deleted
        # deleted China
        setup.find_element(By.XPATH, "//input[@name='search_string']").send_keys("China")
        time.sleep(1)
        setup.find_element(By.CSS_SELECTOR, "button[value='search']").click()
        setup.find_element(By.XPATH, "//img[@alt='good']").click()
        time.sleep(3)
        setup.find_element(By.XPATH, "//i[@id='delete']").click()

        # test if the image of thailand is deleted
        setup.find_element(By.XPATH, "//input[@name='search_string']").send_keys("greece")
        time.sleep(1)
        setup.find_element(By.CSS_SELECTOR, "button[value='search']").click()
        setup.find_element(By.XPATH, "//img[@alt='good']").click()
        time.sleep(3)
        setup.find_element(By.XPATH, "//i[@id='delete']").click()
        assert setup.find_element(By.XPATH, "//input[@name='search_string']").is_displayed(), "Passed"
        print("The image is deleted")


def test_crossBrowser(crossBrowser):
    print(crossBrowser)
