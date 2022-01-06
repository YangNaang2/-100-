print("\n31번")
a= "3"
b= "4"
print(a+b)
#a,b가 문자열이므로 결과값은 34로 예상

print("\n32번")
print("Hi" * 3)
#문자열 3번 반복이므로 HiHiHi예상

print("\n33번")
a = "-"
print(a*80)

print("\n34번")
t1= 'python'
t2= 'java'
t3= t1 +" "+t2+ " "
print(t3*3)

print("\n35번")
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: %s 나이: %d" % (name1, age1))
print("이름: %s 나이: %d" % (name2, age2))

print("\n36번")
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: {} 나이: {}".format(name1, age1))
print("이름: {} 나이: {}".format(name2, age2))

print("\n37번")
name1= "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print(f"이름: {name1} 나이: {age1}")
print(f"이름: {name2} 나이: {age2}")

print("\n38번")
상장주식수 = "5,969,782,550"
a= 상장주식수.replace(",", "")
#지금 a 는 문자열 형태
b= int(a)
print(b, type(b))


print("\n39번")
분기 = "2020/03(E) (IFRS연결)"
print(분기[:7])

print("\n40번")
data = "   삼성전자   "
a= data.replace(" ", "")
print(a)
#or
data= "    삼성전자   "
a= data.strip()
print(a)
