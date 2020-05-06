#조건 판단하기
#논리 자료형

#논리형 : True, False
my_bool1 = True
my_bool2 = False
my_bool3 = 1 < 3
my_bool4 = 1 == 2
print(my_bool1, my_bool2, my_bool3, my_bool4)

#비교 연산자 : ==, !=, >, <, >=, <=
my_cmp1 = 1 < 2
my_cmp2 = 1 == 2
my_cmp3 = 2 <= 1
my_cmp4 = 1 <= 2 < 3
print(my_cmp1, my_cmp2, my_cmp3, my_cmp4)

#논리 연산자 : and, or, not
my_con1 = 1 < 2 and 2 < 3
my_con2 = 1 < 2 and 2 < 1
my_con3 = 1 < 2 or 2 < 1
my_con4 = not 1 == 1
print(my_con1, my_con2, my_con3, my_con4)

#if
# if 조건:
#     실행할 명령1
#     실행할 명령2
#     ...

name = 'Lefty'
if name == 'Lefty':
    print('You\'re Lefty.')
    print('Nice to meet you')


#else와 elif
# if 조건:
#     실행할 명령1
#     실행할 명령2
# elif 조건:
#     실행할 명령1
#     실행할 명령2
# else:
#     실행할 명령1
#     실행할 명령2

name = 'Bob'
if name == 'Alice':
    print('You\'re Alice.')
elif name == 'Bob':
    print('You\'re Bob.')
else:
    print('Who are you?')