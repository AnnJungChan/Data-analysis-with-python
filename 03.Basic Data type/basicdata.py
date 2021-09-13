### data type
# 데이터를 식별하는 분류
# 데이터가 가질 수 있는 값을 결정하고 연산을 제어
# int : 정수
# float : 실수
# bool : 참거짓 분류
# str : 문자형

x=10
print(f"{x}의 data type =>{type(x)}")

x=10.5
print(f"{x}의 data type => {type(x)}")

x=True
print(f"{x}의 data type => {type(x)}")

x='python'
print(f"{x}의 data type => {type(x)}")

### 연산자
# 자료를 처리하는 기호

# 산술연산자
# 수학적 계산
# 사칙, 제곱, 나머지, 나누기 결과 정수(//)

# 비교연산자
# 비교할 때 사용
# 등호(==), 같지 않음(!=), 부등호
# 할당(assign)연산자와는 다름!

# 논리연산자
# TRUE, FALSE
# 논리곱(and) : 조건들이 다 맞아야 참
# 논리합(or)  : 조건에 하나라도 맞으면 참
# not : 참이면 거짓, 거짓이면 참을 돌려줌

# 할당연산자
# = , 오른쪽의 값을 왼쪽의 변수로 할당
# +=,-=,*=, /=, %=, //=
# x = x+10
# x+=10

### 문자열 연산
# 문자열 더하기(+)
# 문자와 문자를 붙여줌

# 문자열 곱하기(*)
# 문자열을 반복해서 보여줌

# 문자열 인덱싱
# 문자를 처음부터 번호를 붙임
# 처음위치[0], 마지막위치[-1]

# x[0] : x 벡터의 첫번째를 추출하라

# 인덱스 슬라이싱
# [인덱스1:인덱스2]
# 인덱스 1의 위치에서 인덱스 2위치까지 추출
# [인덱스1:]
# 인덱스1에서 끝까지 추출
# [:인덱스1]
# 처음부터 인덱스1까지 추출

### 문자열 함수
# len() : 문자열 길이 구하기

# count() : 문자의 개수 구하기

# find() : 문자가 처음 나오는 위치 반환
# -> 없으면 -1을 반환함

# index() : 문자가 처음 나오는 위치 반환
# -> 없으면 오류 ## 그냥 find()써라

# join() : 문자열 사이에 문자 삽입
# -> '삽입문자'.join(문자열)

# upper() : 소문자 대문자 변환

# lower() : 대문자를 소문자로 변환

# replace() : 문자열 바꾸기
# -> replace(원본, 변환문자)

# split() : 문자열 나누기
# 인수가 없으면 공백을 기준


### 실습

# 할당 연산자
x = 10
y = 2.5

print(type(x))
print(type(y))
print(f"what is datatype of {x} ?", "=>", type(x))
print(f"what is datatype of {y} ?", "=>", type(y))

# 산술연산자
print(f'{x}//{y} = {x//y}')

# 산술연산자와 할당연산자 동시사용
z=x+10
print(f'x={x}, z={z}')
x = x+10
x += 10 

# 비교연산자
print(x>=y)
print(x<=y)

# 논리연산자
print((x>y) or (x<y))
print((x>y) and (x<y))
z=True
print(z)
print((x>y) and z)

# 논리합
print(f'True or True = {True or True}')
print(f'True or False = {True or False}')
print(f'False or True = {False or True}')
print(f'False or False = {False or False}')

# 문자열 더하기
x = "hello"
y = "world!"
print(x+y)

# 문자열 곱하기
print("-"*50)

# 문자열 인덱싱
print(x[3]) 
# 네번째 있는 문자가 먼지 알려줌
# 처음 시작은 무조건 "0" 이다!!

print(x[0])
# 처음

print(x[-1])
# 마지막

# 문자열 슬라이싱
print(y[0:2])
# 0에서 2미만인 문자만 뽑아내라!
print(y[:2])
# 처음부터 2미만까지!
print(y[2:])
# 세번째부터(2초과부터) 마지막까지!

# 문자열 길이구하기
print(len(x))
print(x[len(x)-1])
# 전체길이-1하면 0부터 인덱싱되는 문자의 마지막을 말함
# 마지막 문자가 출력됨

# 문자열 개수 구하기
print(x.count("o"))
print(x.count("he"))

# 문자가 처음 나오는 위치 방향
print(x.find("o"))
print(x.find("k")) # -1 반환
print(x.index("o"))
print(x.index("k")) # 오류가 나옴

# 문자열 사이에 문자 삽입
print('-'.join(x)) # 사이사이에 모두 삽입됨

# 대문자를 소문자로 변환
print(x.upper())
print(x.lower())

# 문자열 바꾸기
print(x.replace("he", "*"))

# 문자열 나누기
print(x.split("e"))