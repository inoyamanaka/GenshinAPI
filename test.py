from bs4 import BeautifulSoup
import csv
import requests

# html = requests.get('https://docs.google.com/spreadsheets/d/e/2PACX-1vRq-sQxkvdbvaJtQAGG6iVz2q2UN9FCKZ8Mkyis87QHFptcOU3ViLh0_PJyMxFSgwJZrd10kbYpQFl1/pubhtml#').text
# soup = BeautifulSoup(html, "lxml")
# tables = soup.find_all("table")
# index = 0
# for table in tables:
#     # with open(str(index) + ".csv", "w") as f:
#     with open(str(index), "w", encoding="utf-8") as f:
#         wr = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
#         wr.writerows([[td.text for td in row.find_all("td")] for row in table.find_all("tr")])
#     index = index + 1
    
read =  open('3','r')
print(read.read())