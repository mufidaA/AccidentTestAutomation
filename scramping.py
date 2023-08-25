from bs4 import BeautifulSoup
from selenium import webdriver
import time
import json

# Set up Selenium WebDriver (you need to have the appropriate driver installed)
# For example, for Chrome: https://sites.google.com/chromium.org/driver/
driver = webdriver.Chrome()

url = ""
driver.get(url)

# Wait for some time to let the page load the content
time.sleep(5)  # Adjust as needed

page_content = driver.page_source

driver.quit()

soup = BeautifulSoup(page_content, "html.parser")

job_items = soup.find_all("li", class_="w-full")

data = []  # Initialize an empty list to store job data

# Loop through li elements with class "w-full"
for job_item in job_items:
    job_title = job_item.find("span", class_="title").get_text(strip=True)
    job_link = job_item.find("a", class_="link")['href']
    
    print("Job Position:", job_title)
    print("Job Link:", job_link)
    print("---------------------------------------------------")
    
    # Append job data to the data list
    data.append({"job": job_title, "link": job_link})

# Write the entire data list to the JSON file outside the loop
with open("jobs.json", "w") as json_file:
    json.dump(data, json_file)
