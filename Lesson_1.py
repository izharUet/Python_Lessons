#abs(x)...
#Return the absolute value of a number. The argument may be an integer,
# a floating-point number, or an object implementing __abs__().
# If the argument is a complex number, its magnitude is returned.
# Exercise with python 3.9

# abs() with integer and floating numbers gives the positive value of the operations.

print(abs(12))  # output = 12
print(abs(-12)) # output = 12

# abs() with Complex number, complex(3, 2).
# gives the floating number of the magnitude
# Exercise

z = complex(3,2)
print(z.real) # print the real magnitude of complex number
print(z.imag) # print the imag magnitue of complex
print(abs(z)) # output = floating number

# abs() for