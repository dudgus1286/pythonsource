# set(집합)
# 중복을 허용하지 않음
# 순서 없음 : 인덱싱을 할 수 없음

# %%
# 생성
set1 = set()
set2 = set([1, 2, 3, 4])
set3 = set([1, 4, 5, 6, 6])

# %%
print(set2)
print(set3)

# %%
# 리스트나 튜플로 변환 : 인덱싱이 필요하다면
# list(), tuple()
list1 = list(set2)
t1 = tuple(set3)
print(list1)
print(t1)

# %%
# 문자열 => set
set4 = set("abcdefg")
print(set4)
# {'a', 'b', 'c', 'd', 'e', 'f', 'g'}

# %%
# dict => set
dict1 = {"no": 1, "name": "hong", "age": 25}
set(dict1)
# {'age', 'name', 'no'}

# %%
list1 = [1, 2, 3, 4, 5]
set(list1)

# %%
# 교집합, 합집합, 차집합
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# 교집합
print(s1 & s2)
print(s1.intersection(s2))

# 합집합
print(s1 | s2)
print(s1.union(s2))

# 차집합
print(s1 - s2)
print(s1.difference(s2))

# %%
# add() : 하나만 추가
s1.add(7)
s1

# %%
# update() : 여러 개 추가하기
s1.update([9, 10, 11])
s1

# %%
# remove() : 제거
s1.remove(2)
s1

# %%
