class Vehicle():
    def __init__(self, color, number_wheels):
        self.color = color
        self.number_wheels = number_wheels

    def __str__(self):
        return f"Color: {self.color}, {self.number_wheels} Wheels"
