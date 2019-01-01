import asyncio, discord
try:
    from _command import Command
    import _deeppyer as deeppyer
except:
    from coms._command import Command
    import coms._deeppyer as deeppyer
from PIL import Image
import requests


class Com(Command):
    def __init__(self):
        self.usage = "!deepfry [red/blue] [attached image]"
        self.description = "Deepfries an image to hell and back hehe"

        self.keys = ["!deepfry", ".fry", "!fry"]
        self.permissions = ["*"]


    async def command(self, client, message, rawtext):
        if "blue" in rawtext:
            colour = deeppyer.DeepfryTypes.BLUE
        else:
            colour = deeppyer.DeepfryTypes.RED
            

        await self.send(client, message.channel, "Frying, wait for it...")
        att = message.attachments[0]
        img = Image.open(requests.get(att.url, stream=True).raw)
        img = await deeppyer.deepfry(img, type=colour)
        img.save('./assets/deepfried.jpg')
        await message.channel.send(file=discord.File("./assets/deepfried.jpg"))
    


if __name__ == "__main__":
    command = Com()
    print(command.help())


