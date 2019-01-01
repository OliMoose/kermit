import asyncio, discord
try:
    from _command import Command
except:
    from coms._command import Command
import pickle


class Com(Command):
    def __init__(self):
        self.usage = "!responses"
        self.description = "Direct Messages you with a list of all the responses!"

        self.keys = ["!responses", "what are the responses", ".responses"]
        self.permissions = ["*"]


    async def command(self, client, message, rawtext):
        pkl = open("./assets/responses.pkl", "rb")
        responses = pickle.load(pkl)
        pkl.close()

        text = "***Responses:***\n"
        for key in responses.keys():
            text += "**" + key + ":**\t\t" + responses[key] + "\n"

        await self.send(client, message.author, message=text)
        await self.send(client, message.channel, message="I sent the responses :))")
    


if __name__ == "__main__":
    command = Com()
    print(command.help())


