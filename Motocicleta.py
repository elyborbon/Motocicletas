class Motocicleta():
    status = "Nuevo"
    motor = "False"

    def __init__(self, color, matricula, combustible_litros, numero_ruedas, marca, modelo, fecha_fabricacion, velocida_punta, peso):
        self.color = color
        self.matricula = matricula
        self.combustible_litros = combustible_litros
        self.numero_ruedas = numero_ruedas
        self.marca = marca
        self.modelo = modelo
        self.fecha_fabricacion = fecha_fabricacion
        self.velocidad_punta = velocida_punta
        self.peso = peso

    def arrancar (self):
        if not self.motor:
            print ("El motor esta encendido.")
        else:
            print ("El motor ya esta en marcha. ")

    def detener (self):
        if self.motor:
            print ("El motor se ha apagado.")
        else:
            print ("El motor ya esta apagado ")

    def consulta (self):
        print("El precio de la motocicleta 1 es de: {}". format (self.precio))

moto_1 = Motocicleta("Amarillo", "2BCD", 10, 2, "Yamaha", "R1", "30/02/2016", 250, 180)
moto_1.detener()
moto_1.precio = 3500
moto_1.consulta()