def find_N(a, b):
    
    return b ^ a

if __name__ == "__main__":
    a = 23
    b = 45
    N = find_N(a, b)
    print(f"a = {a} (decimal), b = {b} (decimal)")
    print(f"Computed N = b XOR a = {b} ^ {a} = {N}")
    
