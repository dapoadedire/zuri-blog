print("")   
print("Welcome to the calculator!")
print("")
print("Please enter your first number:")
first_number = input()
print("")
print("Please enter your second number:")
second_number = input()
print("")
print("Please enter your operator:")
operator = input()
print("")
print("Your result is:")
if operator == "+":
    print(int(first_number) + int(second_number))
elif operator == "-":
    print(int(first_number) - int(second_number))
elif operator == "*":
    print(int(first_number) * int(second_number))
elif operator == "/":
    print(int(first_number) / int(second_number))
else:
    print("Invalid operator")
    print("")
    print("Please try again.")



