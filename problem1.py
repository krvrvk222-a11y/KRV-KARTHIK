# Problem-1: 
# Create a small calculator which performs operations such as Addition, Subtraction, Multiplication and Division using class.
# Calculator inputs :> ‘a’, ‘b’ and ‘type of operation’
#Datatype :> ‘a’ = double, ‘b’ = double, ‘type of operation’ = string

class Calculator:
    def __init__(self,a,b,operation):
        self.a = float(a)
        self.b = float(b)
        self.operation = operation.lower()
    def calculate(self):
        if self.operation == "add":
            return self.a + self.b
        elif self.operation == "subtract":
            return self.a - self.b
        elif self.operation == "multiply":
            return self.a * self.b
        elif self.operation == "divide":
            if self.b == 0:
                return "Cannot divide by zero"
            return self.a / self.b
        else:
            return "Invalid operation"

calcadditon = Calculator(20,10,"add")
print(calcadditon.calculate())

calcsubtraction = Calculator(20,10,"subtract")
print(calcsubtraction.calculate())

calcmulti = Calculator(20,10,"multiply")
print(calcmulti.calculate())

calcdivison = Calculator(20,10,"divide")
print(calcdivison.calculate())

