import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

SEARCH_TERM = "mjölk"
MAX_PAGES = 3
DELAY = 3

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 15)

try:
    # 1️⃣ Öppna ICA
    driver.get("https://handlaprivatkund.ica.se/stores/1003620/search?q=mj%C3%B6lk")
    # driver.get("https://handlaprivatkund.ica.se/stores/1003620")
    time.sleep(3)

    # 2️⃣ Acceptera cookies (om popup finns)
    try:
        cookie_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Acceptera')]"))
        )
        cookie_btn.click()
        time.sleep(2)
    except:
        pass

    # 3️⃣ Sök efter mjölk
    search_box = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='search']"))
    )
    search_box.clear()
    search_box.send_keys(SEARCH_TERM)
    search_box.send_keys(Keys.ENTER)

    time.sleep(4)

    all_products = []

    # 4️⃣ Pagination-loop
    for page in range(MAX_PAGES):
        print(f"Hämtar sida {page+1}")
        time.sleep(DELAY)

        products = driver.find_elements(By.CSS_SELECTOR, "[data-testid='product-card']")

        for product in products:
            try:
                name = product.find_element(By.CSS_SELECTOR, "h3").text
            except:
                name = ""

            try:
                price = product.find_element(By.CSS_SELECTOR, "[data-testid='price']").text
            except:
                price = ""

            all_products.append({
                "name": name,
                "price": price
            })

        # Klicka nästa sida om den finns
        try:
            next_button = driver.find_element(By.XPATH, "//button[contains(., 'Nästa')]")
            driver.execute_script("arguments[0].click();", next_button)
        except:
            print("Ingen fler sida hittades.")
            break

    # 5️⃣ Spara CSV
    df = pd.DataFrame(all_products)
    df.to_csv("ica_maxi_trelleborg_mjolk.csv", index=False, encoding="utf-8-sig")

    print(f"\nKlart! Sparade {len(df)} produkter.")

finally:ls
    driver.quit()