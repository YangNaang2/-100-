print("#21")
letters = 'python'
print(letters[0], letters[2])

print("\n#22")
license_plate = "24가 2210"
print(license_plate[4:])

print("#\n23")
string = "홀짝홀짝홀짝"
print(string[0],string[2],string[4])
print(string[::2])

print("\n#24")
string = "PYTHON"
print(string[::-1])

print("\n#25")
phone_number = "010-1111-2222"
print(phone_number)
phone_number1 = phone_number.replace("-", " ")
print(phone_number1)

print("\n#26")
phone_number = "010-1111-2222"
phone_number2 = phone_number.replace("-", "")
print(phone_number2)

print("\n#27")
url = "http://sharebook.kr"
url_split = url.split('.')
print(url_split[-1])

print("\n#28")
#lang = 'python'
#lang[0] = 'P'
#print(lang)
#문자열은 수정이 불가하므로 오류가 난다.

print("\n#29")
string = 'abcdfe2a354a32a'
string1 = string.replace("a", "A")
print(string1)

print("\n#30")
string = 'abcd'
string.replace('b', 'B')
print(string)
#문자열은 수정이 불가하므로 replace를 써도 기존에 넣은거 그래도 나온다.
