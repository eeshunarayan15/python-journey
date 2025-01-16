# print("Hello, world!")
# print('c:\ndocs\nnavin')
# c:
# docs
# # navin
# print(r'c:\ndocs\nnavin')
# c:\ndocs\nnavin

# =====================
# x=2
# y=3
# x=9
# print(x)
# print(x+y)
# name='rahul'
# print(name[0:2])
# ===========
# length function in python

# name='rahul'
# length=len(name)
# print(len(name))
# print(length)
# ======================

# list in python
# nums=[1,2,3,4,5,6,7,8,9,0,"nums"]
# num2=[nums,1]
# print(nums)
# print(nums[0:4])
# print(num2)


# # list are mutable and it has varous method
nums=[1,2,3,4,5,6,7,8,9,0,"nums"]
# 1. append()
# Adds an element to the end of the list.
# nums.append("rahul")
# print(nums)

# ==============================
# insert()
# Inserts an element at a specified position.
# nums.insert(2,'inserted')
# print(nums)


# =============================================



# 3. remove()
# Removes the first occurrence of a specified value.
# print(nums)
# nums.remove(1)
# print(nums)
# ==============================================
# 4. pop()
# Removes and returns the element at the specified position (default is the last element).
# print(nums)
# poppedElement=nums.pop()
# print(poppedElement)
# print(nums)
# poppedElement1=nums.pop(0)
# print(poppedElement1)

# The pop method is a built-in method for lists in Python. It removes and
#  returns the element at the specified index. If no index is specified,
# it removes and returns the last element of the list.
# If no index is specified, it removes and returns the last element.the default value is (-1)


# ==================================
# 5. index()
# Returns the index of the first occurrence of a specified value.
# print(nums.index(5))
# ====================================================
# 6. count()
# Returns the number of occurrences of a specified value.
# count_of_2 = nums.count(2)
# print(count_of_2)  # Output: 1
# 7. sort()
# Sorts the list in ascending order.
#  (Note: This will raise an error if the list contains
#  non-comparable types like strings and integers together.)
# nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# nums.sort()
# print(nums)  # Output: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]



# =========================================================
# 8. reverse()
# Reverses the elements of the list in place.
# nums.reverse()
# print(nums)  # Output: [0, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# =================================================================
# 9. extend()
# Extends the list by appending elements from another list.
# nums.extend([10, 11])
# print(nums)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, "nums", 10, 11]




# ==========================================================
# 10. clear()
# Removes all elements from the list.
# nums.clear()
# print(nums)  # Output: []




# =============================================================
# The del statement in Python is used to delete objects. 
# It can be used to delete variables, list elements, or entire lists.
#  When you use del, you are instructing Python to remove the specified object from memory.

# In the context of lists, del can be used to remove elements at specific positions. 
# Here's a breakdown of how it works:

# Deleting a single element by index:
# nums = [1, 2, 3, 4, 5]
# del nums[2]  # Deletes the element at index 2 (which is 3)
# print(nums)  # Output: [1, 2, 4, 5]


# =========================================
# Deleting a slice of elements:
# nums = [1, 2, 3, 4, 5]
# del nums[1:3]  # Deletes elements from index 1 to 2 (which are 2 and 3)
# print(nums)  # Output: [1, 4, 5]
# ==================================================
# Deleting the entire list:
# nums = [1, 2, 3, 4, 5]
# print(nums)
# del nums  # Deletes the entire list
# print(nums)  # This would raise a NameError because nums no longer exists  
nums=[1,2,3,4,5,6,7,8,9,0]
print(nums)
print(max(nums))
print(min(nums))