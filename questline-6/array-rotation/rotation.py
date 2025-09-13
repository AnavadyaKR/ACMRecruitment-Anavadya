def reverse(nums, start, end):
  
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1


def rotate(nums, k):
    n = len(nums)
    k = k % n  # Normalize k in case it's larger than n

    # Step 1: Reverse the entire array
    reverse(nums, 0, n - 1)

    # Step 2: Reverse first k elements
    reverse(nums, 0, k - 1)

    # Step 3: Reverse remaining elements
    reverse(nums, k, n - 1)


# Main program for testing
if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    print("Original Array:", nums)
    rotate(nums, k)
    print(f"Array after rotating by {k} steps:", nums)
