import requests
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from openpyxl import Workbook

wb = Workbook()
ws = wb.active

ws.title = "네이버open"
# 너비 조정
ws.column_dimensions["B"].width = 30
ws.column_dimensions["C"].width = 80

ws.append(["번호", "isbn", "책제목", "할인가격"])

headers = {
    "X-Naver-Client-Id": "y75cFyztfRqWH6MqHjz4",
    "X-Naver-Client-Secret": "QtZOXTb6DB",
}

num, start = 0, 1
for idx in range(2):
    start_num = start + (idx * 100)
    url = "https://openapi.naver.com/v1/search/book.json"

    params = {"query": "베르나르 베르베르", "display": "100", "start": str(start_num)}
    r = requests.get(url, headers=headers, params=params)
    # print(r.url)

    # json 가져오기
    data = r.json()
    # print(data)
    for idx, item in enumerate(data["items"], 1):
        print(idx + num, item["isbn"], item["title"], item["discount"])
        ws.append([idx + num, item["isbn"], item["title"], item["discount"]])
    num += 100

base_dir = "./crawl/file/"
wb.save(base_dir + "베르나르.xlsx")
wb.close()
