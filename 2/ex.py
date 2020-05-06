#리스트
#여러 개의 값을 한 곳에 모아서 저장한다. 그 값은 숫자, 문자, 리스트가 될 수 있다. 값을 변경할 수 있으며 값들은 순서를 가지고 있다. 
#[요소1, 요소2, ...]

my_list1 = []
my_list2 = [1, 2, 3]
my_list3 = ['a', 'b']

print(my_list1)
print(my_list2[2])
print(my_list3[0])


#리스트에 값 추가하기 : .append()

my_list1.append(123)
my_list1.append('abc')
my_list1.append(True)
print(my_list1)


#값에 접근하기 : 인덱싱(인덱스를 이용해서 리스트의 각 요소에 접근할 수 있다.)
print(my_list1[0])
print(my_list1[-1])

#값 제거하기 : 리스트에 있는 요소를 지운다 -> del (지워지면서 인덱스가 한개식 당겨진다.)
del my_list1[0]
print(my_list1)

#여러 값 가져오기 : 슬라이싱 (원본 리스트는 그대로 유지)
print(my_list2[:1])
print(my_list2[1:3])
print(my_list2[2:])

#값 정렬하기 : .sort() 
my_list4 = [5, 3, 6, 1]
my_list4.sort()
print(my_list4)
my_list5 = ['c', 'f', 'z', 'b']
my_list5.sort()
print(my_list5)

# 값의 개수 세기 : .count() (리스트 안에 값이 몇개 있는지 세준다)
my_list6 = ['a', 'a', 'a', 'b', 'b', 'c', 'c']
print(my_list6.count('a'), my_list6.count('b'), my_list6.count('c'), my_list6.count('d'))

#in과 not in : 리스트 안에 값이 있는지 없는지 확인, True, False로 돌려준다.
my_list6 = ['a', 'b', 'c', 'd']
print('a' in my_list6)
print('b' not in my_list6)

#튜플 : 여러 값을 모아놓은 것이지만 값을 변경 할 수 없다.
#(요소1, 요소2, ...)    //괄호 없이 사용해도 된다.

my_tuple1 = ()
my_tuple2 = (1, )   #값이 한 개 일때 튜플이라는 것을 알려주기 위해 괄호 사용.
my_tuple3 = ('a', 'b', 'c')
my_tuple4 = 3.14, 'Python', True

print(my_tuple1, my_tuple2, my_tuple3)
print(type(my_tuple3))

my_tuple5 = (1)
print(type(my_tuple5))


#패킹과 언패킹
#패킹은 여러개의 값을 하나로 묶는 것, 언패킹은 하나로 묶여 있던 값을 여러개로 푸는 것
my_tuple4 = 3.14, 'Python', True    #패킹
i, s, b = (123, 'abc', True)    #언패킹
print(my_tuple4)
print(i, s, b)