# list=eval(input("enter a list of numbers:"))
# print(list)
# print("\n")
# print(max(list))
# list.reverse()
# print('Reversed List:',list)

#correction
nums=[] 
list_length=4

for i in range(list_length):
    number=eval(input("Enter a number:"))
    nums.append(number)
for number in nums:
    print(number)
print(nums)

print(nums[-1])

#getting the second largest or second smallest
# first you sort
nums.sort()
#second largest will be the second last item in the sorted list
print(nums)
#getting the second
