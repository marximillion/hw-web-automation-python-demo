# Test Suite: Build Acceptance
from dotenv import load_dotenv
import os

# Set up Credentials
load_dotenv()  # loads variables from .env
CREDENTIALS = {
    "personal": {
        "email": os.getenv("PERSONAL_EMAIL"),
        "password": os.getenv("PERSONAL_PASSWORD")
    },
    "demo": {
        "email": os.getenv("DEMO_EMAIL"),
        "password": os.getenv("DEMO_PASSWORD")
    },
}

def test_bat_web_001(homeweb):
    # 1: Navigate to Homeweb landing
    homeweb.navigate_landing()
    homeweb.set_landing(True)
    assert "homeweb" in homeweb.current_url.lower()
    assert homeweb.title

def test_bat_web_002(homeweb):
    assert homeweb.is_landing()

    # 1: Set up
    resources = homeweb.landing["elements"]["resources"]
    paths = homeweb.landing["paths"]["resources"]

    # 2: Test - Resource 1
    homeweb.click_element("xpath", resources["emotional_intelligence"])
    assert paths["emotional_intelligence"] in homeweb.current_url.lower()
    assert homeweb.wait_for_resource_content()
    homeweb.go_back()

    # 3: Test - Resource 2
    homeweb.click_element("xpath", resources["anxiety"])
    assert paths["anxiety"] in homeweb.current_url.lower()
    assert homeweb.wait_for_resource_content()
    homeweb.go_back()

    # 4: Test - Resource 3
    homeweb.click_element("xpath", resources["letting_go"])
    assert paths["letting_go"] in homeweb.current_url.lower()
    assert homeweb.wait_for_resource_content()
    homeweb.go_back()

    # 5: Test - Resource 4
    homeweb.click_element("xpath", resources["toolkit"])
    assert paths["toolkit"] in homeweb.current_url.lower()
    assert homeweb.wait_for_resource_content()
    homeweb.go_back()

def test_bat_web_003(homeweb, quantum):
    assert homeweb.is_landing()

    # 1: Set up
    buttons = homeweb.landing["elements"]["buttons"];
    paths = homeweb.landing["paths"]["buttons"];
    inputs = quantum.login["elements"]["inputs"]

    # 2: Test - Sign In
    homeweb.click_element("xpath", buttons["sign_in"])
    assert paths["sign_in"] in quantum.current_url.lower()

    # 3: Test - Email field
    quantum.input(inputs["email_address"], CREDENTIALS["personal"]["email"])
    quantum.submit()
    password_input = quantum.wait_for_password()
    assert password_input.is_displayed()

    # 4: Test - Password field
    quantum.input(inputs["password"], CREDENTIALS["personal"]["password"])
    quantum.submit()

    # 5: Test - Login
    homeweb.wait_for_dashboard()
    assert "homeweb" in homeweb.current_url.lower()
    assert "/app/en/homeweb/dashboard" in homeweb.current_url.lower()

    homeweb.set_authenticated(True)

def test_bat_web_004(homeweb):
    assert homeweb.is_authenticated

    resource_target = "https://homeweb.ca/en/user/articles/56252b81e40e6f50062aa714"
    homeweb.driver.get(resource_target)
    assert homeweb.wait_for_resource_content()

# TODO: BAT-WEB-005
def test_bat_web_005(homeweb):
    assert homeweb.is_authenticated

# TODO: BAT-WEB-006
# TODO: BAT-WEB-007
# TODO: BAT-WEB-008
# TODO: BAT-WEB-009
# TODO: BAT-WEB-010
# TODO: BAT-WEB-011