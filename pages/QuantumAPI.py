from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pages.Login import LoginPage


class QuantumAPI:
    URL = "https://api.homewoodhealth.io/en/login"

    def __init__(self, driver, lang="EN"):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.login = LoginPage.EN if lang == "EN" else LoginPage.FR

    def open(self):
        self.driver.get(self.URL)

    def input(self, input_identifier, input_value):
        email_input = self.wait.until(
            expected_conditions.visibility_of_element_located((By.XPATH, input_identifier))
        )
        email_input.clear()
        email_input.send_keys(input_value)
        next_button = self.wait.until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.login["elements"]["buttons"]["next"]))
        )
        next_button.click()

    def enter_password(self, password: str):
        password_input = self.wait.until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.login["elements"]["inputs"]["password"]))
        )
        password_input.clear()
        password_input.send_keys(password)
        submit_button = self.wait.until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.login["elements"]["buttons"]["next"]))
        )
        submit_button.click()


    def is_logged_in(self):
        # Adjust this to check what indicates a successful login, e.g., URL or element
        return "dashboard" in self.driver.current_url.lower()


