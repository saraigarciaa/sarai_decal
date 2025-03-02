#1 Oski Stole My Power 
x = 2
y = 3
def power (x, y):
    result = 1
    for _ in range(y):
        result *= x
    return result
print(power(x,y))

# 2: What Should I Wear?
readings = [15, 14, 17, 20, 23, 28, 20]
def temperatureRange(readings):
    return (min(readings)), max(readings)
print(temperatureRange(readings))

#3 Check If its the Weekend
def isWeekend(days):
    days = {"1": "Monday", "2": "Tuesday" , "3" : "Wednesday" , "4": "Thursday", "5":"Friday", "6":"Saturday", "7":"Sunday"}
    return day in [6,7]

day = 6
print(isWeekend(day))

day = 3
print(isWeekend(day))

#4 Fuel Efficiency Calculator:

def fuel_efficiency(distance, fuel):
    return round(distance / fuel, 2)

distance = 70
fuel = 21.5
print(fuel_efficiency(distance, fuel))

#5 Secret Code:


def decodeNumbers(n):
    last_digit = n % 10
    remaining_number = n // 10
    multipler = 1 
    temp = remaining_number
    while temp > 0:
        temp //= 10
        multipler *= 10
    return last_digit * multipler + remaining_number

n = 12345
print(decodeNumbers(n))

# 6 Min and Max but with Loops:
#   6.1 For Loops:

def find_min_with_for_loop(nums):
    min_value = nums[0]
    for num in nums:
        if num < min_value:
            min_value = num
    return min_value

nums = [2024, 98, 131, 2, 3, 72]
print(find_min_with_for_loop(nums))

def find_max_with_for_loop(nums):
    max_value = nums[0]
    for num in nums:
        if num > max_value:
            max_value = num
    return max_value

print(find_max_with_for_loop(nums))

#   6.2 While Loops:

def find_min_with_while_loop(nums):
    min_value = nums[0]
    index = 1 
    while index < len(nums):
        if nums[index] < min_value:
            min_value = nums[index]
        index += 1
    return min_value

print(find_min_with_while_loop(nums))

def find_max_with_while_loop(nums):
    max_value = nums[0]  # Assume the first number is the maximum
    index = 1  # Start checking from the second element
    while index < len(nums):
        if nums[index] > max_value:  # If a larger number is found, update max_value
            max_value = nums[index]
        index += 1  # Move to the next element
    return max_value

print(find_max_with_while_loop(nums))

# 7 Counting Vowels

def vowel_and_consonant_count(text):
    vowels = "aeiouAEIOU"
    vowels_count = 0
    consonants_count = 0

    for char in text:
        if char.isalpha():
            if char in vowels:
                vowels_count += 1
            else: 
                consonants_count += 1
    return (vowels_count, consonants_count)

text = "UC Berkeley, founded in 1868!"
print(vowel_and_consonant_count(text))
   

# 8 Calculate Digital Root
def digital_root(num):
    total = 0
    while num > 0:
        total += num % 10  
        num //= 10  
    return total

num = 2468
print(digital_root(num)) 
