# 딕셔너로 == Map
# list 와 같이 쓰이는 자료형
# key, value
# {}

# %%
# 생성
dict1 = {}
dict2 = {"name": "Song", "age": 12}
dict3 = {0: "Hello Python", 1: "Hello Coding"}
dict4 = {"arr": [1, 2, 3, 4, 5]}

# %%
print(dict2)
print(dict3)
print(dict4)

# %%
print(dict2["name"])
print(dict3[0])
print(dict4["arr"])

# %%
# dict1["addr"]
# KeyError: 'addr'

# %%
dict1.get("addr")
# 해당 key 가 없어도 오류 안 남

# %%
print(dict1)

# %%
# 데이터 추가 - 키와 값의 형태로 추가
dict2["birth"] = "0514"
dict2

# %%
dict3[2] = ["Hello Java", "Hello Oracle"]
dict3

# %%
# dict4 에 rank => 튜플 (16,17,18)
dict4["rank"] = (16, 17, 18)
print(dict4)

# %%
numbers = [1, 2, 6, 8, 4, 3, 2, 1, 9, 7, 2, 1, 3, 5, 4, 8, 9, 7, 2, 3]
counter = {}
# {1: 3, 2:4, ...} 숫자의 반복횟수 담기
num = 1
# while num <= 9:
#     counter[num] = numbers.count(num)
#     num += 1
for num in numbers:
    counter[num] = numbers.count(num)

print(counter)

# %%
# 삭제
del dict2["birth"]
dict2

# %%
# 1) keys() : key 리스트를 리턴
dict2.keys()
# dict_keys(['name', 'age'])

# %%
# 2) values()
dict2.values()
# dict_values(['Song', 12])

# %%
# 3) items() : key,value 쌍으로 리턴
dict2.items()
# dict_items([('name', 'Song'), ('age', 12)])
# [[('키','값'), ()]]

# %%
for k in dict2.keys():
    print(k)

# %%
for k, v in dict2.items():
    print(k, v)

# %%
# in : 해당 key 값이 있는지 확인
"name" in dict1  # False
"name" in dict2  # True

# %%
# clear() : key, value 전부 제거
dict2.clear()
dict2

# %%
q1 = {"봄": "딸기", "여름": "토마토", "가을": "사과", "겨울": "귤"}

# 가을에 해당하는 과일 출력
print(q1.get("가을"))
# for 문의 경우
for k in q1.keys():
    if k == "가을":
        print(q1[k])

# 사과가 포함되었는지 확인
print("사과" in q1.values())

str = "사과가 포함됨" if "사과" in q1.values() else "사과가 포함되지 않음"
str

# %%
