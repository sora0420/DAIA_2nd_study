from urllib.request import Request, urlopen
import re
from bs4 import BeautifulSoup
import requests
import csv
import json
import numpy as np
import pandas as pd


html = Request("https://dgucoop.dongguk.edu/store/store.php?w=4&l=2")#생협주소
webpage = urlopen(html).read()
soup = BeautifulSoup(webpage, "html.parser")


#요일 리스트 뽑기

#all = soup.findAll("div",{"class":"detail_board"})
weekday = soup.findAll("td",{"style":"padding:5px 0 5px 0;text-align:center;width:86px;line-height:150%;"})
weekResult = []
j = 0
for i in weekday:
    exp = r"\d{2}월 \d{2}일"
    rex = re.search(exp, str(i))
    weekResult.append(rex.group(0))
print(weekResult)


#식당 이름
resResult = []
resName = soup.findAll("td",{"class":"menu_st"})
for i in resName:
    exp = r"(?<=3px 5px;\">).*(?=</td>)"
    rex = re.search(exp, str(i))
    resResult.append(rex.group(0))
print(resResult)


#식당안의 코너
resResult1 = []
resName1 = soup.findAll("td",{"style":"width:30;padding:5px 0 5px 0;"})
for i in resName1:
    exp = r"(?<=0 5px 0;\">).*(?=</td>)"
    rex = re.search(exp, str(i))
    resResult1.append(rex.group(0))
print(resResult1)


resMenu = soup.findAll("span",{"style":"color:#303030;font-size:9pt;"})
print(resMenu)
print(len(resMenu))

menuResult = []
for i in resMenu:
    exp = r"(?<=<span style=\"color:#303030;font-size:9pt;\">).*(?=<br>\r)"
    rex = re.search(exp, str(i))
    if (rex is not None):
        menuResult.append(rex.group(0))
    else:
        continue
print(menuResult)
print(len(menuResult))
