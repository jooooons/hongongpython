from math import *
r = float(input("반지름을 입력하세요 : "))
l = round(2 * pi * r, 2)
s = round(pi * r * r, 2)
print("둘레의 길이는 {}이고, 면적은 {}입니다.".format(l,s))