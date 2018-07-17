import requests
from bs4 import BeautifulSoup
import re
import csv
import json

session = requests.session()
url = "http://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day&sectionId=103&date=20180715"
#url = "http://news.naver.com/main/ranking/popularDay.nhn?"\
#    "rankingType=popular_day"\
#    "sectionId=105"\
#    "date=20180712"
response = session.get(url)

csvfile = open("news name.csv","w")
jsonfile = open("news name.json","w")

spamWriter = csv.writer(csvfile)

soup = BeautifulSoup(response.text,"html.parser")

for i in range(30):
    soupResult = soup.findAll("li",{"class":"ranking_item is_num"+str(i+1)})
    exp = r"(?<=title=\").*(?=\"\s)"
    rex = re.search(exp, str(soupResult))

    if(rex is not None):
        data = {"title": str(rex.group(0))}
        json.dump(data, jsonfile)

        spamWriter.writerow([str(rex.group(0))])
        print(rex.group(0))