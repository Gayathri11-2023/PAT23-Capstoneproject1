"""
Testcase-ID : TC_Login_02
Unsuccessful Employee login into OrangeHRM Portal
"""

# Importing necessary modules and classes from Selenium and pytest
from Data import data
from Locators import locator
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
import pytest

from time import sleep

# Defining a test class


class Test:
    dashboard = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"

    # pytest fixture for setting up the test environment
    @pytest.fixture
    def boot(self):
        # Setting up Chrome WebDriver with the WebDriver Manager
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        yield
        self.driver.quit()

    @pytest.mark.html
    def test_login(self, boot):
        # Opening the specified URL in the browser
        self.driver.get(data.WebData().url)
        # Maximizing the browser window
        self.driver.maximize_window()
        # Introducing a sleep delay for 7 seconds
        sleep(7)

        # Call the 'entertext' and 'clickbutton' method from the 'WebLocators' class to
        # enter text into a username field , Password field and login button

        locator.WebLocators().entertext(self.driver, locator.WebLocators().usernameLocator, data.WebData().username)
        locator.WebLocators().entertext(self.driver, locator.WebLocators().passwordLocator, data.WebData().wrongpassword)
        locator.WebLocators().clickbutton(self.driver, locator.WebLocators().buttonLocator)
        sleep(2)
        assert (self.driver.current_url != data.WebData().dashboardURL)

        # Print a success message indicating that login was successful, along with the username and password used
        print(f"UNSUCCESSFUL : Logged in with {data.WebData().username} and the password is {data.WebData().wrongpassword}")
        print("Test Case-2 : Valid username and Wrong password is evaluated")


