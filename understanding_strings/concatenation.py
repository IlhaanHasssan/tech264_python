x = 2

y = 5.4

z = " there's now a number 25.4 unless we put a space in!"

#print(x + y + z) does not work
#the problem is that a string cannot be added to a float/int as the data type is not supported in mathematical operations

print(str(x) + str(y) + z)
#to fix this, the int & float data types have been converted into string