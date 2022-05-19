
#Change to binary number
num = 162
x = bin(num)[2:]
print(x)

num = 1043
x = hex(num)[16:]
print(x)

#Convert back to decimal
y = int(x,2)
print(y)