### 출력함수 print()
# 출력해야 하는 내용을 넣어주면 됨

# 표준 출력
print('hello')
print('world')

#한줄 연결 출력
print('Hello', end='')
print('World!')

print('hello', 'World!')
# -> 중간에 변수가 들어가면 사용

print('hello' + 'world!')
# -> 하나의 문자열로 연산을 해서 출력하는 것도 가능

### 입력합수 input()
# 기억을 하기 위해서 변수에 저장

# 표준 입력
x = input()
# <- 기억을 하기 위해서 x라는 변수를 지정

x = input('x 입력 :')
# <- 메세지를 출력한 후 입력을 받게 함

x = input('x 입력 :')
y = input('y 입력 :')
print(x, '+' , y, '=', x+y) 
# '+' 연산자는 결합연산자!
# input에서 입력한 숫자를 문자로 받아들임

# 정수입력
x = int(input('x 입력 :'))

# 실수입력
x = float(input('x 입력 :'))

# !! 타입이 다를때는 형 변환 사용 !! #

### 변수
# 1. 영문, 숫자 사용 > 대소문자 구분
# 2. 숫자먼저 나오는 변수 사용 불가
# 3. 파이썬에 사용되는 키워드 사용 못함
# 4. 특수문자 사용 못함

### 기본산술 연산자
# 1. () 괄호
# 2. ** 지수연산
# 3. +,- 양수, 음수
# 4. *(곱셈), /(나눗셈), //(정수나눗셈), %(나머지)
# 5. +,- 덧셈, 뺄셈

### Python f-string 출력
# 'f' 라는 접두사를 통해 간단히 사용

x = int(input('x 입력 :'))
y = int(input('y 입력 :'))

print(f'{x} + {y} = {x+y}')
print(f'{x} - {y} = {x-y}')
print(f'{x} x {y} = {x*y}')

# 소수점 표현 1 : 소수점 4자리까지 표시
print(f'{x} + {y} = {(x/y):0.4f}')

# 소수점 표현 2 : 전체 10자리 중 소수점 4자리까지 표시
print(f'{x} / {y} = {(x/y):10.4f}')

# 나눗셈 => 결과 int(정수)
print(f'{x} / {y} = {x//y}')

# 나눗셈의 나머지
print(f'{x} % {y} = {x%y}')

# 거듭제곱
print(f'{x}의 {y}승 = {x**y}')

### 이스케이프 시퀀스
# \와 특정 문제를 결합하여 제어 문자를 표현

# \\ 백슬래시
# \' 작은따옴표 출력
# \" 큰따옴표 출력
# \n 엔터
# \t tab, 다음문자 출력

### 주석처리 여러줄
'''
주석처리합니다
주석처리는 작은따옴표 3개로 합니다.
'''

### 문제

# 섭씨온도를 입력받아서 화씨 온도로 변환하시오

'''
입력 => 섭씨온도 (실수)
출력 => 화씨온도 (공식)
'''
C = float(input('섭씨온도 입력'))
F = (C * (9/5)) + 32
print('섭씨온도 : ', C, '->', '화씨온도:', F)

