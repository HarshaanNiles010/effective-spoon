from RPA.Browser.Selenium import Selenium

br = Selenium()


class Robot:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Hello, my name is " + self.name)
        print("I am a robot and I can look up birth date, death date, age of the scintist and little bit about them "
            "and their achievments")

    def say_goodbye(self):
        print("Goodbye, my name is " + self.name)

    def open_webpage(self, webpage):
        br.open_available_browser(webpage)

    def lookup(self, name):
        # lookup the name on wikipedia
        print(f"Looking up the scientist by the name of: {name}")
