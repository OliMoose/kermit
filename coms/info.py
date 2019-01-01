import asyncio, discord
try:
    from _command import Command
except:
    from coms._command import Command



class Com(Command):
    def __init__(self):
        self.usage = "!info"
        self.description = "Gives info about mcskewl"

        self.keys = ["!info", ".info"]
        self.permissions = ["*"]


    async def command(self, client, message, rawtext):
        embed=discord.Embed(title="mcskewls", description="the man, the myth, the mlg MCer\n" +
                "**Age:**\t\t18\n**Favourite Food:**\t\tPizza\n**Steam profile:**\t\t" + 
                "https://steamcommunity.com/id/minecraftintheschooltoilets\n**Favourite game:**\t\t" +
                "Tied between TF2 and Mario Kart DS\n**Favourite animal:**\t\tSloth\n" +
                "**Favourite TV Series:**\t\tFirefly/Mr Robot\n")
        await self.send(client, message.channel, embed=embed)
    


if __name__ == "__main__":
    command = Com()
    print(command.help())


