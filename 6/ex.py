#dictionary : 관련된 정보를 서로 연관시켜 놓은것, 키-값을 쌍으로 저장하는 자료형
#{키1: 값1, 키2: 값2,}
#dictionary에서 키로 사용할 수 있는 것은 immutable이다. => 숫자, 문자, 튜플
#dictionaty에서 값으로는 모든 값을 사용할 수 있다. 
my_dict1 = {1: 'a', 2: 'b'}
my_dict2 = {'a': 1, 'b': 2}
my_dict3 = {1: 'a', 'b': 2}

print(my_dict1, my_dict2, my_dict3)


#dictionary에 값 추가하기 => 키와 값 쌍을 이뤄서 저장해야한다.
my_dict = {}
my_dict[1] = 'a'
my_dict['b'] = 2
my_dict['c'] = 'd'
print(my_dict)

#dictionary에서 값을 접근하기, 가져오기 => 키를 이용해서 값을 가져온다.
print(my_dict[1], my_dict['b'], my_dict['c'])

#dictionary에서 값 제거하기 => del과 키를 이용해서 제거한다.
del my_dict[1]
del my_dict['b']
del my_dict['c']
print(my_dict)

#dictionary method
#.values() => dictionary에서 값들만 뽑아온다.
my_dict4 = {'k1': 'v1', 'k2': 'v2'}
for val in my_dict4.values():
    print(val)

#.keys() => dictionary에서 키만 뽑아온다.
for key in my_dict4.keys():
    print(key)

#items() => dictionary에서 key와 value를 모두 뽑아온다.
for key, val in my_dict4.items():
    print(key, val)