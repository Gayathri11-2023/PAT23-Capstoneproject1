"""
Testcase-ID : TC_PIM_03
Delete the existing employee in the PIM module
"""

from Data import data
from Locators import locator
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
import pytest


# Defining a test class
class Testcase5:
    dashboard = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"

    # pytest fixture for setting up the test environment
    @pytest.fixture
    def boot(self):
        # Setting up Chrome WebDriver with the WebDriver Manager
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        yield
          # implementation of implicit wait
       self.driver.implicitly_wait(10
        self.driver.quit()

    @pytest.mark.html
    def test_deleteemp(self, boot):
        try:
           # Opening the specified URL in the browser
           self.driver.get(data.WebData().url)
           # Maximizing the browser window
           self.driver.maximize_window()
        
           # Call the 'entertext' and 'clickbutton' method from the 'WebLocators' class to
           # enter text into a username field , Password field and login button

           locator.WebLocators().entertext(self.driver, locator.WebLocators().usernameLocator, data.WebData().username)
           locator.WebLocators().entertext(self.driver, locator.WebLocators().passwordLocator,
                                        data.WebData().password)
           locator.WebLocators().clickbutton(self.driver, locator.WebLocators().buttonLocator)
           assert (self.driver.current_url == self.dashboard)
           print("Successfuly logged into the webpage of OrangeHRM")

           # Use the some method from the 'WebLocators' class to locate and click on a link with the specified text (e.g., 'PIM')

           locator.WebLocators().link_text(self.driver, locator.WebLocators().pimLocator)
           locator.WebLocators().clickbutton(self.driver,locator.WebLocators().deleteLocator)
           locator.WebLocators().clickbutton(self.driver, locator.WebLocators().yesbuttonLocator)
           # print the message Deleted
           print("Successful: Deleted existing employee record")
           print("Successfully deleted existing employee information in PIM module")
      except NoSuchElemetExcption as e:
           print("Error")


