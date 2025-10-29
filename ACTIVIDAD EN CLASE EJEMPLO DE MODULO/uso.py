import Modulo
import time

def menu():
    while True:
        print("\n==== MENÚ IoT (simulado) ====")
        print("1) Encender LED")
        print("2) Apagar LED")
        print("3) Blink LED (3 veces)")
        print("4) Salir")

        op = input("Elige una opción: ")
        if op == "1":
            Modulo.encender_led()
        if op == "2":
            Modulo.apagar_led()
        if op == "3":
            Modulo.blink_led()
        if op == "4":
            break


if __name__ == "__main__":
    menu()  
