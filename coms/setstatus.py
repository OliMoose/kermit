import asyncio, discord
try:
    from _command import Command
except:
    from coms._command import Command
from profanity import profanity


class Com(Command):
    def __init__(self):
        self.usage = "!setstatus [1 for \'playing\', 2 for \'streaming\'] [rest of the status]"
        self.description = "Set's kermit's status!"

        self.keys = ["!setstatus", "oi kermit do"]
        self.permissions = ["*"]


    async def command(self, client, message, rawtext):
        if profanity.contains_profanity(rawtext.lower()):
            return
        
        if rawtext[0] == "1":
            await client.change_presence(activity=discord.Game(name=rawtext[2:]))
            await self.send(client, message.channel, "i'm now playing " + rawtext[2:])
        else:
            await client.change_presence(activity=discord.Streaming(name=rawtext[2:], url="https://twitch.tv/kermit"))
            await self.send(client, message.channel, "i'm now streaming " + rawtext[2:])
    


if __name__ == "__main__":
    command = Com()
    print(command.help())


