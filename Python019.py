# ---------------
# ----Numbers----
# ---------------

# int
print(type(10))

# float
print(type(10.5))

# complex
ccomplex = 5+6j
print(type(ccomplex))

print("Real is {}".format(ccomplex.real)) # Just the real part
print("Image is {}".format(ccomplex.imag)) # Just the real part


# CONVERT
# [1] int > float or complex
# [2] float > int or complex
# [3] complex cannot be converted

print(float(100))
print(complex(100))

print(int(10.5))
print(complex(10.50))

# print(int(10+8j)) Error