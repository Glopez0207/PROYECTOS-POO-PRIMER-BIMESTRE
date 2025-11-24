from controlador import RobotController
import time
TOKEN = "8374308621:AAEhpi0U1A4AkZPxQVzqObSXiuni6vHdzqA"   

controller = RobotController(TOKEN)

controller.encender_robot_inicial()
time.sleep(5)

controller.apagar_robot_inicial()
time.sleep(3)

controller.view.titulo("ROBOT MEDICO")

controller.diagnosticar_medico()
time.sleep(3)
controller.diagnosticar_medico()
time.sleep(3)
controller.diagnosticar_medico()
time.sleep(3)

controller.view.titulo("ROBOT EXPLORADOR")


print("Sistema ejecutdndose con Telegram...")

while True:
    time.sleep(1)

