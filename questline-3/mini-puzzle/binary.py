# rotate_binary.py

def rotate_binary(binary_str: str, k: int) -> int:
    """
    Rotates a binary string k steps to the left
    and converts the result to its decimal value.

    Args:
        binary_str (str): A string containing only '0' and '1'
        k (int): Number of positions to rotate left

    Returns:
        int: Decimal value of the rotated binary string
    """

    # Normalize k in case it’s larger than the length
    k = k % len(binary_str)

    # Perform rotation
    rotated = binary_str[k:] + binary_str[:k]

    # Convert to decimal
    return int(rotated, 2)


# ---------- Usage Examples ----------
if __name__ == "__main__":
    # Example 1
    b1 = "1011"
    k1 = 2
    print(f"Rotate {b1} by {k1} → {rotate_binary(b1, k1)}")
    # 1011 rotated left 2 → "1110" → decimal 14

    # Example 2
    b2 = "1100"
    k2 = 1
    print(f"Rotate {b2} by {k2} → {rotate_binary(b2, k2)}")
    # 1100 rotated left 1 → "1001" → decimal 9

    # Example 3
    b3 = "1001"
    k3 = 3
    print(f"Rotate {b3} by {k3} → {rotate_binary(b3, k3)}")
    # 1001 rotated left 3 → "1100" → decimal 12
