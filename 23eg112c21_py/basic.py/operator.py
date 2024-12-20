# Arithmetic Operators
a = 15
b = 4

print("Arithmetic Operators:")
print(f"a + b = {a + b}")     # Addition
print(f"a - b = {a - b}")     # Subtraction
print(f"a * b = {a * b}")     # Multiplication
print(f"a / b = {a / b}")     # Division
print(f"a % b = {a % b}")     # Modulus
print(f"a ** b = {a ** b}")   # Exponent
print(f"a // b = {a // b}")   # Floor Division

# Comparison Operators
print("\nComparison Operators:")
print(f"a == b: {a == b}")    # Equal
print(f"a != b: {a != b}")    # Not equal
print(f"a > b: {a > b}")      # Greater than
print(f"a < b: {a < b}")      # Less than
print(f"a >= b: {a >= b}")    # Greater than or equal to
print(f"a <= b: {a <= b}")    # Less than or equal to

# Assignment Operators
c = 10
print("\nAssignment Operators:")
print(f"c = : {c}")
c += 5
print(f"c += 5: {c}")
c -= 3
print(f"c -= 3: {c}")
c *= 2
print(f"c *= 2: {c}")
c /= 4
print(f"c /= 4: {c}")
c %= 3
print(f"c %= 3: {c}")
c **= 2
print(f"c **= 2: {c}")
c //= 3
print(f"c //= 3: {c}")

# Logical Operators
x = True
y = False

print("\nLogical Operators:")
print(f"X is {x} and Y is {y}")
print(f"x and y: {x and y}")
print(f"x or y: {x or y}")
print(f"not x: {not x}")

# Bitwise Operators
m = 10  # 1010 in binary
n = 4   # 0100 in binary
print("\nBitwise Operators:")
print(f"binary of {m}: {bin(m)} and {n}: {bin(n)}")
print(f"m & n: {m & n}")   # AND
print(f"m | n: {m | n}")   # OR
print(f"m ^ n: {m ^ n}")   # XOR
print(f"~m: {~m}")         # NOT
print(f"m << 1: {m << 1}") # Left Shift
print(f"m >> 1: {m >> 1}") # Right Shift

# Identity Operators
print("\nIdentity Operators:")
print(f"a is b: {a is b}")
print(f"a is not b: {a is not b}")

# Membership Operators
string = "Hello World"
print("\nMembership Operators:")
print(f"'H' in string {string}: {'H' in string}")
print(f"'z' not in string {string}: {'z' not in string}")
