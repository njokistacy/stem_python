#for random list generation you have to import randint from random
from random import randint
nums=[]
for i in range(5):
    num=randint(1, 100)
    nums.append(num)

print(nums)
