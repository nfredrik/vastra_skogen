import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://westforest.se/")
    page.locator("#burger").click()
    page.get_by_role("link", name="Kontakt").click()
    page.get_by_role("button", name="Ok").click()

    #wtf_page = page.content()
    #print(wtf_page)

    email_elements = page.query_selector_all("a[href^='mailto:']")
    emails = []
    for element in email_elements:
        email_href = element.get_attribute("href")
        if email_href and email_href.startswith("mailto:"):
            emails.append(email_href[len("mailto:"):])  # Strip 'mailto:'

    print(f"Extracted Emails: {emails}")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
