a = float(input('Please, enter your weight in kilograms?'))
b = float(input('Please, enter your height in meters?'))
c = a/(b*b)

if c < 20:
        print('Your BMI is',c,'which means you are underweight!!!')
elif c >=20 and c <=23:
    print ('Your BMI is','20=|=========50')
elif c >=23 and c <=26:
    print ('Your BMI is','20==|========50')
elif c>=26 and c <=29:
    print ('Your BMI is','20===|=======50')
elif c>=29 and c <=32:
    print ('Your BMI is','20====|======50')
elif c>=32 and c <=35:
    print ('Your BMI is','20=====|=====50')
elif c>=35 and c <=38:
    print ('Your BMI is','20======|====50')
elif c>=38 and c <=41:
    print ('Your BMI is','20=======|===50')
elif c>=41 and c <=44:
    print ('Your BMI is','20========|==50')
elif c>=44 and c <=47:
    print ('Your BMI is','20=========|=50')
elif c>=47 and c <=50:
    print ('Your BMI is','20==========|50')
elif c > 30:
        print('Your BMI is',c,'which means you are obese!!!')
        
