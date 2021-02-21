user=int(input("Enter the Number-"))
if user%7==0 and user%11==0:
    print("It is divisible by both 11 and 7")
elif user%7!=0 or user%11==0:
    print("It is not divisible by 7 but it is divisible by 11")
elif user%7==0 or user%11!=0:
    print("It is divisible by 7 but it is not divisible by 11")
else:
    print("It is neither divisible by 7 nor 11")