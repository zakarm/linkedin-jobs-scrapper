import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 

def scrap_selenuim():
    url="https://www.linkedin.com/login"
    driver = webdriver.Chrome()
    driver.get(url)
    username = driver.find_element('name', 'session_key')
    username.send_keys('your_mail')

    password = driver.find_element('name', 'session_password')
    password.send_keys('you_password')
    password.send_keys(Keys.RETURN)
    time.sleep(5)
    driver.get('https://www.linkedin.com/jobs/')
    time.sleep(5)
    WebDriverWait(driver, 10).until(EC.title_contains("Jobs"))
    show_all_link = driver.find_element(By.XPATH, "//a[contains(@href,'/jobs/collections/recommended')]")
    show_all_link.click()
    time.sleep(5)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    job_cards = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "jobs-search-results__list-item"))
    )

    for job_card in job_cards:
        job_id = job_card.get_attribute("data-occludable-job-id")
        title = job_card.find_element(By.CLASS_NAME, "job-card-list__title").text
        company = job_card.find_element(By.CLASS_NAME, "job-card-container__primary-description").text
        location = job_card.find_element(By.CLASS_NAME, "job-card-container__metadata-item").text
        posted_time = job_card.find_element(By.TAG_NAME, "time").text

        print(f"Job ID: {job_id}")
        print(f"Title: {title}")
        print(f"Company: {company}")
        print(f"Location: {location}")
        print(f"Posted Time: {posted_time}")
        # print(f"Apply Method: {apply_method}")
        print("----")
    driver.quit()

def main():
    scrap_selenuim()

if __name__ == "__main__":
    main()