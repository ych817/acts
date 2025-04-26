class natural_number:
    def __init__(self, n):
        if (isinstance(n, int)) and (n >= 0):
            self.n = n
        else:
            raise ValueError("Input must be a non-negative integer")

    def factorial(self):
        if self.n == 0 or self.n == 1:
            return 1
        else:
            result = 1
            for i in range(2, self.n + 1):
                result *= i
            return result
        
    def __str__(self):
        return f"Factorial of {self.n} is {self.factorial()}"
    

n5 = natural_number(5)
print(f"Factorial of {n5.n} is {n5.factorial()}")