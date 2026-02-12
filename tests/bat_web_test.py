# Test Suite: Build Acceptance
def test_bat_web_001(homeweb):
    homeweb.navigate_landing()
    assert "homeweb" in homeweb.current_url.lower()
    assert homeweb.title

def test_bat_web_002(homeweb):
    resources = homeweb.landing["elements"]["resources"]
    paths = homeweb.landing["paths"]["resources"]

    homeweb.click_element("xpath", resources["emotional_intelligence"])
    assert paths["emotional_intelligence"] in homeweb.current_url.lower()
    homeweb.go_back()

    homeweb.click_element("xpath", resources["anxiety"])
    assert paths["anxiety"] in homeweb.current_url.lower()
    homeweb.go_back()

    homeweb.click_element("xpath", resources["letting_go"])
    assert paths["letting_go"] in homeweb.current_url.lower()
    homeweb.go_back()

    homeweb.click_element("xpath", resources["toolkit"])
    assert paths["toolkit"] in homeweb.current_url.lower()
    homeweb.go_back()

def test_bat_web_003(homeweb, quantum):
    buttons = homeweb.landing["elements"]["buttons"];
    paths = homeweb.landing["paths"]["buttons"];
    homeweb.click_element("xpath", buttons["sign_in"])
    assert paths["sign_in"] in homeweb.current_url.lower()

    inputs = quantum.login["elements"]["inputs"]
    quantum.input(inputs["email_address"], "mdguzman@homewoodhealth.com")
    quantum.input(inputs["password"], "Quantum123!")
    input("Press enter to continue...")

# TODO: BAT-WEB-004
# TODO: BAT-WEB-005
# TODO: BAT-WEB-006
# TODO: BAT-WEB-007
# TODO: BAT-WEB-008
# TODO: BAT-WEB-009
# TODO: BAT-WEB-010
# TODO: BAT-WEB-011