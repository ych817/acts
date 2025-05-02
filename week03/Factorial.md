# Activity 3: 

rewrite below sample code (from activity w3-6) without using `__init__` & `self` (if it is possible?)

```python
class Factorial:
    def __init__(self, num1):  # Constructor to initialize the number
        self.num1 = num1
    def factorial(self):  # Factorial method now works with self.num1
        result = 1  # Initialized before the loop to store the product.
        for i in range(1, self.num1 + 1):
            result *= i
        return result
    def check_Prime(self):  # Prime check method added
        if self.num1 < 2:  # 0 and 1 are not prime numbers
            return False
        for i in range(2, int(self.num1 ** 0.5) + 1): # Check up to the square root of num1 and int to make it not show decimal values
            # Check if num1 is divisible by i 
            if self.num1 % i == 0:
                return False
        return True
 
    def display(self):  # Display method corrected
        print("Factorial of", self.num1, "is", self.factorial())
        if self.check_Prime():
            print(f"{self.num1} is a prime number.")
        else:
            print(f"{self.num1} is not a prime number.")
 
# Instantiate the class with number 5
number1 = Factorial(10)
 
# Call the display method to show the result
number1.display()
```

> **Answer** : I do not know .
>
> By the way I think it would be appropriate to write the name of the `Factorial` class  as `Natural` , since either calculating factorial of a number or determine whether a number is a prime are to **interfaces** of `Natural` class . 