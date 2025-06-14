
base = float(input("Enter the base number: "))


exponent = int(input("Enter the exponent: "))

result = 1

if exponent > 0:
    count = 0
    while count < exponent:
        result = result * base
        count = count + 1

elif exponent < 0:
    count = 0
    while count < abs(exponent):
        result = result * base
        count = count + 1
    result = 1 / result

else:
    print(f"{base}^{exponent} = {result}")
