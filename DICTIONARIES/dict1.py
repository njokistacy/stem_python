# def average (a, b):
#     av=(a+b)/2
#     return av
#     #will work because it is inside the function
#     print(av)
# #when run it will give an error because av which is a local variable has een outside the function(it is outside it"s scope)

# # print(av)

# cars= {
#     "model":"ford",
#     "year":1989,

# }
# person={
#     "name":"cathy",
#     "age":23,
#     "pets":{
#         "dog":"Scooby",
#         "cat":"Sally"}
#     }
# # accessin dictionary items
# print(person["pets"]["dog"])

#create an empty dictionary first
# profile={}
# profile["username"]="user123"
# profile["age"] =20
# profile["email"]= "user123@gmail.com"

# print(profile)

profile={}

def register():
    #ask for username
    username=input("Enter your username:")
    email=input("Enter your email:")
    #ask for password
    password=input("Enter password:")
    #store in a dictionary
    profile["username"]=username
    profile["email"]=email
    profile["password"]=password
register()
def get_profile():
    print(profile)

def change_username():
    new_username=input("Enter new username:")
    profile["username"]=new_username
get_profile()
change_username()
get_profile()

    