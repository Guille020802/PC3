#Pregunta 1

def get_fuel_percentage():
    while True:
        try:
            fraction = input("Ingrese una fracción en el formato X/Y: ")
            x, y = map(int, fraction.split('/'))

            if y == 0:
                raise ZeroDivisionError("El denominador no puede ser cero.")
            if x > y:
                print("X debe ser mayor o igual a Y.")
                continue
            
            percentage = (x / y) * 100

            if percentage < 1:
                return 'E'
            elif percentage > 99:
                return 'F'
            else:
                return f"{round(percentage)}%"

        except ValueError:
            print("Formato incorrecto. Ingrese dos números enteros separados por '/'.")
        except ZeroDivisionError as e:
            print(e)

if __name__ == "__main__":
    fuel_percentage = get_fuel_percentage()
    print(f"Cantidad de combustible en el tanque: {fuel_percentage}")

#Pregunta 2

def get_validated_grades():
    while True:
        try:
            grades_input = input("Ingrese las calificaciones separadas por comas: ")
            grades_list = grades_input.split(',')
            validated_grades = []

            for grade in grades_list:
                grade = grade.strip()
                validated_grades.append(int(grade))

            return validated_grades

        except ValueError:
            print("Error: Las calificaciones deben ser números enteros.")

if __name__ == "__main__":
    grades = get_validated_grades()
    print("Calificaciones válidas:", grades)

#Pregunta 3

import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self):
        area = math.pi * self.radio ** 2
        return area

if __name__ == "__main__":
    radio = float(input("Ingrese el radio del círculo: "))
    circulo = Circulo(radio)
    area = circulo.calcular_area()
    print(f"El área del círculo con radio {radio} es: {area:.2f}")

#Pregunta 4

class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
    
    def calcular_area(self):
        area = self.largo * self.ancho
        return area

if __name__ == "__main__":
    largo = float(input("Ingrese el largo del rectángulo: "))
    ancho = float(input("Ingrese el ancho del rectángulo: "))
    
    rectangulo = Rectangulo(largo, ancho)
    area = rectangulo.calcular_area()
    
    print(f"El área del rectángulo con largo {largo} y ancho {ancho} es: {area:.2f}")

# Pregunta 5

class Alumno:
    def __init__(self, nombre, numero_registro):
        self.nombre = nombre
        self.numero_registro = numero_registro
        self.edad = None
        self.notas = []

    def display(self):
        print(f"Información del estudiante:")
        print(f"Nombre: {self.nombre}")
        print(f"Número de registro: {self.numero_registro}")
        if self.edad is not None:
            print(f"Edad: {self.edad}")
        if self.notas:
            print("Notas:")
            for i, nota in enumerate(self.notas, start=1):
                print(f"Nota {i}: {nota}")

    def set_age(self, edad):
        self.edad = edad

    def set_notas(self, notas):
        self.notas = notas

if __name__ == "__main__":
    nombre = input("Ingrese el nombre del alumno: ")
    numero_registro = input("Ingrese el número de registro del alumno: ")

    alumno = Alumno(nombre, numero_registro)

    edad = int(input("Ingrese la edad del alumno: "))
    alumno.set_age(edad)

    num_notas = int(input("Ingrese la cantidad de notas: "))
    notas = []
    for i in range(num_notas):
        nota = float(input(f"Ingrese la nota {i + 1}: "))
        notas.append(nota)
    alumno.set_notas(notas)

    alumno.display()

#Pregunta 6

"Clase Restaurante"

class Restaurante:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurante: {self.restaurant_name}")
        print(f"Tipo de cocina: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"¡El restaurante {self.restaurant_name} está abierto!")

# Crear una instancia de la clase Restaurante
mi_restaurante = Restaurante("El Hornero", "Carnes")

# Llamar a los métodos
mi_restaurante.describe_restaurant()
mi_restaurante.open_restaurant()

"Tres Restaurantes"

class Restaurante:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurante: {self.restaurant_name}")
        print(f"Tipo de cocina: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"¡El restaurante {self.restaurant_name} está abierto!")

# Crear tres instancias de la clase Restaurante
restaurante1 = Restaurante("El Hornero", "Carnes")
restaurante2 = Restaurante("Mikumi", "Coreana")
restaurante3 = Restaurante("Queen Burguer", "Americana")

# Llamar a los métodos para cada instancia
restaurante1.describe_restaurant()
restaurante1.open_restaurant()

restaurante2.describe_restaurant()
restaurante2.open_restaurant()

restaurante3.describe_restaurant()
restaurante3.open_restaurant()

#Pregunta 7

import mi_modulo

if __name__ == "__main__":
    numeros_aleatorios = mi_modulo.generar_numeros_aleatorios(20, 0, 100)
    mi_modulo.mostrar_lista(numeros_aleatorios)
    
    mi_modulo.ordenar_y_mostrar(numeros_aleatorios)

#Pregunta 8

import operaciones

if __name__ == "__main__":
    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        
        print("Suma:", operaciones.suma(num1, num2))
        print("Resta:", operaciones.resta(num1, num2))
        print("Producto:", operaciones.producto(num1, num2))
        print("División:", operaciones.division(num1, num2))
        
        print("Intento de división por cero:", operaciones.division(num1, 0))
    except ValueError:
        print("Error: Ingresa valores numéricos válidos")    