import asyncio, discord
import traceback


class Command(object):
    def __init__(self):
        self.usage = "!example [text] [othertext]"
        self.description = "An example command."
        
        self.keys = ["!example", ".example"]
        self.permissions = ["Developer", "*"]


    def help(self):
        return self.description + "\n\n*Usage:*\n```" + self.usage + "```\n*Aliases:*\n" + ", ".join(self.keys[1:])
    
    
    async def command(self, client, message):
        pass


    async def commandwrapper(self, client, message):
        try:
            allowed = False
            for role in message.author.roles:
                if role.name in self.permissions:
                    raise
        except:
            allowed = True

        if allowed or "*" in self.permissions:
            try:
                rawtext = message.content
                for key in self.keys:
                    if message.content.startswith(key):
                        rawtext = message.content[len(key) + 1:]

                await self.command(client, message, rawtext)
            except Exception as e:
                print(e)
                traceback.print_exc()
                await self.send(client, message.channel, message="Something went wrong!\n" + self.help())
            
            return

        await self.send(client, message.channel, message="You aren't allowed.")


    async def main(self, client, message):
        if "*" in self.keys:
            await self.commandwrapper(client, message)
            return

        for key in self.keys:
            if message.content.startswith(key):
                args = message.content[len(key) + 1:]

                if args == "-help":
                    await self.send(client, message.channel, message=self.help())
                else:
                    await self.commandwrapper(client, message)
                return
        
        await self.send(client, message.channel, message="*Usage:*\n```" + self.usage + "```")


    async def send(self, client, channel, message=None, embed=None):
        if embed:
            msg = await channel.send(embed=embed)
        else:
            print(message)
            msg = await channel.send(message)
        return msg

