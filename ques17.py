class  Calculator:
    def __init__(self, num1, num2, operator):
        try:
            num1 = int(num1)
            num2 = int(num2)
            self.number1 = num1
            self.number2 = num2 
        except ValueError:
            raise ValueError('Enter the integers only. ')
        self.operator = operator
    def calculate(self):
        operators = {
            '+' : self.add(),
            '-' : self.substract(),
            '*' : self.multiply(),
            '/' : self.divide()
            }
        return operators.get(self.operator)
    def add(self):
        return self.number1 + self.number2
        
    def substract(self):
        return self.number1 - self.number2

    def multiply(self):
        return self.number1 * self.number2

    def divide(self):
        try:
            result = self.number1 / self.number2
        except ZeroDivisionError:
            result = 0
        return result
   
first_number = input('Enter the first number: ')
second_number = input('Enter the second number: ')
operator = input('Enter the operator: ')
obj1 = Calculator(first_number,second_number, operator)
print(obj1.calculate())


        
    
    
