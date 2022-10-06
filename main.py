import json
import re
import requests
import csv

URL = " http://www.cbr-xml-daily.ru/archive/2022/09/17/daily_json.js"
HEADER = ["Day", "Excange rate"]

with open("C:/Users/artyo/Desktop/dataset.csv", "w") as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerow(HEADER)

while True:
    html_text = requests.get(URL).text
    json_pars = json.loads(html_text)

    current_day = json_pars["Date"]
    final_current_day = re.findall(r'(\d{4}\-\d{2}\-\d{2})', current_day)

    current_course = json_pars["Valute"]["USD"]["Value"]

    previous_day_url = json_pars["PreviousURL"]
    final_previous_day_url = previous_day_url.replace("//", "")
    switch_current_day_url = "http://" + final_previous_day_url

    with open("C:/Users/artyo/Desktop/dataset.csv", "a", newline="") as file:
        writer = csv.writer(file,  delimiter=";")
        writer.writerow([str(*final_current_day), current_course])

    URL = switch_current_day_url
