class Calculator:

    def add(self, a, b):
        """Додавання двох чисел."""
        return a + b

    def subtract(self, a, b):
        """Віднімання другого числа від першого."""
        return a - b

    def multiply(self, a, b):
        """Множення двох чисел."""
        return a * b

    def divide(self, a, b):
        """Ділення першого числа на друге. Генерує помилку при діленні на нуль."""
        if b == 0:
            raise ValueError("Ділення на нуль неможливе.")
        return a / b
