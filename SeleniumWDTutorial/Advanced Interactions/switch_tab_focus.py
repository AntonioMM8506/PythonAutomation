from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class SwitchTabFocus():
    def test(self):
        baseURL = "https://www.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseURL)

        # Store the ID of the original tab
        original_tab = driver.current_window_handle

        # Click the button that opens a new tab
        driver.find_element(By.ID, "opentab").click()
        time.sleep(2)

        # Switch to the new tab
        self.switch_to_new_tab(driver, original_tab)
        time.sleep(2)

        # Perform actions in the new tab (e.g., print the title)
        print("New tab title:", driver.title)

        # Close the new tab and switch back to the original tab
        driver.close()
        driver.switch_to.window(original_tab)
        print("Switched back to original tab:", driver.title)

        driver.quit()

    # Switch to the new tab
    def switch_to_new_tab(self, driver, original_tab):
        try:
            # Wait for the new tab to open
            time.sleep(2)
            # Get all window handles
            all_tabs = driver.window_handles
            for tab in all_tabs:
                if tab != original_tab:
                    driver.switch_to.window(tab)
                    print("Switched to new tab successfully.")
                    return
            print("No new tab found.")
        except Exception as e:
            print(f"Error occurred while switching to new tab: {e}")

stf = SwitchTabFocus()
stf.test()