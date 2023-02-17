# username=input("Enter your username:")

# def username_function(username):
#  print("Hello " + username.upper())

# username_function(username)

#assignment: having a list of strings with emails and determine which ones are from which mail servers
for email in range(3):
    email=input("Enter your email:")
    if email[-9:]=="gmail.com":
         print("From Google mail")
    else:
         print("Not from Google mail")