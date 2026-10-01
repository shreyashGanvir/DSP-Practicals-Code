# Program 1: Array Creation
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print("Array:", arr)

# Program 2: Special Initialization
import numpy as np

print("Zeros:\n", np.zeros((2, 2)))
print("Ones:\n", np.ones((3, 3)))
print("Full:\n", np.full((2, 2), 7))
print("Random:\n", np.random.rand(2, 2))

# Program 3: Indexing, Slicing, Reshaping
import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

# Indexing
print("Element:", arr[1][2])

# Slicing
print("Slice:\n", arr[0:2, 1:3])

# Reshaping
new_arr = arr.reshape(1, 9)
print("Reshaped:", new_arr)

# Program 4: Array Operations
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Addition:", a + b)
print("Multiplication:", a * b)
print("Mean:", np.mean(a))
print("Sum:", np.sum(b))
