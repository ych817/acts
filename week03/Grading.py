# grading_system.py

class Student:
    """
    Represents a student with a name and grades for three courses.
    Grades are private and accessed via getter/setter methods.
    """

    def __init__(self, name, mse800, mse801, mse802):
        """
        Initializes a student with name and three course grades.
        Grades must be between 0 and 100.
        """
        self.name = name
        self.set_mse800(mse800)
        self.set_mse801(mse801)
        self.set_mse802(mse802)

    # ----- Private attributes -----
    __mse800 = 0.0
    __mse801 = 0.0
    __mse802 = 0.0

    # ----- Getter methods -----
    def get_mse800(self):
        return self.__mse800

    def get_mse801(self):
        return self.__mse801

    def get_mse802(self):
        return self.__mse802

    # ----- Setter methods -----
    def set_mse800(self, score):
        if 0 <= score <= 100:
            self.__mse800 = score
        else:
            raise ValueError("MSE800 score must be between 0 and 100.")

    def set_mse801(self, score):
        if 0 <= score <= 100:
            self.__mse801 = score
        else:
            raise ValueError("MSE801 score must be between 0 and 100.")

    def set_mse802(self, score):
        if 0 <= score <= 100:
            self.__mse802 = score
        else:
            raise ValueError("MSE802 score must be between 0 and 100.")

    # ----- Display method -----
    def display(self):
        """
        Prints the student's name and all three course grades.
        """
        print(f"Student: {self.name}")
        print(f"  MSE800: {self.get_mse800()}")
        print(f"  MSE801: {self.get_mse801()}")
        print(f"  MSE802: {self.get_mse802()}")
        print()


# ----- Example usage -----
if __name__ == "__main__":
    # Create students
    s1 = Student("Alice", 85, 90, 78)
    s2 = Student("Bob", 70, 88, 92)

    # Display student records
    s1.display()
    s2.display()

    # Example of modifying grades using setters
    s1.set_mse800(95)
    print("After updating Alice's MSE800:")
    s1.display()

    # Example of invalid grade assignment
    try:
        s2.set_mse801(110)
    except ValueError as e:
        print("Error:", e)
