from robotics import Robot
from selenium import webdriver
from datetime import datetime
from RPA.Browser.Selenium import Selenium as ChromeBrowser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException



SCIENTISTS = ["Albert Einstein", "Isaac Newton", "Marie Curie", "Charles Darwin"]

robot = Robot("Quandrinaut")


def introduce_yourself():
    robot.say_hello()


def explain_yourself():
    robot.explain()

def find_information(name):
    print(name)
    driver = webdriver.Chrome()
    driver.get(
        f"https://en.wikipedia.org/wiki/{name.replace(' ','_')}")
    try:
        birth_date_el = WebDriverWait(driver,10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR,"span.bday"))
            )
        birth_date = birth_date_el.get_attribute("innerText")
        
        death_date_el = WebDriverWait(driver,10).until(
            EC.presence_of_element_located(
                (By.XPATH,"//th[contains(text(), 'Died')]/following-sibling::td//span"))
            )
        
        death_date = death_date_el.get_attribute("innerText").replace("(","").replace(")","")
        
        born = datetime.strptime(birth_date, '%Y-%m-%d')
        died = datetime.strptime(death_date,'%Y-%m-%d')
        age = int((died - born).days/365.25)
        
        summary = WebDriverWait(driver,10).until(
            EC.presence_of_element_located(
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
        print(f"An error occured while process {name}: {e}")
        
def main():
    robot = Robot("Quandrinaut")
    introduce_yourself()
    for scientist in SCIENTISTS:
        find_information(scientist)


if __name__ == "__main__":
    main()
