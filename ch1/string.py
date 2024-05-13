# %%
# 문자 처리
# 문자, 문자열 구분 안함 - 쌍따옴표, 홑따옴표 다 허용
# "Life is too short, You need Python"
# 'Life is too short, You need Python'
# """Life is too short, You need Python"""
# '''Life is too short, You need Python'''

multiline = """
    Life is too short
    You need Python
"""
multiline

# %%
# + : 문자열 결합
str1 = "Python" + " is fun"
str1

# %%
# * : 문자열 반복
"Python " * 2

# %%
print("=" * 50)
print("My Program")
print("=" * 50)

# %%
# 문자열 인덱싱과 슬라이싱
# 문자열[찾으려는위치숫자]: 알아서 인덱싱 해줌
print(str1[3])
print(str1[5])
print(str1[-1])  # 오른쪽에서부터 인덱싱

# %%
# 슬라이싱 [시작위치:끝위치] => 끝위치는 포함안됨
str1 = "Life is too short"
print(str1[0:])
print(str1[0:4])
print(str1[4:])
print(str1[4:8])
print(str1[:17])
print(str1[0:-4])

# %%
# len() : 길이
len(str1)

# %%
str2 = "20240510Sunny"

date = str2[:8]
weather = str2[8:]

# 년월일 출력 : 20240510
print(date)

# 날씨 출력 : Sunny
print(weather)

# %%
# 년월일 출력 : 2024-05-10
print(date)
year = date[:4]
month = date[4:6]
day = date[6:]
print(year, month, day, sep="-")

# %%
jumin = "901205-3234567"
# 주민등록번호에서 1 or 3 남자, 2 or 4 여자
num1 = int(jumin[7])
if num1 % 2 == 0:
    print("여자")
else:
    print("남자")

# %%
str1 = "파이썬프로그래밍"
for s in str1:
    print(s + "♥", end="")

# %%
# 사용자로부터 숫자 입력받기
# 입력받은 숫자만큼 하트 출력

num1 = input("숫자 입력")

for i in range(len(num1)):
    for j in range(int(num1[i])):
        print("♥", end="")
    print()

# %%
# 문자열 함수
# 1) count() : 문자열에 포함된 특정 문자열 개수
str1 = "hobby"
print("a 문자열에 포함된 b 개수 %d" % str1.count("b"))

# %%
# 2) find() :
str1 = "Python is the best choice"
print("a 문자열에 b 위치 %d" % str1.find("b"))
print("a 문자열에 b 위치 {}".format(str1.find("b")))
print(f"a 문자열에 b 위치 {str1.find("b")}")
print("a 문자열에 b 위치", str1.find("b"))

# %%
# 3) index() : 문자열 위치
print("a 문자열에 b 위치 %d" % str1.index("b"))

# %%
# find() vs index()
# 찾는 값이 존재하지 않는 경우: -1 vs ValueError
# print("a 문자열에 b 위치 %d" % str1.index("K"))
# ValueError: substring not found 에러
print("a 문자열에 b 위치 %d" % str1.find("K"))
# -1

# %%
# 4) startwith / endswith
# 특정 문자열로 시작/끝나는지 체크
str2 = "Python Is Easy Programming"
print(str2.startswith("P"))
print(str2.endswith("P"))

# %%
# 5) join()
print(",".join("abcdefg"))
# a,b,c,d,e,f,g

# 리스트나 튜플 문자열로 변경할 때 주로 사용
list1 = ["a","b","c","d","e"]
print("".join(list1))

# %%
# 6) upper / lower / swapcase / title : 대소문자 변경

a = "abcde"
print("소문자 => 대문자 ", a.upper())

a = "ABCDE"
print("대문자 => 소문자 ", a.lower())

a = "Python is Easy"
print("대문자 소문자 상호 변환 ", a.swapcase())

a = "python is easy"
print("단어 제일 앞 글자 대문자로 변환 ", a.title())

# %%
# python 은 대소문자 구별함
print("abc" == "ABC")

# %%
# 7) lstrip / rstrip / strip : 왼/오른/양 쪽 공백 제거
a = "        hi"
print(a)
print(a.lstrip())

a = "hi        "
print(a)
print(a.rstrip())

a = "           hi        "
print(a)
print(a.strip())

# %%
# 8) replace()
a = "Life is too short"
a.replace("Life", "Your leg")

# %%
# 9) split() : 문자열 나누기
# 기본 공백 기준으로 나눔
print(a.split())

b = "a:b:c:d"
print(b.split(":"))

# %%
# 10) splitlines() : 엔터 기준으로 나누기
c="하나\n둘\n셋"
print(c.splitlines())
print(c.split("\n"))

# %%
# 11) is~ : 문자열 구성 파악(True, False 로 결과 나옴)
print("1234".isdigit())
print("abcd".isalpha())
print("abc123".isalnum())
print("abcd".islower())
print("ABCD".isupper())
print("    ".isspace())

# %%
# 대 <=> 소
name = "KennRY"
print(name.swapcase())

for s in name:
    if s.islower():
        print(s.upper(),end="")
    else:
        print(s.lower(),end="")
# %%
# 년월일 입력받은 후 10 년 후 날짜 출력
# 2024/05/13 형식으로 입력
date1 = input("yyyy/MM/dd 형식으로 날짜 입력")
pos = date1.find("/")
year=int(date1[:pos]) + 10
print(f"입력한 날짜의 10년 후 {year}{date1[pos:]}")

# split 사용
date1 = date1.split("/")
print(f"입력한 날짜의 10년 후 {str(int(date1[0])+10)}/{date1[1]}/{date1[2]}")
# %%
# 사이트별 비밀번호 작성
# http://naver.com
# 규칙1 http:// 제외
# 규칙2 처음 나오는 . 이후 부분 제외
# 규칙3 남은 글자 중 첫 세자리+글자 개수+글자 내 'e' 문자 개수+'!' 로 구성
site = input("사이트 주소 입력")
siteName = site[7:site.find(".")]
print(siteName[:3])
print(len(siteName))
print(siteName.count("e"))

print(f"{siteName[:3]}{len(siteName)}{siteName.count("e")}!")

# %%
