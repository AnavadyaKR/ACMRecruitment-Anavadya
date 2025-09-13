# This program implements the Bubble Sort algorithm
# and tests it on the list [5, 2, 9, 1, 5, 6].

def bubble_sort(arr):
    n = len(arr)
    # Outer loop: goes through the list multiple times
    for i in range(n - 1):
        # Inner loop: compares each adjacent pair
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap the elements if they are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    # Return the sorted list
    return arr

# Main part of the program
if __name__ == "__main__":
    test_list = [5, 2, 9, 1, 5, 6]  # The list to be sorted
    print("Original List:", test_list)
    sorted_list = bubble_sort(test_list)  # Call bubble sort
    print("Sorted List:", sorted_list)    # Print the result
