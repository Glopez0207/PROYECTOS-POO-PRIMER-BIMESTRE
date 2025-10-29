import funciones
import os
from funciones import led_on
from funciones import led_on_board
from funciones import  control_led_board
from funciones import control_led_bcm
import time
import RPi.GPIO as GPIO

def limpiar():
    os.system("clear")

def menu():
    while True:
        limpiar()
        print("====================================")
        print("     CONTROL DE LEDS Y BOTONES")
        print("====================================")
        print("1. Encender LED con modo BCM (pin 18)")
        print("2. Encender LED con modo BOARD (pin 12)")
        print("3. Controlar LED con boton en BOARD (LED 12, BTN 22)")
        print("4. Controlar LED con boton en BCM (LED 18, BTN 25)")
        print("0. Salir")
        print("====================================")

        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            led_on(18, GPIO.BCM)
            
        if opcion == "2":
            led_on_board(12, GPIO.BOARD)
            
        if opcion == "3":
            control_led_board()
           
        if opcion == "4":
            control_led_bcm()
           
        if opcion == "0":
            GPIO.cleanup()
            print("Saliendo del programa...")
            time.sleep(1)
            limpiar()
            break
        if opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4" and opcion != "0":
            print("Opcion invvlida, presiona ENTER para continuar...")
            input()
            continue

if __name__ == "__main__":
    menu()
