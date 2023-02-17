person = {
    "name" : "cathy",
    "age" : 23,
    "pets" : {
                 "dog": "x",
                 "cat": "y"
    }
}
#accessing dictionary items
print(person["pets"])
profile = {}
profile["username"] = "user123"
profile["age"] = 20
profile["email"] = "user123@gmail" 
print(profile)    


  
def register():
    username = input("Enter username:")
    email = input("Enter email:")
    password = input("Enter password:")
    #store in a dictionary
    profile["username"] = username
    profile["email"] = email
    profile["password"] = password
def get_profile():
    #print the user profile
    print(profile)
def change_username():
    new_username = input("Enter new username")
    profile["username"] = new_username
    
register()
get_profile()

change_username()
get_profile()






















