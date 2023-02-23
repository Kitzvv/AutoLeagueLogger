import os
import time
import pyautogui
import re
import linecache
import subprocess
import cv2

print("Checking files...")


def checker(c):
    os.path.exists(c)
    if not os.path.exists(c):
        print(f"Missing '{c}'")
        print("Program will quit in a moment ")
        time.sleep(5)
        quit()


while True:
    checker("Data.txt")
    checker("Config.txt")
    checker("Pictures/username.png")
    checker("Pictures/password.png")
    checker("Pictures/button.png")
    print("Found all files!")
    break

with open("Data.txt", "r") as f:
    line_num = len(f.readlines())

while True:
    account_num = input("Choose what acc u want to log: ")
    if not account_num.isdigit():
        print("Enter a number!")
    else:
        break

league_client = linecache.getline("Config.txt", 1)

if account_num == 0:
    print("Enter smh above 0")
    time.sleep(5)
    quit()
elif str(line_num) < str(account_num):
    print(f"U haven't add {account_num} acc to Data")
    time.sleep(5)
    quit()
else:
    subprocess.Popen(league_client)

line = linecache.getline("Data.txt", int(account_num))
data_username = re.findall(r"%\w+", line)
data_password = re.findall(r"/\w+", line)
username = [w.replace("%", "") for w in data_username]
password = [w.replace("/", "") for w in data_password]
clean_username = f"{username}"[2:-2]
clean_password = f"{password}"[2:-2]

photo_username = cv2.imread("Pictures/username.png")
photo_password = cv2.imread("Pictures/password.png")
photo_button = cv2.imread("Pictures/button.png")


def select_box(x):
    picture_box = pyautogui.locateCenterOnScreen(x, grayscale=False, confidence=0.75)
    pyautogui.click(picture_box)


def write_data(y):
    data = pyautogui.typewrite(f"{y}", interval=0.01)
    pyautogui.click(data)


def click_loging(z):
    sign_in = pyautogui.locateOnScreen(z, grayscale=False, confidence=0.75)
    pyautogui.click(sign_in)


select_box(photo_username)
time.sleep(5)
write_data(clean_username)
select_box(photo_password)
write_data(clean_password)
click_loging(photo_button)
