try:
    number=int(input("Enter a number: "))
    result=10/number
    print(f"result:{result}")
except ValueError:
    print("please enter a valid number")    
except ZeroDivisionError:
    print("cannot divide by zero")
finally:
    print("operation completed")    