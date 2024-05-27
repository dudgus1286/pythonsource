import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

url = "https://finance.naver.com/"

userAgent = UserAgent()
header = {"user-agent": userAgent.chrome}

with requests.Session() as s:
    r = s.get(url, headers=header)
    # print(r.text)
    # print(r.status_code)

    soup = BeautifulSoup(r.text, "lxml")

    # 해외 증시
    h_stockList = soup.select(".h_stock +table tbody tr")
    # print(h_stockList)
    for item in h_stockList:
        # 회사명
        company_name = item.select_one("a").string
        # 현재 금액
        current_amount = item.select_one("td").string

        print(company_name, current_amount)

    # 인기 검색종목
    h_popular = soup.select(".h_popular +table tbody tr a")
    # print(h_popular)
    for item in h_popular:
        print(item.get_text())
