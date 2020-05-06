#function
#반복 되는 것들을 모아서 이름을 붙인 것.

#함수 만들기
# def 함수이름 (인자 1, ...):
#     실행할 명령1
#     실행할 명령1
#     ...
#     return 결과1, 결과2, ...

def my_sum(n1, n2):
    return n1 + n2
print(my_sum(1, 2))

#함수의 종류
# 내장함수 : built-in function 별도의 작업없이 이름을 불러 사용할 수 있다.
# 모듈의 함수 : 미리 만들어 놓은 것들을 사용할 수 있다.
# 사용자 정의 함수 : 직접 만들어 사용할 수 있다.

#함수를 사용하는 이유
#다시 사용할 수 있다. 코드를 관리하기 쉬워진다. 작은 단위로 만들어서 조립해서 사용할 수 있다. 

#여러개 돌려주기 : 겉으로는 여러값 돌려주는 것으로 보이지만 실제로는 하나의 값이다. (튜플)
def my_sum_mul(n1, n2):
    return n1 + n2, n1 * n2
s, m = my_sum_mul(2, 3)
print('s: ', s, 'm: ', m)
result = my_sum_mul(2, 3)
print(result)   #결과값 튜플로 나온다.

#Docstring : 함수가 어떤 일을 수행하는지 설명할 때 사용하는 주석
# def sum_mul(num1, num2):
#     """입력 값을 더하고 곱합니다."""
#     return num1 + num2, num1 * num2


#module : 비슷한 함수들을 모아놓은 파일
#import를 사용해서 모듈을 가져올 수 있다.
#.을 사용해서 모듈에 포함된 함수들을 사용할 수 있다.


#random : 난수를 만들거나 무작위와 관련한 함수를 포함하는 모듈이다.
#.choice() : 리스트의 값 중 하나를 랜덤하게 선택한다.
import random
fruits = ['apple', 'banana', 'lemon']
my_fruit = random.choice(fruits)
print(my_fruit)


#.sample() => 리스트의 값들 중 지정한 개수만큼 중복없이 랜덤하게 선택한다. 몇 개의 값을 중복없이 선택할지도 넣어줘야한다. 
import random
my_fruit = random.sample(fruits, 2)
print(my_fruit)

#.randint() => 정해진 범위내에서 정수 하나를 무작위로 선택해준다.
import random
my_int = random.randint(0, 10)
print(my_int)