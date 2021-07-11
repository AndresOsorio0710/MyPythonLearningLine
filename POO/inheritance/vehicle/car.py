from .vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, color, number_wheels, velocity, cylinder_capacity):
        # 1- self.color = color
        # 1- self.number_wheels = number_wheels
        # 2- Vehicle.__init__(self, color, number_wheels)
        # Ventaja que si cambio el nombre d ela clase, al momento de heredar no tengo que cambiar el codigo
        super().__init__(color, number_wheels)
        self.velocity = velocity
        self.cylinder_capacity = cylinder_capacity

    def __str__(self):
        # 1- return f"Color: {self.color}, {self.velocity} km/h, {self.number_wheels} Wheels, {self.cylinder_capacity} cc"
        # 2- return Vehicle.__str__(self)+f" {self.velocity} km/h, {self.cylinder_capacity} cc"
        return super().__str__()+f" {self.velocity} km/h, {self.cylinder_capacity} cc"
