import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from openpyxl import Workbook
from xlsx_write import write_excel_template
from datetime import datetime

userAgent = UserAgent()
header = {"user-agent": userAgent.chrome}

# 데이터 담을 리스트 생성
# lists = []
lists = list()

with requests.Session() as s:

    for page in range(5):
        url = "https://www.clien.net/service/board/lecture?&od=T31&category=0&po="
        url = url + str(page)
        r = s.get(url, headers=header)
        # print(r.title)
        # print(r.status_code)
        soup = BeautifulSoup(r.text, "lxml")

        # 타이틀 출력
        # titles = soup.select(".list_content .list_item .list_title a span.subject_fixed")
        # for title in titles:
        #     print(title.text.strip())
        # print(len(titles))

        # dates = soup.select(".list_content .list_item .list_time span.timestamp")
        # print(len(dates))
        # for date in dates:
        #     print(date.text)

        # 행 가져오기
        rows = soup.select("div.list_content > div.list_item.symph_row")

        # 시트명: 팁과강좌, 파일명: clien_240527.xlsx
        # 파일 저장 [타이틀, 날짜]를 배열에 담음
        # 2024-05-23 16:03:53 => 2024-05-23
        for row in rows:
            title = row.select_one("div.list_title > a > span.subject_fixed")
            time = row.select_one("div.list_time > span > span")
            print(title.text.strip(), time.text.strip()[:10])

            lists.append([title.text.strip(), time.text.strip()[:10]])
        print()

# 오늘 날짜
today = datetime.now().strftime("%Y%m%d")
write_excel_template(f"clien_{today}.xlsx", "팁과강좌", lists)
