class Factorial:
    def __init__(self, number):
        self.number = number
    
    def compute(self):
        fact = 1
        for i in range(1, self.number+1):
            fact *= i
        return fact


num = int(input("Enter number: "))
fact = Factorial(num)
print(fact.compute())