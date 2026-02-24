import time
import pandas as pd
from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


#driver = webdriver.Chrome() #Opens the chromedriver. If u don't have a chromedriver, u can download it from https://chromedriver.chromium.org/downloads 

#def interceptor(request):
#   del request.headers['User-Agent']
#   request.headers['User-Agent'] = 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1'
#driver.request_interceptor = interceptor


options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.set_window_size(400, 400)
# driver.implicitly_wait(10)
wait = WebDriverWait(driver, 15)


try:
    driver.get('https://handlaprivatkund.ica.se/stores/1003620/search?q=mj%C3%B6lk') #Opens the specified url  
    time.sleep(3)

    # Vänta tills iframe laddas
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
    iframes = driver.find_elements(By.TAG_NAME, "iframe")
    
    for iframe in iframes:
        driver.switch_to.frame(iframe)
        # buttons = driver.find_elements(By.XPATH, "//*[@id='onetrust-accept-btn-handler']")
        # print(buttons)

        # for b in buttons:
        #     print(b.text)
            
        try:
            cookie_btn = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='onetrust-accept-btn-handler']"))
            )
            cookie_btn.click()
            print("Cookie accepterad")
            break
        except:
            driver.switch_to.default_content()

        print("clicking")


    # for request in driver.requests:
    #     if request.response:
    #         print(
    #             # request.url,
    #             # request.response.status_code,
    #             request.response.headers['Content-Type']
    #         )
    # driver.refresh ()

    # presence_of_element_located
    # pNr = driver.find_element(By.XPATH, "//input[@id='inputElementId--1']")
    # btn = driver.find_element(By.XPATH, "//div[@class='button' and contains(text(), 'Godkänn alla cookies')]")
    # new WebDriverWait(driver, 10).until(ExpectedConditions.visibility_of_element_located(By.id("U_1L_1001"))).click();
    # "//input[@type='text' and @placeholder='ÅÅÅÅMMDD-XXXX']"
    # wait = WebDriverWait(driver, 20)

    # e = wait.until(EC.presence_of_element_located((By.XPATH, "//form[@class='ng-pristine ng-invalid ng-touched']")))
    # print(e.is_displayed())
    # /html/body/section[2]/section[2]/div/section/section[2]/div[2]/button[2]
    
    # e1 = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='ikano-button ikano-accent-ligth oam-login-btn-mobile' and @type='button']")))
    # print(e1.is_displayed())
    # e3 = e2.find_element(By.XPATH, "//div[@class='form-field-wrapper']")
    # e3 = e2.find_elements(By.TAG_NAME, "input")[0]
    # e3 = e2.find_element(By.XPATH, "//input[@type='text' and @placeholder='ÅÅÅÅMMDD-XXXX']").send_keys('19640403-xxxx')
    # driver.execute_script("arguments[0].style.display = 'block';", e3)
    # e3 = e2.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='text']")))
    # e3[0].send_keys('19640403')
    # print(e3.is_displayed())
    # e = wait.until(lambda x: x.find_element(By.XPATH, "//input[@type='text' and @placeholder='ÅÅÅÅMMDD-XXXX']")) 
    # driver.execute_script("arguments[0].style.display = 'block';", e)
    
    # e = wait.until(lambda x: x.find_element(By.TAG_NAME, "span")) 
    # e = WebDriverWait(driver, 30, 1, (ElementNotVisibleException)).until_not(lambda x: x.find_element(By.XPATH, "//input[@type='text' and @placeholder='ÅÅÅÅMMDD-XXXX']").is_displayed())
    # e.send_keys('19640403')
    # print(e.text)

    # btn2 = driver.find_elements(By.XPATH, '//html/body/fdp-root/acorn-main-layout/acorn-main-layout-header/fdp-page-header/acorn-top-navbar/acorn-top-navbar-brand-image//a/img')
    # pNr = driver.find_element(By.XPATH, "//html/body/fdp-root/acorn-main-layout/div/div[2]/fdp-login-page/acorn-dialog-page/div/div[1]/fdp-app-login-initial/div/fdp-widget-login/div/fdp-widget-login-initial/form/acorn-text-field//div[1]/div[2]/input")
   
    # try:
    #     print(e.is_displayed())
    #     for x in e:
    #         print(x)
    # except:
    #     print("exeption")

    # /html/body/fdp-root/acorn-main-layout/div/div[2]/fdp-login-page/acorn-dialog-page/div/div[1]/fdp-app-login-initial/div/fdp-widget-login/div/fdp-widget-login-initial/form/acorn-text-field//div[1]/div[2]/input
    # //*[@id="inputElementId--1"]  "//input[@type='text' and @id='inputElementId--1']"

    
    print("success in clicking button")
    time.sleep(5)
except:

    print("login button has failed")
    time.sleep(5)
    driver.quit()