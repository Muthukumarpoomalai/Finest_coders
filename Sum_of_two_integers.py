a = int(input("Enter the number for a : "))
b = int(input("Enter the number for b : "))

while b != 0:
    carry = (a & b) << 1   
    a = a ^ b              
    b = carry              

print(a)
