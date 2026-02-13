from selenium.webdriver.support.wait import WebDriverWait

from pages.Header import Header
from selenium.webdriver.support import expected_conditions


class CustomerPortal:
    # Properties
    @property
    def title(self):
        return self.driver.title

    @property
    def current_url(self):
        return self.driver.current_url

    def __init__(self, driver, lang="EN"):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)
        self.lang = lang
        # self.header = Header()
        # self.header = HeaderCustomerPortal.EN if lang == "EN" else HeaderCustomerPortal.FR
        self._is_authenticated = False
        self.header = None
        self.update_header()

    def update_header(self):
        user_type = "AUTH" if self._is_authenticated else "ANON"
        self.header = Header(self.driver, domain="customer_portal", lang=self.lang, user=user_type)

    def set_authenticated(self, value):
        self._is_authenticated = value
        self.update_header()

    def is_authenticated(self):
        return self._is_authenticated

    def wait_for_portal_login(self):
        return self.wait.until(
            lambda d: "portal.homewoodhealth" in d.current_url.lower() and "/app/en" in d.current_url.lower()
        )

    # def wait_for_insights_load(self):
    #     # 1: Locate embed container
    #     self.wait.until(
    #         expected_conditions.presence_of_element_located(("id", "embedContainer"))
    #     )
    #
    #     # 2: Locate iframe
    #     iframe = self.wait.until(
    #         expected_conditions.presence_of_element_located(("tag name", "iframe"))
    #     )
    #
    #     # 3: Switch to the iframe to interact with elements inside it
    #     self.driver.switch_to.frame(iframe)
    #
    #     # 4: Wait until iframe DOM is fully ready
    #     return self.wait.until(
    #         lambda d: d.execute_script("return document.readyState") == "complete"
    #     )

    def wait_for_insights_load(self):
        # 1: Locate embed container
        self.wait.until(
            expected_conditions.presence_of_element_located(("id", "embedContainer"))
        )

        # 2: Locate iframe
        iframe = self.wait.until(
            expected_conditions.presence_of_element_located(("tag name", "iframe"))
        )

        # 3: Switch to the iframe to interact with elements inside it
        self.driver.switch_to.frame(iframe)

        # 4: Wait until iframe DOM is fully ready
        self.wait.until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

        # 5: Wait for Power BI spinners to disappear (all visuals finish loading)
        self.wait.until(
            expected_conditions.invisibility_of_element_located(
                ("css selector", "spinner[localize-tooltip='Visual_Loading_AlertText']")
            )
        )

        # 6: Verify report container is visible
        self.wait.until(
            expected_conditions.visibility_of_element_located(
                ("css selector", "report-embed")
            )
        )

        # 7: Ensure at least one visual is initialized
        self.wait.until(
            expected_conditions.presence_of_all_elements_located(
                ("css selector", "[initialized='true']")
            )
        )

        return True

    # def powerbi_loaded(driver):
    #     spinners = self.driver.find_elements(By.CSS_SELECTOR, "spinner[title='Visuals are loading...']")
    #
    #     # loaded = visuals exist AND no spinner visible
    #     return len(visuals) > 0 and len(spinners) == 0
    #
    # def wait_for_insights_load(self):
    #     self.wait.until(lambda d: d.find_element(By.ID, "embedContainer"))
    #
    #     iframe = self.wait.until(lambda d: d.find_element(By.TAG_NAME, "iframe"))
    #     self.driver.switch_to.frame(iframe)
    #
    #     return self.wait.until(self.powerbi_loaded())
