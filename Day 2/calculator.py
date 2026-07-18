print ("Calculator")
num1 = float(input("Enter first Number:"))
num2 = float(input("Enter second Number:"))
print("Select operation -\n" \
      "1. Add\n" \
      "2. Subtract\n" \
      "3. Multiply\n" \
      "4. Divide")
choice = input("Enter choice (1/2/3/4): ")
if choice in ('1', '2', '3', '4'):
    if choice == '1':
        print(num1, "+", num2, "=", num1 + num2)

    elif choice == '2':
        print(num1, "-", num2, "=", num1 - num2)

    elif choice == '3':
        print(num1, "*", num2, "=", num1 * num2)

    elif choice == '4':
        if num2 != 0:
            print(num1, "/", num2, "=", num1 / num2)
        else:
            print("Error: Division by zero is not allowed.")
    
else:
    print("Invalid Input")

