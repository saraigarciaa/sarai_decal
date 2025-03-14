# HW 5: Review
#1 HW1/HW2 Review: The Terminal + Command Line + Git
#1) The command that will tell me what my working directory is is pwd.

#2) The command that will list all the files in my current working directory is ls.

#3) The command that will let me move to the correct repository is cd ..  enter then cd brianna_repo. To see the latest changes, you would put [git pull main origin].

#4) To move homework.py to my personal repository homework directory 
#       cd brianna_repo 
#       mv homework.py ../judy_decal/homework/

#5) cd ~/python_decal/judy_decal/homework/
#   cat homework.py

#6) cd ~/python_decal/judy_decal/homework/
#   nano homework.py

#7) cd ~/python_decal/judy_decal/homework/
#   cat homework.py
#   [ctrl + x]
#   [y]
#   git status
#   git add homework.py
#   git commit -m "Homework completed"
#   git push origin main
#   git status 

#8) Judy didn'y do git add [file name.py], she tried to git push before pulling in the staging area.
# the correct code is:
#       git pull origin main [to view the changes made first from remote repository]
    #   git push origin main

#9) You could use cd ~/Recent/


#  2 - HW3 Review: Data Types + Functions + Conditionals + Loops
#2.1 - Data Types
print(type(0.1))
print(type(True))

#  2.2 - Conditionals
def evenOrodd(n):
    return "even" if n % 2 == 0 else "odd"

print(evenOrodd(7))
print(evenOrodd(10))

# 3  -  Loops
def sumWithLoop(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

numbers = [1, 2, 3, 4, 5]
print(sumWithLoop(numbers))

# 4  - HW4 Review: Lists

# 4.1 - Lists
def duplicateList(lst):
    result = []
    for item in lst:
        result.append(item)
        result.append(item)
    return result

alpha_list = ['a', 'b', 'c']
print(duplicateList(alpha_list))

# 4.2 - Debugging
def square(num):
    return num **2


