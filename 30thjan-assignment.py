# 1.
percentage=int(input("please enter your percentage "))
if percentage>90:
    print("A")
elif 90>=percentage>80:
    print("B")
elif 80>=percentage>=60:
    print("C")
else :
    print("D")



# 2
costprice=int(input("please enter the cost-price of your bike"))
if costprice>100000:
    print("15%")
elif 100000>=costprice>50000:
    print("10%")
elif costprice<=50000:
    print("5%")



#3
city=input("enter the  city from these options :- Delhi,Agra,Jaipur . I will display monuments of that city")
if city.lower()=="delhi":
    print("Red Fort")
elif city.lower()=="agra":
    print("Taj Mahal")
elif city.lower()=="jaipur":
    print("Jal Mahal")
else:
    print("please enter the correct option")




# 4
nums=int(input("kindly enter the number which is divisible by 3 and greater than 10  ")
)
number=nums
count=0
while nums>10:
    count=count+1
    nums=nums/3
print(f"{count} times {number} can be divided by 3 before it is less than or equal to 10. ")




# 5

# while loop is an indefinite itteration that is used when a loop repeats unkown number of times and end when some condition is met

i=0
while i<10:
    print(i)
    i=i+1
# now here the loop will execute indefinite iterations until the condition is met , here we donot know about the number of iteration . but it for loop we know the number of iterations .




# 6
i = 1
while i <= 4 :
    j = 0
    while  j <= 3 :
        print(i*j, end=" ")
        j += 1
    print()
    i += 1
# 2.
n = int(input('Enter number of rows : '))
 
i = 1
while i <= n :
    j = 1
    while j <= i:
        print("*", end = " ")
        j += 1
    print()
    i += 1
# 3.
n = int(input('Enter number of rows : '))
 
i = 1
while i <= n :
    j = n
    while j >= i:
        print("*", end = " ")
        j -= 1
    print()
    i += 1




# 7.or 8.
i=10
while(i>=1):
    print(i)
    i-=1