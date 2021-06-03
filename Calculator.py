first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))

arithmetic_operation = input("Enter one of the basic arithmetic operations. "
                             "Select + for addition, - for subtraction, "
                             "* for multiplication or / for division: ")

if arithmetic_operation == "+":
    print("Sum of the selected numbers is: " + str(first_num + second_num))
elif arithmetic_operation == "-":
    print("Result of the subtraction is: " + str(first_num - second_num))
elif arithmetic_operation == "*":
    print("Result of the multiplication is: " + str(first_num * second_num))
elif arithmetic_operation == "/":
    print("Result of the division is: " + str(first_num / second_num))
else:
    print("Wrong operator inserted")
