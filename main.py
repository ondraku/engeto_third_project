import sys
import csv
import requests
from bs4 import BeautifulSoup

SEPARATOR = "=" * 70

def main():
    print(SEPARATOR)
    print("Welcome to the Elections Scraper app!")
    print("This app will show you results of the 2017 elections by region.")
    print(SEPARATOR)
    print(
    """
    * Please visit: https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ
    * Choose your region by clicking on 'X' in 'Vyber obce' column.
    """
    )
    print(SEPARATOR)
    user_region = input("Please copy the URL and paste it here: ")
    file_name = input("Please choose a name for the file - without suffix please: ")
    print(SEPARATOR)

    f = open(file_name + ".csv", mode="w")
    f_writer = csv.writer(f, delimiter=";")

