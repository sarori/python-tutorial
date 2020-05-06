#조건으로 반복하기 : while
# while 조건:
#     실행할 명령1
#     실행할 명령2

count = 0
while count < 3:
    print('Count:', count)
    count = count + 1


#continue : 반복문에서 continue를 만나면 아래의 명령을 수행하지 않고 다시 조건문으로 돌아간다.
count = 0
while count < 5 :
    count = count + 1
    if count % 2 == 1:
        continue
    print(count)

#break : 조건과 상관없이 반복문을 종료합니다.
while True:
    name = input('What is your name?')
    if name == 'finish':
        print('finish')
        break
    print('Hello, {}'.format(name))


#input() : 입력값은 항상 문자열을 받아온다.
name = input('Enter your name: ')
print('Hi, {}!'.format(name))

#type() : 자료형 확인 할 수 있다.
print(type(name))


#자료형 바꾸기 : int(), float(), list(), str()
age = int(input('Enter your age : '))
print('{} years old!'.format(age - 3))
print(float(1))
print(int(1.0))
print(list('saro'))
print(str(['a', 'b', 'c']))