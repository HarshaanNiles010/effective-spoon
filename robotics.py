import sys

from selenium import webdriver
from datetime import datetime
from exception import CustomException
from RPA.Browser.Selenium import Selenium as ChromeBrowser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

br = ChromeBrowser()


class Robot:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Hello, my name is " + self.name)
        print("I am a robot and I can look up birth date, death date, age of the scientist and little bit about them "
            "and their achievments")

    def say_goodbye(self):
        print("Goodbye, my name is " + self.name)

    def open_webpage(self, webpage):
        br.open_available_browser(webpage)

    def lookup(self, name):
        # lookup the name on wikipedia
        print(f"Looking up the scientist by the name of: {name}")
        #use the selenium web driver to open wikipedia and gather information
        driver = webdriver.Chrome()
        driver.get(
            f"https://en.wikipedia.org/wiki/{name.replace(' ','_')}")
        try:
            # wait for everything to load up
            birth_date_el = WebDriverWait(driver,10).until(
                EC.presence_of_element_located(
                    # use the css selector to find and pull out the required element
                    (By.CSS_SELECTOR,"span.bday"))
                )
            # get the birth date from the element pulled earlier
            birth_date = birth_date_el.get_attribute("innerText")

            # wait in case of change to the web browser and pull the required element
            death_date_el = WebDriverWait(driver,10).until(
                EC.presence_of_element_located(
                    # use xpath to find the right elemenet
                    (By.XPATH,"//th[contains(text(), 'Died')]/following-sibling::td//span"))
                )
            # get the death date from the element pulled from wikipedia earlier
            death_date = death_date_el.get_attribute("innerText").replace("(","").replace(")","")

            # convert the birth date to a date time object
            born = datetime.strptime(birth_date, '%Y-%m-%d')
            # convert the death date to a date time object
            died = datetime.strptime(death_date,'%Y-%m-%d')
            # find the age at time of death in days
            age = int((died - born).days/365.25)

            # Take the summary from the wikipedia article
            summary = WebDriverWait(driver,10).until(
                EC.presence_of_element_located(
                # use xptath to get the summary and then convert it into text at the end 
                    (By.XPATH,"(//div[@id='mw-content-text']/div/p[not(@class='mw-empty-elt')])[1]"))
                ).text
        
            scientist_info = {
                "Name": name,
                "Birth Date": birth_date,
                "Death Date": death_date,
                "Age": age,
                "Summary": summary
                }  
            for key, value in scientist_info.items():
                    print(f"{key}: {value}")
            
        except Exception as e:
            raise CustomException(e,sys)
