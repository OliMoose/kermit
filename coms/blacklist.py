import asyncio, discord
try:
    from _command import Command
except:
    from coms._command import Command
import pickle


class Com(Command):
    def __init__(self):
        self.usage = "!blacklist"
        self.description = "Direct Messages you with the blacklist, if you have permission."

        self.keys = ["!blacklist", "!banned", "!censored"]
        self.permissions = ["Developer", "Moderator", "Moderator-In-Training", ":)"]


    async def command(self, client, message, rawtext):
        pkl = open("./assets/blacklist.pkl", "rb")
        blacklist = pickle.load(pkl)
        pkl.close()

        text = "**Censored:**\n"
        for word in blacklist:
            text += word + "\n"

        await self.send(client, message.author, message=text)
        await self.send(client, message.channel, message="ooo i sent you the blacklist, be careful with it")
    


if __name__ == "__main__":
    command = Com()
    print(command.help())


