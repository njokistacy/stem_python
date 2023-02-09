number=eval(input("enter number:"))
if number < 0:
    print("wrong input,number is negative")
else:
    if number>50:
        result=number/2
        print(result)
    else:
        print("number is less than 50")