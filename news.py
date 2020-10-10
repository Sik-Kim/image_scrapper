from bs4 import BeautifulSoup
from selenium import webdriver

from openpyxl import Workbook


driver = webdriver.Chrome("./chromedriver")

url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=추석"

driver.get(url)
req = driver.page_source
soup = BeautifulSoup(req, "html.parser")

wb = Workbook()
ws1 = wb.active
ws1.title = "articles"
ws1.append(["제목", "링크", "신문사", "썸네일"])

articles = soup.select("#main_pack > div.news.mynews.section._prs_nws > ul > li")

for article in articles:
    a_tag = article.select_one("dl > dt > a")

    title = a_tag.text
    url = a_tag["href"]
    comp = (
        article.select_one("dd.txt_inline > span._sp_each_source")
        .text.split(" ")[0]
        .replace("언론사", "")
    )
    thumbnail = article.select_one("div > a > img")["src"]

    ws1.append([title, url, comp, thumbnail])

driver.quit()
wb.save(filename="articles.xlsx")
