import logging
from BaseClass import BaseClass
from conftest import *
import pytest

@pytest.mark.Acceptance
@pytest.mark.usefixtures("setup")
class Test_Add_Game(BaseClass):
    def test_Add_game_func(self, setup):
        driver = setup
        driver.get("http://127.0.0.1:5000/")
        driver.find_element(By.XPATH, "//button[normalize-space()='ADD GAME']").click()
        driver.find_element(By.XPATH, "//input[@name='filename']").send_keys("C:/Users/DELL/Desktop/PS4 - MORTAL KOMBAT X")
        driver.find_element(By.XPATH, "//input[@name='Game_title']").send_keys("PS4 - MORTAL KOMBAT X")
        driver.find_element(By.XPATH, "//textarea[@name='description']").send_keys("A fight game . very interesting game ")
        driver.find_element(By.XPATH, "//input[@name='age']").send_keys("+18")
        driver.find_element(By.XPATH, "//input[@name='price']").send_keys("120")
        driver.find_element(By.XPATH, "//input[@name='online_play']").send_keys("No")
        driver.find_element(By.XPATH, "//input[@name='multiplayer']").send_keys("Yes")
        driver.find_element(By.XPATH, "//button[normalize-space()='Add']").click()
        driver.get_screenshot_as_file("A new game Added")
        log = self.getLogger()
        log.info("YOUR TEST IS SUCCESS")

        def test_button(self,setup):
            driver = setup
            driver.get("http://127.0.0.1:5000/")
            AddGameButton = driver.find_element(By.XPATH, "//button[normalize-space()='ADD GAME']").text
            assert AddGameButton == "ADD GAME", "Failed, the button is not add game "
            print("The sentence of the button is Add game ")

