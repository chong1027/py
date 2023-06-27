import time
import lo
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
reMR=" "
relo=" "
relo=lo.lo1(input("請輸入地區:"))
reMR=lo.MR(input("請輸入認證:"))
options = Options()
options.chrome_executable_path = "C:\Program Files\Google\Chrome\Application"
driver = webdriver.Chrome(options=options)
Str=""
tim=0
i=0
for i in range(1,int(10**100)): 
    #if(reMR!=None and relo!=None):driver.get(F"https://www.taiwan.net.tw/m1.aspx?sNo=0020118&keyString=%5e{relo}%5e{reMR}&page={i}")
    #elif(reMR==None and relo!=None):driver.get(F"https://www.taiwan.net.tw/m1.aspx?sNo=0020118&keyString=%5e{relo}%5e&page={i}")
    #elif(relo==None and reMR!=None):driver.get(F"https://www.taiwan.net.tw/m1.aspx?sNo=0020118&keyString=%5e%5e{reMR}&page={i}")
    #else: driver.get(F"https://www.taiwan.net.tw/m1.aspx?sNo=0020118&keyString=%5e%5e&page={i}")#https://www.taiwan.net.tw/m1.aspx?sNo=0020118&keyString=%5e%5e
    driver.get(F"https://www.taiwan.net.tw/m1.aspx?sNo=0020118&keyString=%5e{relo}%5e{reMR}&page={i}")#
    time.sleep(0.5)
    if(driver.find_elements(By.CLASS_NAME,"error-title")):
         break
    if(driver.find_elements(By.CLASS_NAME,"name")):
        tags = driver.find_elements(By.CLASS_NAME,"name")
        for aa in tags:
            Str+=aa.text
            Str+="\n"
            tim+=1
    else:
        break
for i in range(1,50):
    print("\n")
print("開始列印\n")
print(Str)
print("共計"+str(tim)+"家餐旅")
driver.close()
pass