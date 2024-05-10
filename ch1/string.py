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
