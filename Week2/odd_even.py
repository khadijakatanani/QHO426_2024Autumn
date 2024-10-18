
number = int(input("Please type a number: "))

if number % 2 == 0:
    #print("The number", number, "is even!")
    print(f"The number {number} is even!")
else:
    print(f"The number {number} is odd!")


print("Please enter the first number: ")
first_number = int(input())

print("Please enter the second number: ")
second_number = int(input())

if first_number > second_number:
    print(f"The first number is the greatest: {first_number}")
elif first_number < second_number:
    print(f"The first number is the smallest: {first_number}")
else:
    print(f"The two numbers are equal, first number: {first_number}, "
          f"second number: {second_number}")
