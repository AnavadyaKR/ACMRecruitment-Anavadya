# without using built-in reverse functions.

# Iterative method
def reverse_iterative(s):
    reversed_str = ""
    for i in range(len(s) - 1, -1, -1):  # Start from last index to 0
        reversed_str += s[i]
    return reversed_str


# Recursive method
def reverse_recursive(s):
    # Base case: if string is empty or single character
    if len(s) <= 1:
        return s
    # Recursive case:
    return reverse_recursive(s[1:]) + s[0]


# Main program
if __name__ == "__main__":
    test_str = "hello"
    print("Original String:", test_str)

    print("Iterative Reversal:", reverse_iterative(test_str))
    print("Recursive Reversal:", reverse_recursive(test_str))
