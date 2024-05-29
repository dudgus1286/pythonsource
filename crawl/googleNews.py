# 파이썬 뉴스기사 크롤링
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from urllib.error import HTTPError

base_url = "https://news.google.com"


def main(keyword):
    url = "https://news.google.com/search?q=" + keyword + "=ko&gl=KR&ceid=KR%3Ako"

    try:
        with requests.Session() as s:
            r = s.get(url)
            soup = BeautifulSoup(r.text, "lxml")

            news_clipping = data_extract(soup)
            for news in news_clipping:
                for k, v in news.items():
                    print(f"{k} : {v}")
                print()

    except HTTPError as e:
        print(e.code)


def data_extract(soup):
    # div > c-wiz > c-wiz article
    articles = soup.select("div.UW0SDc article")
    news = []
    news_items = {}

    for article in articles:
        print(article.text)

        # a 태그만 추출
        link_title = article.select_one("div > div:nth-child(2) a")
        # print(link_title)

        # 기사 제목, 링크 추출
        title = link_title.text
        href = base_url + link_title["href"][1:]
        # link_title["href"] = ./articles/CBMiNGh0dHBzOi8vd3d3LmU0ZHMuY29tL3N1Yl92aWV3LmFzcD9jaD02JnQ9MCZpZHg9MTg5OTLSAQA?hl=ko&gl=KR&ceid=KR%3Ako

        # 언론사 추출
        writer = article.select_one("div div.oovtQ div.vr1PYe").text

        news_items["title"] = title
        news_items["href"] = href
        news_items["writer"] = writer

        # 작성일자와 시간 따로 추출
        # T 기준으로 분리
        date = article.select_one("div:last-child time")
        if date:
            # []
            date = date["datetime"].split("T")
            news_items["report_date"] = date[0]
            news_items["report_time"] = date[1]
        else:
            report_date = ""
            report_time = ""

        # print(title)
        # print(href)
        # print(writer)
        # print(report_date + " " + report_time)

        news.append(news_items)
        news_items = {}


if __name__ == "__name__":
    main("아이폰")
