#Luna Alsalman 588512
#Python List Exercises

### 1. Creating a List
## Exercise: Create a list of 5 of your favorite fruits. Print the list.
fruit = ['Watermelon', 'Orange', 'Mango', 'Avocado', 'passionfruit']  #define list of fruits

print(fruit)  #print the list of fruits

### 2. Accessing Elements
## Exercise: Given the list `colors = ['red', 'blue', 'green', 'yellow', 'purple']`, print the first, third, and last color in the list.
colors = ['red', 'blue', 'green', 'yellow', 'purple']  #create the list of colors
print(colors[0])  #print the first color
print(colors[2])  #print the third color
print(colors[-1])  #print the last color

### 3. Modifying a List
##Exercise: Create a list `numbers` with values `[10, 20, 30, 40, 50]`. Change the second item to `25` and add `60` to the end of the list. Print the modified list.
numbers = [10, 20, 30, 40, 50]  #initialize a list of numbers
numbers[1] = 25  #change the second item to 25
numbers.append(60)  #add 60 to the end of the list

print(numbers)  #print the modified list

### 4. List Slicing
##Exercise: Using the list `names = ['Alice', 'Bob', 'Charlie', 'David', 'Emma']`, create a new list `subset` containing only the first three names. Print `subset`.
names = ['Alice', 'Bob', 'Charlie', 'David', 'Emma']  #create a list of names
subset = names[:3]  #slice the list to get the first three names

print(subset)  #print the subset of names

### 5. Looping through a List
##Exercise: Create a list of numbers from `1` to `10` and use a loop to print each number squared.
numbers = list(range(1, 11))  #create a list of numbers from 1 to 10
squared_numbers = [number ** 2 for number in numbers]  #create a list of squared numbers

for squared in squared_numbers:  #loop through the squared numbers
    print(squared)  #print each squared number

### 6. List Methods: Append and Extend
##Exercise: Create an empty list called `shopping_cart`. Add the items `'milk'`, `'bread'`, and `'eggs'` to it using the `.append()` method. Then use `.extend()` to add `['butter', 'cheese']` to the list. Print the final list.
shopping_cart = []  #initialize an empty shopping cart

shopping_cart.append('milk')  #add 'milk' to the cart
shopping_cart.append('bread')  #add 'bread' to the cart
shopping_cart.append('eggs')  #add 'eggs' to the cart

shopping_cart.extend(['butter', 'cheese'])  #add multiple items to the cart

print(shopping_cart)  #print the final shopping cart

### 7. Finding Maximum and Minimum in a List
##Exercise: Write a program to find the maximum and minimum values in the list `numbers = [45, 22, 88, 56, 92, 33]`.
num = [45, 22, 88, 56, 92, 33]  #initialize a list of numbers
max_value = max(num)  #find the maximum value in the list
min_value = min(num)  #find the minimum value in the list

print(f"max: {max_value}")  #print the maximum value
print(f"min: {min_value}")  #print the minimum value

### 8. Counting Occurrences
##Exercise: Given the list `letters = ['a', 'b', 'a', 'c', 'b', 'a', 'd']`, count how many times the letter `'a'` appears in the list.
letters = ['a', 'b', 'a', 'c', 'b', 'a', 'd']  #create a list of letters

letter_counter = letters.count('a')  #count occurrences of 'a'
print(f"A is repeated {letter_counter} times")  #print the count of 'a'

### 9. List Comprehension
##Exercise: Use list comprehension to create a new list containing the squares of all even numbers from `0` to `10`. Print the resulting list.
squared = []  #initialize an empty list for squares
for x in range(11):  #loop through numbers from 0 to 10
    if x % 2 == 0:  #check if the number is even
        squared.append(x ** 2)  #append the square of the even number to the list
print(squared)  #print the list of squared even numbers

### 10. Removing Duplicates
##Exercise: Given the list `nums = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]`, write a program to remove duplicates and print the unique elements only.
nums = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]  #initialize a list with duplicates
unique = []  #create an empty list for unique elements

for num in nums:  #loop through the original list
    if num not in unique:  #check if the number is not already in the unique list
        unique.append(num)  #add the unique number to the list

print(unique)  #print the list of unique elements
