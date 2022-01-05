# nums = []
# total = 0
# while 1:
#     num = input("점수를 입력하세요 : (더 이상 입력할 점수가 없으면 -1입력)")
#     if num == "-1":
#         break
#     nums.append(num)
# for i in nums:
#     total += int(i)
# print("모든 정수의 합은 {}이고, 평균은 {}이다.".format(total, total/len(nums)))

li = list(map(int, input("값을 간격띄워서 입력하세요 : ").split()))
print(sum(li))