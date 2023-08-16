def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index where the target is found
    return -1  # Return -1 if the target is not found


my_array = [3, 9, 7, 2, 5, 1, 8, 6, 4]
target_element = 5

# Perform linear search
index = linear_search(my_array, target_element)

if index != -1:
    print(f"Target element {target_element} found at index {index}.")
else:
    print(f"Target element {target_element} not found in the array.")
