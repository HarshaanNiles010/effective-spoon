import sys
from robotics import Robot
from selenium import webdriver
from datetime import datetime
from exception import CustomException
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

def main():
    robot = Robot("Quandrinaut")
    introduce_yourself()
    for scientist in SCIENTISTS:
        robot.lookup(scientist,1)


if __name__ == "__main__":
    main()
