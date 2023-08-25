import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    driver = webdriver.Chrome()

    with open("jobs.json", "r") as json_file:
        loaded_data = json.load(json_file)

    if loaded_data:
        first_job = loaded_data[0]
        first_link = first_job.get("link")

        if first_link:
            driver.get(first_link)

            # Handle cookie consent if present
            try:
                cookie_consent_button = driver.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
                cookie_consent_button.click()
            except:
                pass  # Cookie consent button not found or unable to click

            wait = WebDriverWait(driver, 10)
            input_field = wait.until(EC.element_to_be_clickable((By.NAME, "first_name")))
            input_field.send_keys("12454")
            input_field = wait.until(EC.element_to_be_clickable((By.NAME, "last_name")))
            input_field.send_keys("845128")
            input_field = wait.until(EC.element_to_be_clickable((By.NAME, "email")))
            input_field.send_keys("845128@gmail.fi")
            input_field = wait.until(EC.element_to_be_clickable((By.NAME, "phone")))
            input_field.send_keys("4578951")
            file_path = r"C:\Users\user\Desktop\test.txt"
            file_input = wait.until(EC.presence_of_element_located((By.ID, "resume")))

            # Click the "Bifoga" button to initiate the file attachment
            attach_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-source='attach']")))
            attach_button.click()

            # Send the file path to the file input element
            file_input.send_keys(file_path)
            female_checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Female']")))
            female_checkbox.click()

            # Keep the browser open until user input
            input("Press Enter to close the browser...")
        else:
            print("No link found for the first job.")
    else:
        print("No job data found in the JSON file.")
except Exception as e:
    print("An error occurred:", str(e))
finally:
    driver.quit()
