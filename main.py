import json
import re
import requests
import csv

URL = " http://www.cbr-xml-daily.ru/archive/2022/09/17/daily_json.js"
# html_text = requests.get(url).text
# json_pars = json.loads(html_text)
# print(html_text)
# current_day = json_pars["Date"]
#
# previous_day_url = json_pars["PreviousURL"]
# final_previous_day_url = previous_day_url.replace('//', '') #ссылка на предыдущий день
# final_current_day = re.findall(r'(\d{4}\-\d{2}\-\d{2})', current_day)
# current_course = json_pars["Valute"]["USD"]["Value"]
#
# print(str(*final_current_day), current_course)
# switch_current_day_url = "http://" + final_previous_day_url
# print(switch_current_day_url)

# with open("C:/Users/artyo/Desktop/dataset.csv", "w", newline='') as file:
#     writer = csv.writer(file, delimiter="\t")
#     writer.writerow(HEADER)

for i in range(1, 10):
    html_text = requests.get(URL).text
    json_pars = json.loads(html_text)

    current_day = json_pars["Date"]
    final_current_day = re.findall(r'(\d{4}\-\d{2}\-\d{2})', current_day)

    current_course = json_pars["Valute"]["USD"]["Value"]
    previous_day_url = json_pars["PreviousURL"]
    final_previous_day_url = previous_day_url.replace("//", "")
    switch_current_day_url = "http://" + final_previous_day_url
    # print([str(*final_current_day), current_course])
    with open("C:/Users/artyo/Desktop/dataset.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow([str(*final_current_day), current_course])

    URL = switch_current_day_url

