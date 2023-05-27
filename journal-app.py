# Basic Journal Entry App

import time

date = time.strftime("%d-%m-%Y")
mood = input("How do you feel today on a scale of 1 to 10? ")
journal = input("Let your thoughts flow: \n")

FILEPATH = f"{date}.txt"

with open(FILEPATH, "w") as entry:
    entry.write(f"Date: {date}\n")
    entry.write(f"Mood: {mood}\n \n")
    entry.write(f"Entry: \n{journal}")