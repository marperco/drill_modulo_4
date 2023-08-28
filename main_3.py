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

import csv

class Vehiculo:
    def __init__(self, marca, modelo, num_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.num_ruedas = num_ruedas

    def __str__(self):
        return f"{' '.join([f'{key}: {value}' for key, value in self.__dict__.items()])}"

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, num_ruedas, velocidad, cilindrada):
        super().__init__(marca, modelo, num_ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

class Particular(Automovil):
    def __init__(self, marca, modelo, num_ruedas, velocidad, cilindrada, num_puestos):
        super().__init__(marca, modelo, num_ruedas, velocidad, cilindrada)
        self.num_puestos = num_puestos

class Carga(Automovil):
    def __init__(self, marca, modelo, num_ruedas, velocidad, cilindrada, peso_carga):
        super().__init__(marca, modelo, num_ruedas, velocidad, cilindrada)
        self.peso_carga = peso_carga

def guardar_datos_csv(nombre_archivo, vehiculos):
    try:
        with open(nombre_archivo, "w", newline='') as archivo:
            archivo_csv = csv.writer(archivo)
            for vehiculo in vehiculos:
                datos = [type(vehiculo).__name__, str(vehiculo.__dict__)]
                archivo_csv.writerow(datos)
        print("Datos guardados exitosamente en", nombre_archivo)
    except Exception as e:
        print("Error al guardar los datos:", str(e))


def leer_datos_csv(nombre_archivo):
    vehiculos = []
    try:
        with open(nombre_archivo, "r") as archivo:
            archivo_csv = csv.reader(archivo)
            for vehiculo_tipo, vehiculo_datos in archivo_csv:
                vehiculo_datos = eval(vehiculo_datos)
                if vehiculo_tipo == "Particular":
                    vehiculo = Particular(**vehiculo_datos)
                elif vehiculo_tipo == "Carga":
                    vehiculo = Carga(**vehiculo_datos)
                elif vehiculo_tipo == "Bicicleta":
                    vehiculo = Bicicleta(**vehiculo_datos)
                elif vehiculo_tipo == "Motocicleta":
                    vehiculo = Motocicleta(**vehiculo_datos)
                else:
                    print(f"Tipo de vehículo desconocido: {vehiculo_tipo}")
                    continue  # Salta a la siguiente iteración del ciclo
                vehiculos.append(vehiculo)
        print("Datos recuperados exitosamente de", nombre_archivo)
        return vehiculos
    except Exception as e:
        print("Error al leer los datos:", str(e))
        return []


def main():
    particular = Particular("Ford", "Fiesta", "4", "180", "500", "5")
    carga = Carga("Daft Trucks", "G 38", "10", "120", "1000", "20000")
    bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
    motocicleta = Motocicleta("BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)

    vehiculos = [particular, carga, bicicleta, motocicleta]

    guardar_datos_csv("vehiculos.csv", vehiculos)

    vehiculos_recuperados = leer_datos_csv("vehiculos.csv")

    for vehiculo in vehiculos_recuperados:
        print()
        print("Lista de Vehiculos", type(vehiculo).__name__)
        print(vehiculo.__dict__)

if __name__ == "__main__":
    main()

from Vehiculo import Automovil
import csv
def guardar(nombre_archivo, Automovil):
    archivo = open(nombre_archivo, "w")
    datos = [(Automovil.__class__, Automovil.__dict__)]
    archivo_csv = csv.writer(archivo)
    archivo_csv.writerows(datos)
    archivo.close()
def recuperar(nombre_archivo):
    vehiculos = []
    archivo = open(nombre_archivo, "r")
    archivo_csv = csv.reader(archivo)
    for vehiculo in archivo_csv:
        vehiculos.append(vehiculo)
    archivo.close()
    return vehiculos
automovil = Automovil("Ford", "Fiesta", "4", "180", "500")
guardar("ejemplo.csv", automovil)
automoviles = recuperar("ejemplo.csv")
for automovil in automoviles:
    print(automovil)
