class Vehiculo:
    def __init__(self, marca, modelo, num_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.num_ruedas = num_ruedas

    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.num_ruedas} ruedas"


class Automovil(Vehiculo):
    def __init__(self, marca, modelo, num_ruedas, velocidad, cilindrada):
        super().__init__(marca, modelo, num_ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return f"{super().__str__()} {self.velocidad} Km/h, {self.cilindrada} cc"

print() 
def main():
    num_vehiculos = int(input("Cuantos Vehiculos desea insertar: "))
    vehiculos = []

    for i in range(num_vehiculos):
        print() 
        print(f"Datos del automóvil {i+1}")
        marca = input("Inserte la marca del automóvil: ")
        modelo = input("Inserte el modelo: ")
        num_ruedas = int(input("Inserte el número de ruedas: "))
        velocidad = int(input("Inserte la velocidad en km/h: "))
        cilindrada = int(input("Inserte el cilindraje en cc: "))

        automovil = Automovil(marca, modelo, num_ruedas, velocidad, cilindrada)
        vehiculos.append(automovil)

    print("\nImprimiendo por pantalla los Vehículos:")
    print() 
    for i, vehiculo in enumerate(vehiculos, start=1):
        print(f"Datos del automóvil {i} : {vehiculo}")


if __name__ == "__main__":
    main()
