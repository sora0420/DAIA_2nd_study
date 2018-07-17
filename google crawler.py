import requests
from bs4 import BeautifulSoup
import json

class GoogleCrawler:
    def __init__(self):
        self.url = "https://www.google.co.kr/search"
        self.keywordPrefix = "q="
        self.searchType = "tbm=isch"
        self.clientinfo = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
        self.session = requests.session()
        self.linklist =[]
        self.typelist = []

    def searchKeyword(self, keyword_):
        targetUrl = self.url + "?" + self.keywordPrefix + keyword_ + "&" + self.searchType
        response = self.session.get(targetUrl, headers = {"User-agent" : self.clientinfo})
        soup = BeautifulSoup(response.text, "html.parser")
        soupResult = soup.findAll("div",{"class" : "rg_meta notranslate"})
        for i in range(100):
            link, type = json.loads(soupResult[i].text)["ou"], json.loads(soupResult[i].text)["ity"]
            self.linklist.append(link)
            self.typelist.append(type)

    def dataSave(self, name):
        print("saving...")
        for i in range(100):
            fileinstance = open("image_"+name+"_"+str(i)+"."+ self.typelist[i], 'wb')
            img_response = self.session.get(self.linklist[i])
            fileinstance.write(img_response.content)
        print("complete!")


googleCrawler = GoogleCrawler()
googleCrawler.searchKeyword("apple")
name = input("file name : ")
googleCrawler.dataSave(name)