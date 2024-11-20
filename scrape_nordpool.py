import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.nordpoolgroup.com/")
    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="Market data", exact=True).click()
    page1 = page1_info.value
    page1.get_by_role("button", name="Allow and close", exact=True).click()
    page1.get_by_role("gridcell", name=":00 - 01:00").click()

    print(page1)



    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
