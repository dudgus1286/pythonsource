# 크롤링 : 주기적 / 무작위로 데이터 수집
# requests, beautifulsoup4, selenium 패키지 설치

# requests : 웹서버로 요청 시 사용

import requests

urls = ["https://www.naver.com/", "https://www.python.org/"]

file_name = "robots.txt"

for url in urls:
    robots = requests.get(url + file_name)
    print(robots.text)
