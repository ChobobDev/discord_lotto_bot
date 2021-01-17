import requests
from bs4 import BeautifulSoup

lotto_url="https://www.dhlottery.co.kr/gameResult.do?method=byWin"
url_parser=requests.get(lotto_url)
url_text=url_parser.text
soup=BeautifulSoup(url_text,"html.parser")
info=soup.find("div",attrs={ "class" : "win_result"})
current_ed = info.find("h4").find("strong").text
numb = info.find("div",attrs={ "class" : "nums"})
win_num=numb.find("div",attrs={ "class" : "num win"}).find("p").find_all("span")
bonus_num=numb.find("div",attrs={ "class" : "num bonus"}).find("p").find("span").text