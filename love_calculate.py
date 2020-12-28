import random

print("Welcome Buddy..! Calculate your love percentage \n First Output is true one")

while True:

    prince=input ("What is the name of prince :")

    princess=input("What is the name of princess:")

    boy=(len(prince))

    girl=(len(princess))

    rnd=random.randint(1,20)

    percentage=100-(boy*girl)-rnd

    if percentage>=40 and percentage <=50:

        print("---------please stop and don't love with this person", str(percentage)+" "+"%")

    elif percentage >= 50 and percentage <=60:

        print('----One side Love---', str(percentage)+" "+"%")

    elif percentage >=60 and percentage <=70:

        print('-----Love is there but marriage not possible---', str(percentage)+" "+"%")
    
    else:

        print('-------Made for each other---please be married...!', str(percentage)+" "+"%")


