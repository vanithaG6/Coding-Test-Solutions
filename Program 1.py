class Calculate:
     
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

   
    def multiply(self, a, b):
        return a * b

  
    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero!"
        return a / b
    

a=float(input("Enter the  first number "))
b=float(input("Enter the secind number "))
operation=input("Enter operation (add, sub, mul, div):")
operation.lower
cal=Calculate()
if operation == "add":
    result = cal.add(a, b)
elif operation == "sub":
    result = cal.subtract(a, b)
elif operation == "mul":
    result = cal.multiply(a, b)
elif operation == "div":
    result = cal.divide(a, b)
else:
    result = "Invalid operation!"
    
print("Result:", result)

