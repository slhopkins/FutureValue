print('this program calculates the future value')
print("of a ten year investment.")

principal = eval (input("Enter the initial principal: "))
apr = eval(input("Enter the annual interest rate: "))
for i in range (10):
    principal = principal *(1+apr)

    print("The value in 10 years is: ", principal)