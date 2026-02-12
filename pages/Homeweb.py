from pages.Landing import LandingPage
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class Homeweb:
    # Properties
    @property
    def title(self):
        return self.driver.title

    @property
    def current_url(self):
        return self.driver.current_url

    def __init__(self, driver, lang="EN"):
        self.driver = driver
        self.lang = lang
        self.landing = LandingPage.EN if lang == "EN" else LandingPage.FR

    # Methods
    def navigate_landing(self):
        url = self.landing["base_url"]
        self.driver.get(url)

    def click_element(self, by, locator):
        # 1: Find element
        element = WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located((by, locator))
        )

        # 2: Scroll element into view and click
        ActionChains(self.driver).move_to_element(element).click().perform()

    def go_back(self):
        self.driver.back()
        WebDriverWait(self.driver, 5).until(
            lambda d: "homeweb.ca" in d.current_url
        )
        self.driver.execute_script("window.scrollBy(0, 0);")

