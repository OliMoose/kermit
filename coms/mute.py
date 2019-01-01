import asyncio, discord
try:
    from _command import Command
except:
    from coms._command import Command
import time
import pickle


class Com(Command):
    def __init__(self):
        self.usage = "!mute @user [minutes]"
        self.description = "Mutes a user for a set amount of time- if no time is given, it defaults to 30 minutes."

        self.keys = ["!mute", ".mute", "mute_"]
        self.permissions = ["Developer", "Moderator", "Moderator-In-Training", ":)"]


    async def command(self, client, message, rawtext):
        user = message.mentions[0]
        try:
            seconds = float(rawtext.split()[1]) * 60.0
        except Exception as e:
            print(e)
            seconds = 1800

        mutefile = open("./assets/mutes.pkl", "rb")
        mutes = pickle.load(mutefile)
        mutefile.close()
        
        try:
            if mutes[user.name] > time.time():
                await self.send(client, message.channel, "That user is already muted, for another " + 
                        str((mutes[user.name] - time.time()) / 60) + " minutes.")
            else:
                raise
        except:
            mutes[user.name] = time.time() + seconds
            await self.send(client, message.channel, "User muted for " + str(seconds / 60) + " minutes!")

        mutefile = open("./assets/mutes.pkl", "wb")
        pickle.dump(mutes, mutefile)
        mutefile.close()
    


if __name__ == "__main__":
    command = Com()
    print(command.help())


