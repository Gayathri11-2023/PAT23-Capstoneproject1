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
        locator.WebLocators().entertext(self.driver, locator.WebLocators().usernameLocator, data.WebData().username)
        locator.WebLocators().entertext(self.driver, locator.WebLocators().passwordLocator,
                                        data.WebData().password)
        locator.WebLocators().clickbutton(self.driver, locator.WebLocators().buttonLocator)
        sleep(2)
        assert (self.driver.current_url == self.dashboard)
        print("successfully logged into the webpage of OrangeHRM")
        locator.WebLocators().link_text(self.driver, locator.WebLocators().pimLocator)
        sleep(2)
        locator.WebLocators().clickbutton(self.driver, locator.WebLocators().editLocator)
        sleep(2)

        # locate the element, select the text, delete the text and insert the new text for employee first name , last name and id

        emp_firstname = self.driver.find_element(by=By.XPATH, value=locator.WebLocators().employeefirstnamelocator)
        emp_firstname.send_keys(Keys.CONTROL + 'a')
        sleep(2)
        emp_firstname.send_keys(Keys.DELETE)
        emp_firstname.send_keys(data.WebData().employeefirstname)
        sleep(2)
        emp_lastname = self.driver.find_element(by=By.XPATH, value=locator.WebLocators().employeelastnamelocator)
        emp_lastname.send_keys(Keys.CONTROL + 'a')
        sleep(2)
        emp_lastname.send_keys(Keys.DELETE)
        emp_lastname.send_keys(data.WebData().employeelastname)
        sleep(2)
        emp_id = self.driver.find_element(by=By.XPATH,
                                          value=locator.WebLocators().empidlocator)
        emp_id.send_keys(Keys.CONTROL + 'a')
        sleep(2)
        emp_id.send_keys(Keys.DELETE)
        emp_id.send_keys(data.WebData().empid)
        sleep(2)
        click_button = self.driver.find_element(by=By.XPATH, value=locator.WebLocators().savebuttonLocator)
        click_button.click()
        sleep(3)
        # print the retrived message from that page
        print("Successfully edited existing employee information in PIM module")


'''      
        pim_module = self.driver.find_element(by=By.LINK_TEXT, value="PIM")
        pim_module.click()
        sleep(5)
        emp_list = self.driver.find_element(by=By.LINK_TEXT, value="Employee List")
        emp_list.click()
        sleep(2)
        edit_button = self.driver.find_element(by=By.XPATH,
                                     value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[10]/div/div[9]/div/button[2]')
        edit_button.click()
        sleep(2)
        emp_firstname = self.driver.find_element(by=By.XPATH, value="//input[@name='firstName']")
        emp_firstname.send_keys(Keys.CONTROL + 'a')
        sleep(2)
        emp_firstname.send_keys(Keys.DELETE)
        emp_firstname.send_keys("Raj")
        sleep(2)
        emp_lastname = self.driver.find_element(by=By.XPATH, value="//input[@name='lastName']")
        emp_lastname.send_keys(Keys.CONTROL + 'a')
        sleep(2)
        emp_lastname.send_keys(Keys.DELETE)
        emp_lastname.send_keys("kumar")
        sleep(2)
        emp_id = self.driver.find_element(by=By.XPATH,
                                          value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[1]/div/div[2]/input')
        emp_id.send_keys(Keys.CONTROL + 'a')
        sleep(2)
        emp_id.send_keys(Keys.DELETE)
        emp_id.send_keys("emp01")
        sleep(2)
        click_button = self.driver.find_element(by=By.XPATH, value="//button[@type='submit']")
        click_button.click()
        sleep(3)
        print("Successfully edited existing employee information in PIM module")

'''












