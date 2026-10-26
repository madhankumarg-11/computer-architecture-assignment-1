def ror(n, k):
    return ((n >> k) | (n << (8 - k))) & 255

def rcr(n, carry, k):
    value = (carry << 8) | n
    value = ((value >> k) | (value << (9 - k))) & 511
    return value & 255, (value >> 8) & 1

n = int('11010101', 2)

print("a) Rotate Right Without Carry (ROR)")
print("Original:", format(n, '08b'))

temp = n
for i in range(3):
    temp = ror(temp, 1)
    print("Step", i + 1, ":", format(temp, '08b'))

print("Final Result:", format(temp, '08b'))

print("\nb) Rotate Right With Carry (RCR)")
carry = 0
temp = n
print("Original:", format(temp, '08b'))
print("Initial Carry:", carry)

for i in range(3):
    new_carry = temp & 1
    temp = (temp >> 1) | (carry << 7)
    carry = new_carry
    print("Step", i + 1, ":", format(temp, '08b'),
          "Carry:", carry)

print("Final Result:", format(temp, '08b'))
print("Final Carry:", carry)