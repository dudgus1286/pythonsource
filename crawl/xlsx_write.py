# 엑셀 저장 모듈
# listdata=[[],[],[]] 형식
from openpyxl import Workbook
import os

print("현재 위치", os.getcwd())


def write_excel_template(filename, sheetname, listdata):
    # openpyxl workbook 생성
    wb = Workbook()
    ws = wb.active

    ws.title = sheetname
    # 너비 조정
    ws.column_dimensions["A"].width = 100

    # listdata append
    for row in listdata:
        ws.append(row)

    base_dir = "./crawl/file/"
    wb.save(base_dir + filename)
    wb.close()


if __name__ == "__main__":
    listdata = [["이름", "나이"], ["홍길동", "25"], ["성춘향", 22]]
    write_excel_template(filename="temp.xlsx", sheetname="test", listdata=listdata)
