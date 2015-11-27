# encoding=utf-8

print('Hello World!2')

a=1
print(a)

s1=(1,2,3,4,5,6,7,8,9,'2www')
print(s1,type(s1))

s2=[2,['3ew',True]]
print(s2,type(s2))

print(s1[4])
print(s2[1][1])
 
s2[0]='青春若是一场天真的固执，你则是我最在乎的坚持。'
print(repr(s2))

print(open("Test.txt").read())

print(s1[: 3])
print(s1[3 :])
print(s1[0:7:2])
print(s1[9:4:-1])
print(s1[3:-1])
print(s1[3:-3])


aa='qwewretrete234252sgsgsgadgs124r'
print(aa[3:7])
print(aa[0::3])


print(3**32) #乘方

print(32%3) 
print(524/24) 

print(5 in [1,3,6,5])
print(not False)