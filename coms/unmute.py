import asyncio, discord
try:
    from _command import Command
except:
    from coms._command import Command
import time
import pickle


class Com(Command):
    def __init__(self):
        self.usage = "!unmute @user"
        self.description = "Unmutes a user!"

        self.keys = ["!unmute", ".unmute", "muten't"]
        self.permissions = ["Developer", "Moderator", "Moderator-In-Training", ":)"]


    async def command(self, client, message, rawtext):
        user = message.mentions[0]

        mutefile = open("./assets/mutes.pkl", "rb")
        mutes = pickle.load(mutefile)
        mutefile.close()
        
        try:
            del mutes[user.name]
            await self.send(client, message.channel, "User unmuted.")
        except:
            await self.send(client, message.channel, "That user isn't muted!")

        mutefile = open("./assets/mutes.pkl", "wb")
        pickle.dump(mutes, mutefile)
        mutefile.close()
    


if __name__ == "__main__":
    command = Com()
    print(command.help())


