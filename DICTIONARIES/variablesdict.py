# Info={
#       "name":"Stacy",
#       "town":"Juja",
#       "school":"JKUAT"
#       }
# print(Info.get("name"))
# #updating a dictionary
# Info.update({"town":"Nairobi"})
# print(Info["town"])

# # #for printing all the values in the keys of a certain variable
# # for x in Info:
# #     print(Info[x])

# #do not write a list on one line
# student={
# "student1":{"name":"Stacy",
#             "town":"Nairobi"},
# "student2":{"name":"Dennis",
#             "town":"Kabete"}
# }
# print(student["student1"]["name"])
# print(student["student2"]["town"])

#creating your own functions
# def my_function(first_name):
#     first_name =(input("Enter your name:"))     
#     print(first_name +" hello" )
# my_function("first_name")

num1=eval(input("enter num 1:"))
num2=eval(input("enter num 2:"))

def sum(num1,num2):
    sum_of_numbers=num1+num2
    print(sum_of_numbers)

sum(num1,num2)

