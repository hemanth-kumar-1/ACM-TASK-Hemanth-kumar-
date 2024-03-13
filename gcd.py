
# calculates the gcd of given numbers
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
maxi = max(num1,num2)
mini = min(num1,num2)
div = 1
while div != 0:
    div = maxi % mini
    maxi = mini
    mini = div
    if div == 0:
        print(f"The gcd of {num1} and {num2} is: {maxi}")
