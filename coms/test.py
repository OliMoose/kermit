import asyncio, discord
try:
    from _command import Command
except:
    from coms._command import Command
import time



class Com(Command):
    def __init__(self):
        self.usage = "!test"
        self.description = "Tests the bot's response time."

        self.keys = ["!test", ".test", "test?"]
        self.permissions = ["*"]


    async def command(self, client, message, rawtext):
        t1 = time.perf_counter()
        async with message.channel.typing():
            t2 = time.perf_counter()
        
            embed=discord.Embed(title=None, description='ultra-fast response time from kermit v3: {}'.format(round((t2-t1)*1000)),
                    color=0x2874A6)
        
        await self.send(client, message.channel, embed=embed)



if __name__ == "__main__":
    command = Com()
    print(command.help())


