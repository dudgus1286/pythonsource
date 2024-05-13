# %%
# 숫자, 문자열

# 데이터 모임 표현 : list(== ArrayList(배열)), dict(== Map), set(== HashSet), tuple
# 동일한 타입만을 담지 않음

# %%
# list 생성
list1 = []
list2 = [1, 2, 3, 4, 5, 6]
list3 = [1, "a", 3, "b", 5, 6]
list4 = [1, 2, 3, 4, 5.5, 6.5]
list5 = [1, 2, 3, 4, ["Life", "is", "short"]]
list6 = list([3, 4, 5])


# %%
# 출력
print(list2)

# %%
# 리스트 인덱싱 / 슬라이싱
print(list2[2])
print(list3[-2])
print(list4[-1])
print(list5[-1])
print(list5[4][0])
print(list5[4][-1])

# %%
list7 = [1, 2, 3, 4, ["a", "b", ["Life", "is"]]]
# is 출력
print(list7[-1][-1][-1])

# %%
print(list2)
print(list2[2:4])
print(list2[:4])
print(list2[:-1])

# %%
print(list5)
print(list5[4:])
print(list5[4][:2])
# print(list5[4:2]) == []

# %%
# 연산자
# + : 연결
print(list2 + list3)
print(list5 + list6)
print(list2[1] + list3[0])
# 요소 + 요소 : 산술

# %%
# * 반복
print(list2 * 2)

# %%
# len() : 길이
len(list2)

# %%
# 리스트 수정 / 삭제
list2[0] = 7
print(list2)

# 리스트 안에 리스트 추가 가능
list2[1] = [10, 11, 12]
print(list2)

# 요소 개별 삭제
del list2[1]
print(list2)

# 지정 범위 삭제
del list2[2:]
print(list2)

# %%
for i in list3:
    print(i, end="\t")

# %%
numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]
# 100 이상의 수만 출력
for i in numbers:
    if i >= 100:
        print(i, end=" ")

# %%
# 홀짝 구분하여 출력
for i in numbers:
    if i % 2 != 0:
        print(str(i) + "(홀수)")
    else:
        print(str(i) + "(짝수)")

# %%
# 숫자의 자리수 출력
for i in numbers:
    print("{} : {}".format(i, len(str(i))))

# %%
# 함수
# 1) append() : 리스트에 요소 추가하기
list3.append(["c", "d", "e"])
print(list3)
list3.append(5)
print(list3)

# %%
# 1~100 까지 숫자 중 짝수만 리스트로 생성
even = []
# for i in range(1,101):
for i in range(2, 101, 2):
    even.append(i)
print(even)

# %%
# 2) sort() : 오름차순 정렬 (리스트 원본 순서 변경)
a = [1, 4, 3, 2]
a.sort()
print(a)

a = ["a", "e", "g", "b", "c"]
a.sort()
print(a)

a = ["ㅎ", "ㄱ", "ㅈ", "ㅁ", "ㅋ"]
a.sort()
print(a)

# %%
# 3) reverse() : 리스트 뒤집기 (리스트 원본 순서 변경)
print(list4)
list4.reverse()
print(list4)

# %%
# 4) index() : 인덱스 값 리턴

list4.index(3)
list4.index(6)

# %%
# 5) remove() == del 요소지정
# 처음 만나는 요소 제거

# list4.remove(4)
# print(list4)
list4.append(5.5)
print(list4)

list4.remove(5.5)
print(list4)

# %%
# 6) pop(): 맨 마지막 리스트 요소 꺼내기
list4.pop()
list4

# %%
# pop(인덱스번호) : 인덱스 요소 꺼내기(== 제거)
list4.pop(1)
list4

# %%
# 7) count(찾을요소) : 찾을 요소 숫자개수를 리턴
list4 = [12, 13, 14, 15, 14]
list4.count(14)

# %%
# 8) extend() : 확장(+)
list4.extend([16, 17, 18])
list4

# %%
# 9) clear() : 리스트 요소 모두 삭제
list4.clear()
list4

# %%
# 내림차순 정렬
numbers.sort(reverse=True)
numbers

# %%
# 거짓에 해당 : "", [], ()(튜플), {}(딕셔너리), 0
city = ""
list8 = []

if city:
    print("비어있지 않음")
else:
    print("비었음")

if list8:
    print("비어있지 않음")
else:
    print("비었음")

# %%
fruits = ["딸기", "바나나", "사과", "배", "수박"]

# in == SQL에서의 in 연산자와 동일 개념
if "딸기" in fruits:
    print("딸기 요소가 포함됨")

print("메론" not in fruits)
# True

# %%
a_class = [70, 60, 55, 75, 92, 80, 85, 100, 87, 65]

# a_class 평균과 총합 구하기
total = 0
for i in a_class:
    total += i

print("a_class의 총합:", total)
print("a_class의 평균:", total / len(a_class))

# %%
# sum()
print(f"총합 : {sum(a_class)}, 평균 : {sum(a_class)/len(a_class)}")

# %%
