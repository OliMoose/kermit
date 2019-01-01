import asyncio, discord
try:
    from _command import Command
except:
    from coms._command import Command



class Com(Command):
    def __init__(self):
        self.usage = "!purge [number of messages]"
        self.description = "Deletes all the messages!"

        self.keys = ["!purge", ".purge"]
        self.permissions = ["Developer", "Moderator", "Moderator-In-Training", ":)"]


    async def command(self, client, message, rawtext):
        deleted = await message.channel.purge(limit=int(rawtext) + 1)
        await self.send(client, message.channel, 'Deleted {} message(s)!'.format(len(deleted)))
    


if __name__ == "__main__":
    command = Com()
    print(command.help())


