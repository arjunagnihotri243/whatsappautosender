import webbrowser
import time
import pyautogui as gui
import random
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import os
# import csv


numbers = []
with open("input.txt", 'r') as f:
    lines = f.readlines()
    for line in lines:
        with open("output.txt", "a") as fTwo:
            fTwo.write(f"+{line}")


with open("output.txt", 'r') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        numbers.append(lines[i].strip('\n'))


print(numbers)

PATH = "./chromedriver.exe"
driver = webdriver.Chrome(PATH)


driver.get("https://web.whatsapp.com/")
driver.maximize_window()
time.sleep(5)

a = ActionChains(driver)
count = 0
for i in numbers:
    print(f"Going to Number: {i}")
    url = f"https://web.whatsapp.com/send?phone={i}&app_absent=0"
    try:
        driver.get(url)
        time.sleep(6)

        inpBox = driver.find_elements_by_class_name("_1awRl")

        gui.hotkey('ctrl', 'v')

        gui.press("enter")
        time.sleep(random.randrange(15, 30))
        count += 1
    except:
        pass

with open("log.txt", 'w') as f:
    f.write(f"Completed: {count}")

os.system("shutdown /s")

# https://web.whatsapp.com/send?phone=917355088659&text=Automated+Message&app_absent=0
