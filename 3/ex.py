#횟수로 반복하기
# 조건을 기준으로 반복하는 방법 => while
# 횟수를 기준으로 반복하는 방법 => for

# for 변수 in 순서열:
#     실행할 명령 1
#     실행할 명령 2
#     ...

my_list = [1, 2, 3]
for count in my_list:
    print('count is', count)


#interactive mode / IDLE editor mode

#문자열 반복하기
my_str = 'coding'
for letter in my_str:
    print('letter is', letter)  #한 글자씩 실행한다.


#range(stop) : 순서열을 만들어준다
for count in range(3):
    print('count : ', count)

#range(start, stop) : start값은 시작값, stop은 끝 깞, start부터 stop전까지 입력값을 만들어준다.
for count in range(1, 3):
    print('count', count)


#for 중첩하기
for j in range(2):
    for i in range(2):
        print('i: {}, j: {}'.format(i, j))

#list comprension 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = []
for number in numbers:
    if number % 2 == 1 :
        odd_numbers.append(number)
        print(odd_numbers)

odd_numbers = [number for number in numbers if number % 2 == 1]