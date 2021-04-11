#ödev2:1

Username="Yeşim"

Password="abc"

Username1 = (input("Please enter your username: "))

Password1 = (input("Please enter your password: "))

if (Username != Username1 and Password == Password1):
    print("Your username is wrong")
elif (Username==Username1 and Password != Password1):
    print("Your password is wrong")
elif (Username != Username1 and Password!= Password):
    print("Your username ve password are wrong .")
else:
    print("Congrutulations !, You are successful ")

