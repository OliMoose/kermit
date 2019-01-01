import asyncio, discord
try:
    from _command import Command
except:
    from coms._command import Command
import urbandictionary as ud


class Com(Command):
    def __init__(self):
        self.usage = "!urban [text]"
        self.description = "Searches Urban Dictionary for the definition"

        self.keys = ["!urban", ".urban", "!urbandictionary"]
        self.permissions = ["*"]


    async def command(self, client, message, rawtext):
        defs = ud.define(rawtext)
        if len(defs) == 0:
            await self.send(client, message.channel, "sorry, that doesn't exist")
        else:
            ind = 0
            going = True
            while going:
                uddef = defs[ind]
                notwanted = "[]"

                definition = uddef.definition
                example = uddef.example

                for char in notwanted:
                    definition = definition.replace(char, '')
                    example = example.replace(char, '')

                emb=discord.Embed(title="\t\t\t" + uddef.word, description=definition + "\n\n**Example:**\n*" + 
                        example + "*\n\n:thumbsup:  " + str(uddef.upvotes) + 
                        "\t\t:thumbsdown:  " + str(uddef.downvotes), color= 0x303030)
                
                try:
                    await self.send(client, message.channel, embed=emb)
                    going = False
                except:
                    ind += 1
    


if __name__ == "__main__":
    command = Com()
    print(command.help())


