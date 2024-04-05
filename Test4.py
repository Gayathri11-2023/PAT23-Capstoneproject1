"""
Testcase-ID : TC_PIM_02
Edit the existing employee in the PIM module
"""
from Data import data
from Locators import locator
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import pytest


# Defining a test class


class Testcase4:
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
    def test_editingemp(self, boot):
        try:
           # Opening the specified URL in the browser
           self.driver.get(data.WebData().url)
           # Maximizing the browser window
           self.driver.maximize_window()
           locator.WebLocators().entertext(self.driver, locator.WebLocators().usernameLocator, data.WebData().username)
           locator.WebLocators().entertext(self.driver, locator.WebLocators().passwordLocator,
                                        data.WebData().password)
           locator.WebLocators().clickbutton(self.driver, locator.WebLocators().buttonLocator)
           assert (self.driver.current_url == self.dashboard)
           print("successfully logged into the webpage of OrangeHRM")
           locator.WebLocators().link_text(self.driver, locator.WebLocators().pimLocator)
           locator.WebLocators().clickbutton(self.driver, locator.WebLocators().editLocator)
            
           # locate the element, select the text, delete the text and insert the new text for employee first name , last name and id
           emp_firstname = self.driver.find_element(by=By.XPATH, value=locator.WebLocators().employeefirstnamelocator)
           emp_firstname.send_keys(Keys.CONTROL + 'a')
           emp_firstname.send_keys(Keys.DELETE)
           emp_firstname.send_keys(data.WebData().employeefirstname)
           emp_lastname = self.driver.find_element(by=By.XPATH, value=locator.WebLocators().employeelastnamelocator)
           emp_lastname.send_keys(Keys.CONTROL + 'a')
           emp_lastname.send_keys(Keys.DELETE)
           emp_lastname.send_keys(data.WebData().employeelastname)
           emp_id = self.driver.find_element(by=By.XPATH,
                                          value=locator.WebLocators().empidlocator)
           emp_id.send_keys(Keys.CONTROL + 'a')
           emp_id.send_keys(Keys.DELETE)
           emp_id.send_keys(data.WebData().empid)
           click_button = self.driver.find_element(by=By.XPATH, value=locator.WebLocators().savebuttonLocator)
           click_button.click()
           # print the retrived message from that page
           print("Successfully edited existing employee information in PIM module")
    except NoSuchElementException as e:
          print("Error")
        








