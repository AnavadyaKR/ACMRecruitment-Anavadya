def to_twos_complement(num, bits=8):
    
    if num < 0:
        num = (1 << bits) + num
    return format(num, f'0{bits}b')


number = -42
binary_rep = to_twos_complement(number)

print(f"Decimal: {number}")
print(f"2's complement: {binary_rep}")
