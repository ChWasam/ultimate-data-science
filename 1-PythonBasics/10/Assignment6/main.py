## Signup and login  but it will use classes and object 

# 1. ask user to login or signup
# 2. if login then ask for username and password 
# 3. then check username and password is correct or not 
# 4. Once user logged in you will ask user to post. it will be string only. Then you will get a message posted 
# 5. If user want to see all post it will be another method. see all post ()
# 6. if signup then take username and password and store it 

# user.login(username,password)
# user.post(post, id)
# user.see_all_posts(id)
# user.signup(username,password)

from user import User


user= User()


choice1 = int(input("Press 1 for login and Press 2 for signup : "))
if choice1 == 1:
    username = input("Enter username :")
    password = input("Enter Password :")
    login_result = int(user.login(username,password) )
    if login_result:
        choice2 = int(input("Press 1 for new post and Press 2 to see all previous posts : "))
        if choice2 == 1:
            post = input("Enter what you want to post")
            user.post(post, int(user.login(username,password)))
        elif choice2 == 2:
            all_posts = user.see_all_posts(int(user.login(username,password)))
            print(all_posts)
        else:
            print(" Enter correct choice ")

elif choice1 == 2:
    id = input("Enter id :")
    username = input("Enter username :")
    password = input("Enter Password :")
    signup = user.signup(id,username,password)
    print(signup)

else:
    print(" Enter correct choice ")

