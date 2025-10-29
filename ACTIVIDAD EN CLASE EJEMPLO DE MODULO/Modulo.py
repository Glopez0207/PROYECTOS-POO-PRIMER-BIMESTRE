import time

def encender_led(pin=12, modo="BOARD"):
    print(" LED encendido ✅")
    print("Ejecutando en modo ",modo," con pin",pin)
    time.sleep(1)

def apagar_led(pin=12, modo="BOARD"):
    print(" Ejecutando en modo",modo, "con pin" ,pin)
    print( "LED apagado ❌")
    time.sleep(1)

def blink_led(pin=12, modo="BOARD", veces=3):
    print("Ejecutando en modo",modo," con pin" ,pin)
    print(" Parpadeando LED 3 vces..." )

    for i in range(veces):
        print("parpadeo",i+1)
        time.sleep(1)
