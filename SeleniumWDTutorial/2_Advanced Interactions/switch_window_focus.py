from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class SwitchWindowFocus():
    def test(self):
        baseURL = "https://www.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseURL)

        # Store the ID of the original window
        original_window = driver.current_window_handle

        # Click the button that opens a new window
        driver.find_element(By.ID, "openwindow").click()
        time.sleep(2)

        # Switch to the new window
        self.switch_to_new_window(driver, original_window)
        time.sleep(2)

        # Perform actions in the new window (e.g., print the title)
        print("New window title:", driver.title)

        # Close the new window and switch back to the original window
        driver.close()
        driver.switch_to.window(original_window)
        print("Switched back to original window:", driver.title)

        driver.quit()

    # Switch to the new window
    def switch_to_new_window(self, driver, original_window):
        try:
            # Wait for the new window to open
            time.sleep(2)
            # Get all window handles
            all_windows = driver.window_handles
            for window in all_windows:
                if window != original_window:
                    driver.switch_to.window(window)
                    print("Switched to new window successfully.")
                    return
            print("No new window found.")
        except Exception as e:
            print(f"Error occurred while switching to new window: {e}")

ff = SwitchWindowFocus()
ff.test()