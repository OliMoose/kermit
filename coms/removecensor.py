import asyncio, discord
try:
    from _command import Command
except:
    from coms._command import Command
import pickle


class Com(Command):
    def __init__(self):
        self.usage = "!removecensor [text]"
        self.description = "Uncensors the word, if you have permission."

        self.keys = ["!removecensor", ".removecensor", "!uncensor"]
        self.permissions = ["Developer", "Moderator", "Moderator-In-Training", ":)"]


    async def command(self, client, message, rawtext):
        pkl = open("./assets/blacklist.pkl", "rb")
        blacklist = pickle.load(pkl)
        pkl.close()              
        
        try:
            blacklist.remove(rawtext.lower())
        except:
            await self.send(client, message.channel, message="I don't censor that.")
            return

        pkl = open("./assets/blacklist.pkl", "wb")
        pickle.dump(blacklist, pkl)
        pkl.close()
        
        await self.send(client, message.channel, message="Uncensored!")
    


if __name__ == "__main__":
    command = Com()
    print(command.help())


