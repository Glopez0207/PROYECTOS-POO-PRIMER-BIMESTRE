from clases import ControlLedBCM, ControlbotonBCM

parpadeo = ControlLedBCM(18)
controlboton = ControlbotonBCM(18, 25)

def menu():
    print("\n=== MEnu ===")
    print("1. Parpadeo LED")
    print("2. Controlar LED con boton")
    print("3. Salir")
    opcion = input("Elige una opcion: ")
    return opcion

opcion = menu()

if opcion == "1":
    parpadeo.parpadea()
if opcion == "2":
    controlboton.controlarboton()
if opcion == "3":
    print("Saliendo...")
