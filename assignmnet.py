# a=int(input("enter the number"))
# if a % 2==0:
#     print("even")
# else:
#     print("odd")
number = int(input("Enter a number:"))

if number % 5 == 0:
   print("The number is divisible by 5")
else:
    print("The number is not divisible by 5")


raffic=input("signal")

if raffic=="red":
    print("stop")
elif raffic=="yellow":
        print("wait")
else:
      print("go")