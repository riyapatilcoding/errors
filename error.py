try:
    num1= int(input("Enter the first number:"))
    num2= int(input("Enter the second number:"))
    result= num1/num2
except ZeroDivisionError:
    print("Divison by zero is error !!")
except ValueError:
    print("Please enter a valid whole numbes")
except:
    print("Wrong input")
else:
    print("No exceptions")
finally:
    print("This will execute no matter what")