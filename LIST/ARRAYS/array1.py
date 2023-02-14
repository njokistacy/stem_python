numbers=[9, 10, 2, 5]
x=numbers[0]
print(x)

#2.Assigning a different number to an index
numbers=[10,20,50,6]
numbers[2]=9
print(numbers)

#3.append
cars=["BMW","Porshe","Jeep"]
cars.append("Toyota")
print(cars)

#4.pop
numbers=[9, 11, 15, 16, 11]
print(numbers.pop(2))
print(numbers)
print("\n")
#5. finding the length of items in a list or characters in a string
length=len(numbers)
print(length)
#characters
print(len("cars"))
print("\n")
#6.Count
length=numbers.count(11)
print(length)
print("\n")
#7. Reverse
numbers.reverse()
print(numbers)

for i in numbers:
    print(i)

for i in range(3):
    print(i)