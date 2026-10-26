def binary(n):
    return format(n & 255, '08b')

def decimal(b):
    n = int(b, 2)
    return n - 256 if n >= 128 else n

def calculate(a, b, op):
    result = a + b if op == '+' else a - b
    binary_result = binary(result)
    overflow = result < -128 or result > 127

    print("First operand :", binary(a))
    print("Second operand:", binary(b))
    print("Result binary :", binary_result)
    print("Result decimal:", decimal(binary_result))
    print("Overflow      :", "Yes" if overflow else "No")
    print()

print("a) +46 + (+29)")
calculate(46, 29, '+')

print("b) (-48) - (-23)")
calculate(-48, -23, '-')