print("\n61번")
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

print("\n62번")
nums = [1,2,3,4,5,6,7,8,9,10]
print(nums[::2])

print("\n63번")
nums = [1,2,3,4,5,6,7,8,9,10]
print(nums[1::2])

print("\n64번")
nums = [1,2,3,4,5]
print(nums[::-1])

print("\n65번")
interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0], interest[2])

print("\n66번")
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(" ".join(interest))


print("\n67번")
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print("/".join(interest))

print("\n68번")
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print("\n".join(interest))

print("\n69번")
string = "삼성전자/LG전자/Naver"
interest = string.split("/")
print(interest)

print("\n70번")
data = [2,4,3,1,5,10,9]
data.sort()
print(data)
