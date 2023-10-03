def search_insert_position(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left

# Використання:
sorted_list = [1, 3, 5, 6]
new_element = 2
position = search_insert_position(sorted_list, new_element)
print(f"Позиція для вставки {new_element} у відсортований список: {position}")