
class Mamifero:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color

    def mostrar_dato(self):
        return f"Nombre: {self.nombre}, color: {self.color} "

class Domestico(Mamifero):
    def __init__(self, nombre, color , dueño):
        super().__init__(nombre, color )
        self.dueño = dueño

    def mostrar_dato(self):
        return f"{super().mostrar_dato()}, Dueño: {self.dueño}"

class Perro(Domestico):
    def __init__(self, nombre, color, dueño, raza):
        super().__init__(nombre, color, dueño)
        self.raza = raza

    def mostrar_dato(self):
        return f"{super().mostrar_dato()}, Raza: {self.raza}"

mi_perro = Perro("Max", "negro" , "Pedro", "Pastor Aleman")

print(mi_perro.mostrar_dato())
