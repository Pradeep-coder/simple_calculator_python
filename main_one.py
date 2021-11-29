
'''
Simple Calculator using Python.
Beginner Projects in Python.
Example -1 (Without Python Functions)
--RecentBlogger--
'''
#Displays available Math operations to perform
print("Choose the Math Operation: \n + Addition\n - Subtraction\n * Multiplication\n / Division")

#get the user input to perform Math Operation
choice = input("Enter your choice (+ - * /): ")

#check whether the input entered by user is valid! if not else part
if choice in ('+','-','*','/'):
    number_1 = float(input("Enter the first number: "))
    number_2 = float(input("Enter the Second number: "))
    if choice == '+':
        output = number_1 + number_2
        print(f"Output:\n {number_1} + {number_2} = {output}")
    elif choice == '-':
        output = number_1 - number_2
        print(f"Output:\n {number_1} - {number_2} = {output}")
    elif choice == '*':
        output = number_1 * number_2
        print(f"Output:\n {number_1} * {number_2} = {output}")
    elif choice == '/':
        output = number_1 / number_2
        print(f"Output:\n {number_1} / {number_2} = {output}")
else:
    print("Invalid Input")

