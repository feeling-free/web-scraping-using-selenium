from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

wd = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options= chrome_options)

# Get the main page
wd.get("https://www.wikipedia.org/")

# Assertion statement
assert("Wikipedia" in wd.title)

# Print the entire HTML
# print(wd.page_source)

# Fetching the element by ID
input_element = wd.find_element(by=By.ID, value="searchInput")

# Sending keys
input_element.send_keys("ADS")

# Fetch search button through Css Class Name
search = wd.find_element(by=By.CLASS_NAME, value="pure-button")

# Click the search button
wd.execute_script("arguments[0].click();", search)