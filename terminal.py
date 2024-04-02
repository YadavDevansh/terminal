import os
from selenium import webdriver
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.by import By
import sys
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--headless=new")
driver= webdriver.Chrome(options=chrome_options)
os.system("cls")
#ticker=input("enter ticker : ")
#print(sys.argv)

a=os.getpid()

ticker=sys.argv[1]


f = open("%s.txt"%ticker, "w")
f.write(str(a))
f.close()

driver.implicitly_wait(8)
driver.get("https://www.moneycontrol.com/us-markets/stockpricequote/apple/%s"%ticker)
driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/section[1]/div/div[2]/div/div/div[2]/div/a").click()
driver.implicitly_wait(8)
actions = ActionChains(driver)
print("ok")
time.sleep(10)

iframe = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/section[2]/div/div[1]/div[9]/h2")
ActionChains(driver).scroll_to_element(iframe).perform()

price_=float(0)

while 1<2:
    os.system("cls")

    price=float(driver.find_element(By.XPATH,"/html/body/div[1]/main/div[2]/section[2]/div/div[1]/div[1]/div/div[2]/div/div/div[2]").text)
    if(price_<price):
        os.system("color 0a")
    elif(price_>price):
        os.system("color 0c")
    else:
        os.system("color 08")
    os.system("echo %s %s"%(price,"delta=" + str(price-price_)))

    price_=price

os.system("color a0")    
driver.quit()



