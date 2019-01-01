import asyncio, discord
try:
    from _command import Command
except:
    from coms._command import Command
import pathlib


class Com(Command):
    def __init__(self):
        self.usage = "!help"
        self.description = "Gives some basic help info about kermi"

        self.keys = ["!help", "bot help", ".help", "!commands", ".commands"]
        self.permissions = ["*"]


    async def command(self, client, message, rawtext):
        msg = "**Kermit's info!**\nTo find out more info about any of the commands below, run them with -help after them.\n*e.g\t\t"
        msg += "!deepfry -help*\n\n**Commands:**\n"

        curdir = pathlib.Path('./coms')


        for command in curdir.iterdir():
            if command.name[0] != "_" and command.name[0] != ".":
                com = __import__("coms")
                com = getattr(com, command.name[:-3])

                comobj = com.Com()
                if not comobj.keys[0] == "*":
                    msg += comobj.keys[0] + "\n"

        await self.send(client, message.channel, msg)
    


if __name__ == "__main__":
    command = Com()
    print(command.help())


