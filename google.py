#!/usr/bin/python3

from googlesearch import search
import webbrowser, pyperclip, time

searching_for = input(("Input search words: "))
if searching_for == '':
    searching_for = pyperclip.paste()

num_results = int(input("How many results : ") or "3")

result = search(searching_for)

for i in list(result)[:num_results]:
    webbrowser.open(i)
    time.sleep(1)