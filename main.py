from Paquete_EZEQUIEL.Modulo2 import Cliente

if __name__ == "__main__":
    
    cliente1 = Cliente("Roman Perez", "roman@coder.com", "Calle 123, Ciudad de Berazategui", "22/576/908")
    cliente2 = Cliente("Paola Lopez", "paola@coder.com", "Avenida mitre,  Ciudad Avellaneda", "44/867/927")

    # Mostrar informacion de los clientes
    print("Informacion de Cliente 1:")
    print(cliente1)
    print()

    print("Informacion de Cliente 2:")
    print(cliente2)
    print()

    # Agregar productos al carrito del cliente 1
    cliente1.agregar_al_carrito("| Macbook")
    cliente1.agregar_al_carrito("| iPhone")
    cliente1.agregar_al_carrito("| Airpods")

    # Mostrar el carrito del cliente 1
    cliente1.mostrar_carrito()

    # Vaciar el carrito del cliente 1
    cliente1.vaciar_carrito()
    cliente1.mostrar_carrito()
    
    # Agregar productos al carrito del cliente 2
    cliente2.agregar_al_carrito("| PC gamer")
    cliente2.agregar_al_carrito("| Samsumg s23")
    cliente2.agregar_al_carrito("| Tablet")

    # Mostrar el carrito del cliente 2
    cliente2.mostrar_carrito()

    # Vaciar el carrito del cliente 2
    cliente2.vaciar_carrito()
    cliente2.mostrar_carrito()