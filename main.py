from selenium import webdriver
import time
import pandas as pd

df = pd.read_excel("cgpa.xlsx", dtype = {"name": str,
                            "regno":int,"first":str,"second":str})
Name_list = df["name"].tolist()
print(Name_list)
Reg_list = df["regno"].tolist()
print(Reg_list)
First_list = df["first"].tolist()
print(First_list)
Second_list = df["second"].tolist()
print(Second_list)
num=len(Name_list)
print(num)
driver = webdriver.Chrome(executable_path="E:\chromedriver.exe")
driver.get("https://docs.google.com/forms/d/e/1FAIpQLScY9MNC_P-obqKcJCaZIesQa5VbkvIwSxzRYghTYGYTtxGKyg/viewform?vc=0&c=0&w=1&flr=0")
time.sleep(2)

for i in range(0,num):

    element = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    element.send_keys(Name_list[i])
    time.sleep(2)
    register = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    register.send_keys(Reg_list[i])
    time.sleep(2)
    firstSem = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    firstSem.send_keys(First_list[i])
    time.sleep(2)
    secondSem = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
    secondSem.send_keys(Second_list[i])
    time.sleep(2)
    submit= driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    submit.click()

    reponse = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    reponse.click()
driver.close()