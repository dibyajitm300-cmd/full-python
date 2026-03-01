class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, c2):
        return Complex(self.real + c2.real, self.imaginary + c2.imaginary)

    def __mul__(self, c2):
        # Formula: (a + bi)(c + di) = (ac - bd) + (ad + bc)i
        real_part = self.real * c2.real - self.imaginary * c2.imaginary
        imaginary_part = self.real * c2.imaginary + self.imaginary * c2.real
        return Complex(real_part, imaginary_part)

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"


# Example usage
c = Complex(2, 4)
c2 = Complex(3, 7)

print("Addition:", c + c2)       # 5 + 11i
print("Multiplication:", c * c2) # -22 + 26i