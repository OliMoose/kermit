import asyncio, discord
try:
    from _command import Command
except:
    from coms._command import Command



class Com(Command):
    def __init__(self):
        self.usage = ""
        self.description = ""

        self.keys = [""]
        self.permissions = ["Developer", "Moderator", ":)"]


    async def command(self, client, message, rawtext):
        pass
    


if __name__ == "__main__":
    command = Com()
    print(command.help())


