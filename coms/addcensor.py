import asyncio, discord
try:
    from _command import Command
except:
    from coms._command import Command
import pickle


class Com(Command):
    def __init__(self):
        self.usage = "!addcensor [text]"
        self.description = "Makes the phrase censored, if you have permission!"

        self.keys = ["!addcensor", "!censor", "!addblacklist"]
        self.permissions = ["Developer", "Moderator", "Moderator-In-Training", ":)"]


    async def command(self, client, message, rawtext):
        pkl = open("./assets/blacklist.pkl", "rb")
        blacklist = pickle.load(pkl)
        pkl.close()
        
        blacklist.append(rawtext.lower())

        pkl = open("./assets/blacklist.pkl", "wb")
        pickle.dump(blacklist, pkl)
        pkl.close()
        
        await self.send(client, message.channel, message="I'll now censor " + rawtext + ", yay")
    


if __name__ == "__main__":
    command = Com()
    print(command.help())


