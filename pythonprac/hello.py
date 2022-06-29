# 변수 , 기본연산
a = 3      # 3을 a에 넣는다
b = a      # a를 b에 넣는다
a = a + 1  # a+1을 다시 a에 넣는다

num1 = a*b  # a*b의 값을 num1이라는 변수에 넣는다
num2 = 99  # 99의 값을 num2이라는 변수에 넣는다


# 자료형
name = 'bob'  # 변수에는 문자열이 들어갈 수도 있고,
num = 12  # 숫자가 들어갈 수도 있고,

is_number = True  # True 또는 False -> "Boolean"형이 들어갈 수도 있습니다.

# 리스트형
a_list = []
a_list.append(1)     # 리스트에 값을 넣는다
a_list.append([2, 3])  # 리스트에 [2,3]이라는 리스트를 다시 넣는다


# a_list의 값은? [1,[2,3]]
# a_list[0]의 값은? 1
# a_list[1]의 값은? [2,3]
# a_list[1][0]의 값은? 2


# Dictonary 형
a_dict = {}
a_dict = {'name': 'bob', 'age': 21}
a_dict['height'] = 178

# a_dict의 값은? {'name':'bob','age':21, 'height':178}
# a_dict['name']의 값은? 'bob'
# a_dict['age']의 값은? 21
# a_dict['height']의 값은? 178


# Dictonary + list 형
people = [{'name': 'bob', 'age': 20}, {'name': 'carry', 'age': 38}]

# people[0]['name']의 값은? 'bob'
# people[1]['name']의 값은? 'carry'

person = {'name': 'john', 'age': 7}
people.append(person)

# people의 값은? [{'name':'bob','age':20},{'name':'carry','age':38},{'name':'john','age':7}]
# people[2]['name']의 값은? 'john'

# 함수


def f(x):
    return 2*x+3


def sum_all(a, b, c):
    return a+b+c


def mul(a, b):
    return a*b


result = sum_all(1, 2, 3) + mul(10, 10)


# 조건문
def oddeven(num):  # oddeven이라는 이름의 함수를 정의한다. num을 변수로 받는다.
    if num % 2 == 0:  # num을 2로 나눈 나머지가 0이면
        return True   # True (참)을 반환한다.
    else:            # 아니면,
        return False  # False (거짓)을 반환한다.


result = oddeven(20)


def is_adult(age):
    if age > 20:
        print('성인입니다')    # 조건이 참이면 성인입니다를 출력
    else:
        print('청소년이에요')  # 조건이 거짓이면 청소년이에요를 출력


is_adult(30)


# 반복문
fruits = ['사과', '배', '감', '귤']

for fruit in fruits:
    print(fruit)  # 사과 배 감 귤

fruits = ['사과', '배', '배', '감', '수박', '귤', '딸기', '사과', '배', '수박']

count = 0
for fruit in fruits:
    if fruit == '사과':
        count += 1

print(count)


def count_fruits(target):
    count = 0
    for fruit in fruits:
        if fruit == target:
            count += 1
    return count


subak_count = count_fruits('수박')
print(subak_count)  # 수박의 갯수

gam_count = count_fruits('감')
print(gam_count)  # 감의 갯수

# 딕셔너리 예제
people = [{'name': 'bob', 'age': 20},
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7},
          {'name': 'smith', 'age': 17},
          {'name': 'ben', 'age': 27}]


for person in people:
    print(person['name'], person['age'])


def get_age(myname):
    for person in people:
        if person['name'] == myname:
            return person['age']
    return '해당하는 이름이 없습니다'


print(get_age('bob'))
print(get_age('kay'))
