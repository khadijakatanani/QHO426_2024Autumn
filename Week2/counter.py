print("Please enter the first number: ")
first_number = int(input())

print("Please enter the second number: ")
second_number = int(input())

print("Please enter the third number: ")
third_number = int(input())

even_counter = 0
odd_counter = 0

# first number
if first_number % 2 == 0:
    # even_counter = even_counter + 1
    even_counter += 1
else:
    odd_counter += 1

# second number
if second_number % 2 == 0:
    # even_counter = even_counter + 1
    even_counter += 1
else:
    odd_counter += 1

# third number
if third_number % 2 == 0:
    # even_counter = even_counter + 1
    even_counter += 1
else:
    odd_counter += 1

print(f"There is/are {even_counter} even number(s) and {odd_counter} odd number(s)!")