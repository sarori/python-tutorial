print("hello world");

#숫자형 자료형
print(4096)

#사칙연산
print(1 + 2)
print(3 ** 4)

#제곱, 몫, 나머지 연산자
print(1 ** 2)
print(3 // 4)
print(5 % 6)

# 변수
my_int = 1
my_str = 'python'
my_bool = True
my_list = [1, 2, 3]

print(my_bool)

#복합 할당 연산자 : += -+ *= /=
count = 0
count += 1
count -= 5
count *= 2
print(count);

#뱐수 이름
my_int1 = 1
# 1my_int2 = 2 #syntax_error-> 변수명은 숫자로 시작할 수 없다.
print(my_int1)


A = 1   #대, 소문자 구분한다.
print(A)
a = 2
print(a)

#문자열
my_str1 = 'a'
my_str2 = '3.14'
my_str3 = 'coding'
my_str4 = "coding"
print(my_str1, my_str2, my_str3, my_str4)
print(type(my_str2))

#문자열 연산하기 + : 문자열끼리 연결, *: 반복할때 사용
my_str5 = 'a' + 'b' + 'c'
my_str6 = 'cod' + 'ing'
my_str7 = 'abc' * 4
my_str8 = '=' * 10
print(my_str5, my_str6, my_str7, my_str8)
print(my_str7 + my_str6)

#인덱싱
alphabet = 'abcde'
print(alphabet[0], alphabet[3], alphabet[4])

#뒤에서부터 인덱싱
print(alphabet[-1], alphabet[-4], alphabet[-5])

#여러가지 문자 가져오기 - 슬라이싱(앞의 숫자부터 끝 숫자 바로 전까지)
print(alphabet[1: 4])

#숫자 생략하기
print(alphabet[:3])
print(alphabet[3: ])

#문자열 분리하기 : string에서 사용하는 method .split()
#메소드는 특정 자료형만 사용할 수 있는 함수를 말한다.
fruit_str = 'apple banana lemon'
fruits = fruit_str.split()
print(fruits[0])
print(fruits[1])

#문자열 포맷팅 : .format() -> format 괄호 안에 있는 문자열이 {} 안으로 들어온다.
print('Life if {}' .format('Short!'))
print('{}x{}={}' .format(2, 3, 2 * 3))

#여러줄 문자열(엔터 쳐도 에러 나지 않는다.)
print('''첫번째
두번째
세번째''')

#출력의 끝 지정하기 
print("coding", end='') #줄바꿈 없어짐
print("coding", end="-") #- 뒤에 붙는다
print("coding", end="\n")
print("coding", end="\t")

#이스케이프코드 \n, \t
print("coding\ncoding")
print("tab\ttab")

print('\\n') #\n, \t 자체를 출력하고 싶을 경우
print('\\t')
print('I\'m Yours')

#C스타일 포맷팅
# %d(정수) %f(실수) %s(문자열)
print('Life is %s' % 'Short')
print('%d x %d = %d' % (2, 3, 2 * 3))

#주석 : 컴퓨터는 보지 못함. 사람이 코드를 이해하는 것을 돕기 위해 사용함.
# 