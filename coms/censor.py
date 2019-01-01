import asyncio, discord
try:
    from _command import Command
except:
    from coms._command import Command
import pickle
from profanity import profanity
import time


class Com(Command):
    def __init__(self):
        self.usage = "*"
        self.description = "Censors words and phrases."

        self.keys = ["*"]
        self.permissions = ["*"]


    async def command(self, client, message, rawtext):
        pkl = open("./assets/blacklist.pkl", "rb")
        blacklist = pickle.load(pkl)
        pkl.close()


        profanity.load_words(blacklist)
        
        if profanity.contains_profanity(rawtext.lower()):
            print("CENSORED \'" + message.content + "\' from " + message.author.name)
            await message.delete()
            await self.send(client, message.author, "Please don't say that. i don't like it. :)")
            
            embed=discord.Embed(title="Censor", description='Censored \'' + message.content + '\' from ' + 
                    message.author.mention,color=0xAB987F)
        
            await self.send(client, client.get_channel(505878189185302572), embed=embed)


        mutefile = open("./assets/mutes.pkl", "rb")
        mutes = pickle.load(mutefile)
        mutefile.close()

        if message.author.name in mutes.keys():
            if mutes[message.author.name] < time.time():
                del mutes[message.author.name]
            else:
                await message.delete()

            mutefile = open("./assets/mutes.pkl", "wb")
            pickle.dump(mutes, mutefile)
            mutefile.close()
      

if __name__ == "__main__":
    command = Com()
    print(command.help())


