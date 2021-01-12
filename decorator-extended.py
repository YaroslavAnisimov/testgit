
def decorator1 (autoriz1):
    def wrapper_decorator(*args, **kwargs):
        autoriz1 (*args, **kwargs)
        complete = True
        user = {"some username" : "some password"}
        while complete:
        username = input("What is the username?")
        password = input("What is the password?")
        conf_username = Yarik
        conf_password = 12345
        if username != conf_username or password != conf_password:
            print("username or password does not match") 
            continue
        if password == conf_password or user_name ==  conf_username :
            print("User has been identified, Welcome",username)
            complete = True
        else:
            print("Input password again")
    return wrapper_decorator



print ("Menu:")
print("please make a selection.")
print("1. Number count. ")
print("2. Tell me Hi")
print("3. BMI calculator. You need to be autorized before using the service")

option = int(input("Please, make Your Selection  "))

if option == 1:
    def count(i):
        x = int(input("please enter a number"))
        for i in range(1, x+1):
            print (i)
            
if option == 2:
    print("Hi!:)")

if option == 3:
    @decorator1    
    def BMI(a, b, c):
        a = float(input('Please, enter your weight in kilograms?'))
        b = float(input('Please, enter your height in meters?'))
        c = a/(b*b)
        if c < 20:
            print('Your BMI is',c,'which means you are underweight!!!')
        if c >=20 and c <=30:
            print ('Your BMI is',c)
        if c > 30:
            print('Your BMI is',c,'which means you are obese!!!')
        else:
            print("Invalid command. Select from 1-3")
