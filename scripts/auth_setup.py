from playwright.sync_api import sync_playwright


def create_auth_state():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        context = browser.new_context()
        page = context.new_page()

        page.goto("https://app.plane.so/login", wait_until="networkidle")

        print("🔐 LOGIN MANUALLY (FULL FLOW REQUIRED)")
        print("👉 wait until you are inside workspace/dashboard")

        input("PRESS ENTER ONLY AFTER FULL AUTH")

        context.storage_state(path="state.json")

        print("✅ AUTH STATE SAVED")

        browser.close()


if __name__ == "__main__":
    create_auth_state()