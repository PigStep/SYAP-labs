class Circle:
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2  # pi*R^2

    def perimeter(self):
        return 2 * 3.14 * self.radius  # 2pi*R


circle = Circle(5)

print(circle.radius)
print(circle.area())
print(circle.perimeter())
