import selenium
import time
from dotenv import load_dotenv
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium import webdriver
import os
load_dotenv()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=4137024751&f_AL=true&f_E=1%2C2&f_WT=2&geoId=102713980&keywords=python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&spellCorrectionEnabled=true")


def abort_application():
    # Click Close Button
    close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
    close_button.click()

    time.sleep(2)
    # Click Discard Button
    discard_button = driver.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
    discard_button.click()



my_email = os.getenv("EMAIL")
my_pass = os.getenv("PASSWORD")
my_phone = os.getenv("PHONE")
login = driver.find_element(By.XPATH,value='//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]/button')
time.sleep(3)
login.click()
time.sleep(3)
#Logging in Linkedin
email = driver.find_element(By.ID,value="base-sign-in-modal_session_key")
email.send_keys(my_email)
password = driver.find_element(By.ID,value="base-sign-in-modal_session_password")
password.send_keys(my_pass)
submit = driver.find_element(By.XPATH,value='//*[@id="base-sign-in-modal"]/div/section/div/div/form/div[2]/button')
submit.click()

time.sleep(3)
i=1
all_listings = driver.find_elements(By.CSS_SELECTOR,value=".job-card-container--clickable")
for listing in all_listings:
    listing.click()
    time.sleep(2)
    try:
        apply = driver.find_element(By.CSS_SELECTOR,value=".jobs-apply-button")
        apply.click()
        time.sleep(5)
        number = driver.find_element(By.CSS_SELECTOR,value="input[id*=phoneNumber]")
        if number == "":
            number.send_keys(my_phone)
        submit_application = driver.find_element(By.CSS_SELECTOR, value='footer button')
        submit_application.click()
        if submit_application.get_attribute("data-control-name")=="continue-unify":
            abort_application()
            print("Complex application",skipped)
            continue
        else:
            print("Submitting job application")
            submit_application.click()
        time.sleep(2)
        #click close button
        close_button = driver.find_element(By.CLASS_NAME, value="artdeco-modal_dismiss")
        close_button.click()
    except NoSuchElementException:
        abort_application()
        print("No application button, skipped")
        continue
time.sleep(5)
driver.quit()