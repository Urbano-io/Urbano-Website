from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=True)

    # Desktop view
    desktop_context = browser.new_context(viewport={'width': 1200, 'height': 800})
    desktop_page = desktop_context.new_page()
    desktop_page.goto("http://127.0.0.1:8000/")

    # Scroll to the bottom where the logos are
    desktop_page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    desktop_page.wait_for_timeout(1000)

    desktop_page.screenshot(path="desktop_footer.png")
    desktop_context.close()

    # Mobile view
    mobile_context = browser.new_context(viewport={'width': 375, 'height': 667}, is_mobile=True)
    mobile_page = mobile_context.new_page()
    mobile_page.goto("http://127.0.0.1:8000/")

    # Scroll to the bottom where the logos are
    mobile_page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    mobile_page.wait_for_timeout(1000)

    mobile_page.screenshot(path="mobile_footer.png")
    mobile_context.close()

    browser.close()

with sync_playwright() as playwright:
    run(playwright)
