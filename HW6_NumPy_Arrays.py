# HW 6 - NumPy Arrays



# 1 - Prime Clusters 
import numpy as np

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            return False
    return True

def containsPrimes(arr):
    mask = np.apply_along_axis(lambda row: any(is_prime(x) for x in row), axis = 1, arr = arr)
    return arr[mask]

arr = np.array([[2, 3, 5],  
                [4, 6, 8],  
                [11, 13, 17],  
                [7, 10, 13]])  

print(containsPrimes(arr))






# 2 - Let's Play Checkers

# 2.1:
a = (8 , 8)
checkerboard = np.zeros((a), dtype = int)
print(checkerboard)



# 2.2

def checkerboard():
    board = np.zeros((8,8), dtype= int)
    board [::2, ::2] = 1
    return board

print(checkerboard())



# 2.3

def checkherboard():
    board = np.zeros((8,8), dtype= int)
    board [::2, ::2] = 1
    board [1::2, 1::2] = 1
    return board

print(checkerboard())



# 2.4
def reverse_checkerboard():
    board = np.ones((8,8), dtype= int)
    board [::2, ::2] = 0
    board [1::2, 1::2] = 0
    return board

print(reverse_checkerboard())

# 3 -- THE EXPANDING UNIVERSE

universe = np.array(['galaxy', 'clusters'])
def expansion(arr, spaces):
    def expand_word(word):
        return (' ' * spaces).join(word)

    expanded_array = np.array([expand_word(word) for word in arr])
    return expanded_array


print(expansion(universe, 1)) 
print(expansion(universe, 2))



# 4 -- Second-Dimmest Star

def secondDimmest(stars):
    sorted_stars = np.sort(stars, axis = 0)
    return sorted_stars[1]

arr = np.random.seed(123)
stars = np.random.randint(500, 2000, (5, 5))

print('array of stars') # organizational purposes
print(stars)

print('second dimmest list') # organizational purposes
print(secondDimmest(stars))
