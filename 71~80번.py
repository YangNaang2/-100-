print("\n 71번")
my_variable = ( )

print("\n 72번")
movie_rank = ("닥터 스트레인지", "스플릿", "럭키")

print("\n 73번")
my_tuple = (1)

print("\n 74번")
t = (1,2,3)
#t[0] = 'a'
##튜플은 수정이 불가능하다.

print("\n 75번")
t= 1,2,3,4
# 튜플은 괄호가 있어야하지만 없어도 가능함.

print("\n 76번")
t= ('a', 'b', 'c')
#t = ('A', 'b', 'c')로 바꾸려면 하나만 수정은 불가능. 재정의 해야함
t= ('A', 'b', 'c')

print("\n 77번")
interest = ('삼성전자', 'LG전자', 'SK Hynix')
data = list(interest)

print("\n 78번")
interest = ['삼성전자', 'LG전자', 'SK Hynix']
data = tuple(interest)

print("\n 79번")
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)

print("\n 80번")
#1~99까지 짝수만 저장된 튜플 생성하기
data = tuple(range(2, 100, 2))
print(data)
