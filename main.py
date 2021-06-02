import sys
import csv
import requests
from bs4 import BeautifulSoup

SEPARATOR = "=" * 70
URL = "https://volby.cz/pls/ps2017nss/"

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
    link = get_link()
    file_name = get_name()
    print(SEPARATOR)

    f = open(file_name + ".csv", mode="w")
    f_writer = csv.writer(f, delimiter=";")

    header = False
    scrap = requests.get(link)
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
    print(f"Your file {file_name}.csv is ready for checking.")
    print("Thank you for using the Elections Scraper app!")

def get_link():
    link = input("Please copy the URL and paste it here: ")
    if "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=" in link and "&xnumnuts=" in link:
        return link
    else:
        print("You have enter different URL. Please try again.")
        quit()

def get_name():
    name = input("Please choose a name for the file: ")
    if ".csv" not in name:
        print(SEPARATOR)
        print("Exporting...please wait!")
        return name
    else:
        print("Please name the file without the suffix.")
        quit()

def get_id_name(line, list):
    list.append(line.find("a").string)
    list.append(line.parent.find_all()[2].string)
    return list

def get_soup(URL, line):
    region_url = requests.get(URL + line.find("a").attrs["href"])
    return BeautifulSoup(region_url.text, "html.parser")

def get_voters(region_results, list):
    list.append(region_results.find("td", {"class": "cislo", "headers": "sa2"}).string)
    list.append(region_results.find("td", {"class": "cislo", "headers": "sa3"}).string)
    list.append(region_results.find("td", {"class": "cislo", "headers": "sa6"}).string)
    return list

def get_party_votes(parties, list):
    for line in parties:
        if not line.find("th"):
            list.append(line.find_all("td", {"class": "cislo"})[1].string)
    return list

if __name__ == '__main__':
    sys.exit(main())
