"""
Testcase-ID : TC_PIM_01
Add a new employee in the PIM module of OrangeHRM Portal
"""

# Importing necessary modules and classes from Selenium and pytest
from Data import data
from Locators import locator
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
import pytest

# Defining a test class


class Test:
    dashboard = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"

    # pytest fixture for setting up the test environment
    @pytest.fixture
    def boot(self):
        # Setting up Chrome WebDriver with the WebDriver Manager
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        yield
         # implementation of implicit wait
       self.driver.implicitly_wait(10)
        self.driver.quit()

    @pytest.mark.html
    def test_login(self, boot):
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
           print("successfully logged into the webpage of OrangeHRM")

           # Use the some method from the 'WebLocators' class to locate and click on a link with the specified text (e.g., 'PIM')

           locator.WebLocators().link_text(self.driver, locator.WebLocators().pimLocator)
           locator.WebLocators().clickbutton(self.driver, locator.WebLocators().addLocator)
           locator.WebLocators().x_path(self.driver, locator.WebLocators().emp_fn_Locator,
                                        data.WebData().emp_firstname)
           locator.WebLocators().x_path(self.driver, locator.WebLocators().emp_ln_locator,
                                          data.WebData().emp_lastname)
           locator.WebLocators().x_path(self.driver, locator.WebLocators().emp_id_locator, data.WebData().emp_id)
           locator.WebLocators().clickbutton(self.driver, locator.WebLocators().saveLocator)
          # Print a message indicating that new Employee personal details have been successfully added in the PIM module
           print("successfully added new Employee personal details in PIM module")
     except NoSuchElementException as e:
           print("error")









