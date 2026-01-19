from playwright.sync_api import sync_playwright, Locator, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.set_default_timeout(10000) # в межах сторінки (page)
    page.goto("https://the-internet.herokuapp.com")


    page.mouse.wheel(0, 1000)
    page.mouse.wheel(0, -1000)
    page.wait_for_timeout(2000)

    a_links: list[Locator] = page.locator("//a").all()
    for link in a_links:
        print(link.text_content())
    breakpoint()
    heading_element: Locator = page.locator("h1.heading")
    welcome_text: str = heading_element.text_content()
    heading_class = heading_element.get_attribute("class")
    print(welcome_text)
    print(heading_class)

    # forgot_button = page.locator('//a[text()="Form Authentication"]')
    # forgot_button = page.get_by_text("Form Authentication")
    # forgot_button.click()
    #
    # username: Locator = page.locator("#username")
    # password: Locator = page.locator("#password")
    # #
    # username.type("test_user", delay=100)
    # password.type("test_password", delay=100)
    # page.keyboard.press("Enter")
    #
    # flash_alert = page.locator("//div[@id = 'flash']")
    # expect(flash_alert).to_be_visible()

    # checkboxes_button = page.locator('//a[text()="Checkboxes"]')
    # checkboxes_button.click()
    #
    # checkbox_2: Locator = page.get_by_text("checkbox 2")
    # checkbox_2.click()

    dropdowns_button = page.locator('//a[text()="Dropdown"]')
    dropdowns_button.click()

    dropdown: Locator = page.locator("select#dropdown")
    dropdown.select_option(label="Option 2")



    page.wait_for_timeout(5000) # analog time sleep



# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     page = browser.new_page()
#     page.set_default_timeout(10000) # в межах сторінки (page)
#     page.goto("https://demo.automationtesting.in/Register.html")
#
#
#     page.locator("#checkbox2").check()
#
#     page.wait_for_timeout(1000)
#
#     page.locator("#checkbox2").uncheck()
#
#     page.wait_for_timeout(3000)