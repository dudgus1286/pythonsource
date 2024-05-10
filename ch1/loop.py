# %%
# while / for
# ++, -- 은 사용 못함

i = 1
while i < 11:
    print(i)
    i += 1

# %%
# 1~100 사이의 짝수만 출력
i = 1
while i <= 100:
    if i % 2 == 0:
        print(i, end=" ")
    i += 1

# %%
# 1~100 합계 구한 후 출력
i = 1
sum1 = 0
while i <= 100:
    sum1 += i
    i += 1
print(f"1 ~ 100 합 : {sum1}")

# %%
# 6단 구구단 출력
i = 1
result = 0
while i <= 9:
    print(f"6 * {i} = {6 * i}")
    i += 1

# %%
# 사용자로부터 입력을 받은 후 화면 출력
# q 라는 문자 입력 시 입력 받는 것 중단

# str = ""
# while str != "q":
#     str = input("문자 입력")
#     print(str)

# break 사용 시
while True:
    data = input("데이터 입력")
    print(data)
    if data == "q":
        break

# %%
# for 변수명 in 범위:

# 범위를 지정하는 함수
range(5)  # range(0, 5) 0에서 시작해서 5 전까지
print(list(range(5)))  # [0, 1, 2, 3, 4]
print(list(range(1, 5)))  # [1, 2, 3, 4] 시작점 지정 가능
print(list(range(1, 11, 2)))  # [1, 3, 5, 7, 9] 2씩 증가

# %%
for i in range(1, 11):
    print(i, end=" ")

# %%
for i in range(1, 101, 2):
    print(i, end=" ")

# %%
# 1~100 합계 구하기
sum1 = 0
for i in range(1, 101):
    sum1 += i
sum1

# %%
# sum()
print(sum(range(1, 101)))
sum(range(1, 101, 2))
# 주피터의 경우 마지막 값의 경우 print() 없이도 화면 출력해줌

# %%
range(10, 1)
print(list(range(10, 0, -1)))  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# %%
# 사용자로부터 숫자 입력받은 후 1~ 사용자 입력 숫자까지 합계 구한 뒤 출력
num1 = int(input("숫자 입력"))

hap = 0
for i in range(1, num1 + 1):
    hap += i
print("1~{} 숫자 합 = {}".format(num1, hap))

# %%
num1 = int(input("숫자 입력"))
print("1~{} 숫자 합 = {}".format(num1, sum(range(1, num1 + 1))))

# %%
for s in "dream":
    print(s, end="-")

# %%
for i in range(3):
    for j in range(3):
        print(j, end=" ")
    print()

# %%
for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()

# %%
# 구구단 2~9단 출력

for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i} * {j} = {i*j}", end="\t")
    print()

# %%
# 파이썬 : 리스트 [] ==> 자바스크립트 : 배열 {}
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    print(num)

# %%
# break

i = 1
while i < 11:
    if i == 5:
        break
    print(i, end=" ")
    i += 1

# %%
# continue
i = 1
while i < 11:
    i += 1
    if i % 2 == 1:
        continue
    print(i, end=" ")

# %%
