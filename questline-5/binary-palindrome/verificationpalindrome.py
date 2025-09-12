def is_binary_palindrome(n):
    binary_str = bin(n)[2:]  
    return binary_str == binary_str[::-1]

# Test 
numbers = [5, 10]

for num in numbers:
    binary_str = bin(num)[2:]
    result = "Palindrome" if is_binary_palindrome(num) else "Not a palindrome"
    print(f"Decimal: {num}, Binary: {binary_str}, Result: {result}")
