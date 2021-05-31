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

    URL = "https://volby.cz/pls/ps2017nss/"
    header = False
    scrap = requests.get(region_url)
    tool = BeautifulSoup(scrap.text, "html.parser")
    regions = tool.find_all("td", {"class": "cislo"})

    for line in regions:
        region_data = []
        region_data = get_id_name(line, region_data)
        region_soup = get_soup(URL, line)

        region_results = region_soup.find(id="ps311_t1")
        region_data = get_voters(region_results, region_data)

        parties = region_soup.find(id="inner").find_all("tr")

        region_data = get_party_votes(parties, region_data)

        if not header:
            column_names = ["ID", "Name", "Registered voters", "Envelopes", "Valid Votes"]
            for new_line in parties:
                if not new_line.find("th"):
                    column_names.append(new_line.find_all("td")[1].string)
            f_writer.writerow(column_names)
            header = True

        f_writer.writerow(region_data)

    f.close()
    print("Process is now done!")

