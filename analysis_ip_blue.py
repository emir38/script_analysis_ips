#!/usr/bin/env python3

#This script can be used in windows or linux,if you have a linux without an GUI must have to do a few modifications in the lines webbrowser,you can use subprocess to open browser
#To run this script you will neew to create a file ip_directions.txt which will be iterated to obtain the analysis of the Ips in it

import subprocess
import webbrowser
import pyperclip
import pyautogui
import time
from termcolor import colored

doc = open('ip_directions.txt', 'r')
doc = doc.read().split('\n')

print(colored("Enter the name of the tool which you wanna use to analysis the ip directions: ", "green"))
print(colored("\n 1 - Symantec\n 2 - AbuseIP\n 3 - Virustootal\n", "yellow"))
choose = input("-> ")

# Its recommended adjust the time.sleep to the velocity of your internet for a good performance
# You can add more tools to analysis

if choose == "1":
    for ip in doc:
        webbrowser.get('firefox').open_new("https://sitereview.bluecoat.com/#/")
        time.sleep(5)
        pyperclip.copy(ip)
        pyautogui.hotkey('ctrl', 'v', interval = 0.15)
        pyautogui.press("enter")
elif choose == "2":
    for ip in doc:
        webbrowser.get('firefox').open_new("https://www.abuseipdb.com/")
        time.sleep(3)
        for i in range(15):
            pyautogui.press("tab")
        pyperclip.copy(ip)
        pyautogui.hotkey('ctrl', 'v', interval = 0.15)
        pyautogui.press("enter")
elif choose == "3":
    for ip in doc:
        webbrowser.get('firefox').open_new("https://www.virustotal.com/gui/home/search")
        time.sleep(3)
        for i in range(6):
            pyautogui.press("tab")
        pyperclip.copy(ip)
        pyautogui.hotkey('ctrl', 'v', interval = 0.15)
        pyautogui.press("enter")
else:
    print(colored("ERROR: The option you has been chosen are incorrect"))

