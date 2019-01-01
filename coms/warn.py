import asyncio, discord
try:
    from _command import Command
except:
    from coms._command import Command
import pickle


class Com(Command):
    def __init__(self):
        self.usage = "!warn @user [rule #]"
        self.description = "Warns the user, logs what happened, and direct messages the rule to them."

        self.keys = ["!warn", ".warn", "bad boy"]
        self.permissions = ["Developer", "Moderator", "Moderator-In-Training", ":)"]


    async def command(self, client, message, rawtext):
        rulefile = open("./assets/rules.pkl", "rb")
        rules = pickle.load(rulefile)
        rulefile.close()

        warnfile = open("./assets/rules.pkl", "rb")
        warns = pickle.load(warnfile)
        warnfile.close()


        await self.send(client, message.mentions[0], rules[str(int(rawtext[-2:]))])
        await self.send(client, message.channel, "User warned!")

        try:
            warns[message.mentions[0].name] += 1
        except:
            warns[message.mentions[0].name] = 1
        
        userwarns = warns[message.mentions[0].name]

        embed=discord.Embed(title="Warn", description='Warn from ' + message.author.mention +
                ' to ' + message.mentions[0].mention + ' in #' + message.channel.name + '\n*Rule: ' +
                str(int(rawtext[-2:])) + '*\nUser warns: **' + str(userwarns) + '**',
                color=0x2874A6)
        
        await self.send(client, client.get_channel(505878189185302572), embed=embed)

        warnfile = open("./assets/rules.pkl", "wb")
        warns = pickle.dump(warns, warnfile)
        warnfile.close()




if __name__ == "__main__":
    command = Com()
    print(command.help())


