from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from datetime import datetime, time, timedelta


# Get the page
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://ozh.github.io/cookieclicker/")

# Choose the language
driver.implicitly_wait(3)
language_elem = driver.find_element(By.ID, "langSelect-EN")
language_elem.click()

# Game logic - find button
driver.get("https://ozh.github.io/cookieclicker/")
elem = driver.find_element(By.ID, "bigCookie")

# Game logic - play for 5 min / 30 seconds
running = datetime.now() + timedelta(0,60)

while running.strftime("%H:%M:%S") != datetime.now().strftime("%H:%M:%S"):
    # Game logic - every 5 seconds
    y = datetime.now() + timedelta(0,5)
    while y.strftime("%H:%M:%S") != datetime.now().strftime("%H:%M:%S"):
        elem.click()

    # Game logic - buy a product
    buy_products = driver.find_elements(By.CLASS_NAME, "product.unlocked.enabled")
    product = buy_products[-1]
    print(product)
    product.click()

cookies_per_seconds = driver.find_element(By.ID, "cookies")
total_cookies = driver.find_element(By.ID, "cookiesPerSecond")

print(f"Game over. Cookies per second: {cookies_per_seconds}.\n Total cookies: {total_cookies}")



#Go to Spotify


