class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method: Performs addition without accessing class or instance attributes.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method: Accesses the class attribute and performs multiplication.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
