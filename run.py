import csv
import random

from os.path import expanduser
home = expanduser("~")

from colorama import init, Fore
init()

with open(home + "/word_of_the_day/dat.csv") as wordFile:
    reader = csv.reader(wordFile)
    rows = list(reader)
    lineNum = random.randint(0, len(rows) - 1)
    words = list(rows[lineNum])

print(Fore.RED + "Dagens ord: " + Fore.GREEN + words[0] + Fore.RED + " (" + words[1] + ")")
