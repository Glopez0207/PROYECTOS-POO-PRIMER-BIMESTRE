class RobotView:
    def mostrar(self, *partes):
        print(*partes)

    def titulo(self, titulo):
        print("\n---", titulo, "---\n")


# ? VISTA PARA TELEGRAM
class BotView:
    def __init__(self, bot):
        self.bot = bot

    def mostrar_mensaje(self, chat_id, *msg):
        mensaje = " ".join(str(x) for x in msg)
        self.bot.sendMessage(chat_id, mensaje)
