'''
Simple Calculator using Python.
Beginner Projects in Python.
Example -2 (With Python Functions)
--RecentBlogger--
'''


#Displays available Math operations to perform
print("Choose the Math Operation: \n + Addition\n - Subtraction\n * Multiplication\n / Division")
#Python Functions to specific Math Operations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

#Into a continuous loop 
while True:
    choice = input("Enter your choice (+ - * /): ")
    if choice in ('+','-','*','/'):
        number_1 = float(input("Enter the first number: "))
        number_2 = float(input("Enter the Second number: "))
        if choice == '+':
            print(f"Output:\n {number_1} + {number_2} =", add(number_1, number_2))
        elif choice == '-':
            print(f"Output:\n {number_1} - {number_2} =", subtract(number_1, number_2))
        elif choice == '*':
            print(f"Output:\n {number_1} * {number_2} =", multiply(number_1, number_2))
        elif choice == '/':
            print(f"Output:\n {number_1} / {number_2} =", divide(number_1, number_2)) 
        proceed = input("Do you wanna continue? ( y/n ): ")
        if proceed == 'n':
            break
    else:
        print("Invalid Input!")