def crear_usuario():
    usuario = input("Ingrese un nombre de usuario: ")
    clave = input("Ingrese una contraseña: ")
    with open("usuarios.txt", "a") as archivo:
        archivo.write(f"{usuario}-{clave}\n")
    print("¡Usuario creado exitosamente!")
    menu()


def iniciar_sesion():
    usuario = input("Ingrese su nombre de usuario: ")
    clave = input("Ingrese su contraseña: ")
    with open("usuarios.txt", "r") as archivo:
        usuarios = archivo.read().splitlines()
        for usuario_guardado in usuarios:
            if usuario_guardado == f"{usuario}-{clave}":
                print("¡Inicio de sesion exitoso!")
                #llama funcion para imprimir datos
                imprimir_datos_txt(nombre_archivo)
                return
        print("Nombre de usuario o contraseña incorrectos, intente nuevamente")
        iniciar_sesion()

nombre_archivo = 'usuarios.txt'
usuario=0
def imprimir_datos_txt(archivo):
    try:
        with open(archivo, 'r') as archivo_txt:
            datos = archivo_txt.readlines()
            contador = 1
            print("Lista de usuarios inscriptos:")
            print("")
            for linea in datos:
                print("Usuario", contador, ":", linea.strip())
                contador += 1

    except FileNotFoundError:
        print("No se encontro el archivo.")
    except IOError:
        print("Ocurrio un error al leer el archivo.")

def menu():
    print("Bienvenido al programa de usuarios.")
    print("1. Crear usuario")
    print("2. Iniciar sesion")
    opcion = input("Seleccione una opcion (1 o 2): ")
    if opcion == "1":
        crear_usuario()
    elif opcion == "2":
        iniciar_sesion()
    else:
        print("Opcion invalida. Por favor, seleccione nuevamente.")
        menu()


menu()