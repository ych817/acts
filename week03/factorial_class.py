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
        
    def is_prime(self):
        if self.n < 2:
            return False
        for i in range(2, int(self.n**0.5) + 1):
            if self.n % i == 0:
                return False
        return True
    

n5 = natural_number(5)
print(f"Factorial of {n5.n} is {n5.factorial()}")

for n in range(1, 11): 
    n_obj = natural_number(n)
    print(f"Is {n} prime? {n_obj.is_prime()}")  
