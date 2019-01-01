import asyncio, discord
try:
    from _command import Command
except:
    from coms._command import Command
import pickle


class Com(Command):
    def __init__(self):
        self.usage = "*"
        self.description = "Replies to messages with a set response."

        self.keys = ["*"]
        self.permissions = ["*"]


    async def command(self, client, message, rawtext):
        pkl = open("./assets/responses.pkl", "rb")
        responses = pickle.load(pkl)
        pkl.close()
        
        try:
            await self.send(client, message.channel, message=responses[rawtext.lower()])
        except:
            pass
    


if __name__ == "__main__":
    command = Com()
    print(command.help())


