import asyncio, discord
try:
    from _command import Command
except:
    from coms._command import Command
import sys


class Com(Command):
    def __init__(self):
        self.usage = "!update"
        self.description = "Updates the bot"

        self.keys = ["!update", "yo kermi update"]
        self.permissions = ["Developer", ":)"]


    async def command(self, client, message, rawtext):
        await self.send(client, message.channel, "Reloading! bai")
        sys.exit(0)


if __name__ == "__main__":
    command = Com()
    print(command.help())


