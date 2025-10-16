numeru1 = float(input("Hatama numeru1: "))
operasaun = input("hili operasaun (+, -, *, /): ")
numeru2 = float(input("Hatama numeru2: "))

if operasaun == "+":
    result = numeru1 + numeru2
elif operasaun == "-":
    result = numeru1 - numeru2
elif operasaun == "*":
    result = numeru1 * numeru2    
else:
    if numeru2 != 0:
        result = numeru1 / numeru2
    else: 
        print("errorrrrrrr😒")

print(numeru1, " ", operasaun, " ", numeru2, " = ", result)
