# for num in range(2, 501):
#     for n in range(2, num):
#         if num % n == 0:
#             break
#     else:
#        print(num)

num = range (4,501)
list1 = [1,2,3]
for i in num:
    for j in range(2,i):
        if i%j==0:
             break
    else :
        list1.append(i)
print(list1)