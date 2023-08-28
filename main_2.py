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
"""
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
"""

class Particular(Automovil):
    def __init__(self, marca, modelo, num_ruedas, velocidad, cilindrada, num_puestos):
        super().__init__(marca, modelo, num_ruedas, velocidad, cilindrada)
        self.num_puestos = num_puestos

    def __str__(self):
        return f"{super().__str__()} Puestos: {self.num_puestos}"


class Carga(Automovil):
    def __init__(self, marca, modelo, num_ruedas, velocidad, cilindrada, peso_carga):
        super().__init__(marca, modelo, num_ruedas, velocidad, cilindrada)
        self.peso_carga = peso_carga

    def __str__(self):
        return f"{super().__str__()} Carga: {self.peso_carga} Kg"


class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, num_ruedas, tipo_bicicleta):
        super().__init__(marca, modelo, num_ruedas)
        self.tipo_bicicleta = tipo_bicicleta

    def __str__(self):
        return f"{super().__str__()} Tipo: {self.tipo_bicicleta}"


class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, num_ruedas, tipo_bicicleta, motor, cuadro, nro_radios):
        super().__init__(marca, modelo, num_ruedas, tipo_bicicleta)
        self.motor = motor
        self.cuadro = cuadro
        self.nro_radios = nro_radios

    def __str__(self):
        return f"{super().__str__()} Motor: {self.motor}, Cuadro: {self.cuadro}, Nro Radios: {self.nro_radios}"


def main():
    particular = Particular("Ford", "Fiesta", 4, "180", "500", 5)
    carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
    bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
    motocicleta = Motocicleta("BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", "21")

    vehiculos = [particular, carga, bicicleta, motocicleta]

    for vehiculo in vehiculos:
        print(vehiculo)
        print("Motocicleta es instancia con relación a Vehículo:", isinstance(vehiculo, Vehiculo))
        print("Motocicleta es instancia con relación a Automovil:", isinstance(vehiculo, Automovil))
        print("Motocicleta es instancia con relación a Vehículo particular:", isinstance(vehiculo, Particular))
        print("Motocicleta es instancia con relación a Vehículo de Carga:", isinstance(vehiculo, Carga))
        print("Motocicleta es instancia con relación a Bicicleta:", isinstance(vehiculo, Bicicleta))
        print("Motocicleta es instancia con relación a Motocicleta:", isinstance(vehiculo, Motocicleta))
        print()

if __name__ == "__main__":
    main()
