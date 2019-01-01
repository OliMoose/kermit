import asyncio, discord
try:
    from _command import Command
except:
    from coms._command import Command
import pickle


class Com(Command):
    def __init__(self):
        self.usage = "!removeresponse [text]"
        self.description = "Removes the response, if you have permission."

        self.keys = ["!removeresponse", ".removeresponse", "!killresponse"]
        self.permissions = ["Developer", "Moderator", "Moderator-In-Training", ":)"]


    async def command(self, client, message, rawtext):
        pkl = open("./assets/responses.pkl", "rb")
        responses = pickle.load(pkl)
        pkl.close()              
        
        try:
            del responses[rawtext.lower()]
        except:
            await self.send(client, message.channel, message="I don't respond to that.")
            return

        pkl = open("./assets/responses.pkl", "wb")
        responses = pickle.dump(responses, pkl)
        pkl.close()
        
        await self.send(client, message.channel, message="Response deleted!")
    


if __name__ == "__main__":
    command = Com()
    print(command.help())


