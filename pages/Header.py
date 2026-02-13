from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time

class HeaderAnon:
    EN = {
        "elements": {
            "buttons": {
                "sign_in": "btn-login"
            }
        },
        "paths": {
            "buttons": {
                "sign_in": "/en/login"
            }
        }
    }

    FR = {
        "elements": {
            "buttons": {
                "sign_in": "btn-login"
            }
        },
        "paths": {
            "buttons": {
                "sign_in": "/fr/login"
            }
        }
    }

class HeaderAuth:
    EN = {
        "elements": {
            "buttons": {
                "menu": "nav-account-toggle",
                "sign_out": "[aria-label=\"Sign out\"]"
            }
        },
        "paths": {
        }
    }

    FR = {
        "elements": {
            "buttons": {
                "menu": "nav-account-toggle",
                "sign_out": ""
            }
        },
        "paths": {
        }
    }

class HeaderCustomerPortal:
    EN = {
        "elements": {
            "buttons": {
                "menu": "nav-account-toggle",
                "sign_out": "[aria-label=\"Sign out\"]"
            }
        },
        "paths": {
        }
    }

    FR = {
        "elements": {
            "buttons": {
                "menu": "nav-account-toggle",
                "sign_out": ""
            }
        },
        "paths": {
        }
    }

class Header:
    DOMAIN_MAP = {
        "homeweb": {"AUTH": HeaderAuth, "ANON": HeaderAnon},
        "customer_portal": {"AUTH": HeaderCustomerPortal, "ANON": HeaderAnon},
        "quantum_api": {"AUTH": HeaderAuth, "ANON": HeaderAnon},  # adjust if needed
    }

    def __init__(self,  driver, domain="homeweb", lang="EN", user="ANON"):
        self.driver = driver
        self.lang = lang
        self.wait = WebDriverWait(driver, 10)
        self.type = HeaderAuth if user == "AUTH" else HeaderAnon
        self.domain = domain.lower()
        self.user = user.upper()

        domain_class = self.DOMAIN_MAP[self.domain][self.user]

        self.elements = domain_class.EN["elements"] if lang == "EN" else domain_class.FR["elements"]
        self.paths = domain_class.EN.get("paths", {}) if lang == "EN" else domain_class.FR.get("paths", {})
        # self.elements = self.type.EN["elements"] if lang == "EN" else self.type.FR["elements"]
        # self.paths = self.type.EN["paths"] if lang == "EN" else self.type.FR["paths"]

    def click_element(self, by, locator):
        # 1: Find element
        element = self.wait.until(
            expected_conditions.element_to_be_clickable((by, locator))
        )

        # 2: Scroll element into view and click
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

        # 3: Wait for layout to stabilize
        self.wait.until(
            lambda d: element.is_displayed() and element.is_enabled()
        )

        # 4: Small pause to allow any final reflows
        time.sleep(0.5)

        # 5: Click
        element.click()

    def wait_for_account_menu(self):
        return self.wait.until(
            lambda d: d.find_element("css selector", "div.dropdown-menu.dropdown-account.show")
        )

    def wait_for_insights_dropdown(self):
        return self.wait.until(
            lambda d: d.find_element("css selector", "ul.dropdown-menu.dropdown-insights.show")
        )

