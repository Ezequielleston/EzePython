
class Cliente:
    def __init__(self, nombre, email, direccion, DNI):
        self.nombre = nombre
        self.email = email
        self.direccion = direccion
        self.DNI = DNI
        self.carrito = []

    def agregar_al_carrito(self, producto):
        self.carrito.append(producto)
        print(f"{producto} agregado al carrito.")

    def mostrar_carrito(self):
        if not self.carrito:
            print("El carrito esta vacio.")
        else:
            print("Productos en el carrito:")
            for producto in self.carrito:
                print("-", producto)

    def vaciar_carrito(self):
        self.carrito = []
        print("El carrito ha sido vaciado.")

    def __str__(self):
        return f"Nombre: {self.nombre}\nEmail: {self.email}\nDireccion: {self.direccion}\nDNI: {self.DNI}"


