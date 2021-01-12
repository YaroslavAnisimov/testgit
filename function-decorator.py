
def decorator(autoriz):
    def wrapper_decorator(*args, **kwargs):
        autoriz (*args, **kwargs)
        print('You need to be autorized, enter the Login')
        i = input()
        log == yarik
        if i == log:
            print ('Welcome', log)
            next
        else:
            print ('Invalid password')
            return
        value = autoriz (*args, **kwargs)
        return value
    return wrapper_decorator 


print ("Menu:")
print("please make a selection. You need to be autorized before using the service")
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
    @decorator    
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
