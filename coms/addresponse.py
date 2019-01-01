import asyncio, discord
try:
    from _command import Command
except:
    from coms._command import Command
import pickle


class Com(Command):
    def __init__(self):
        self.usage = "!addresponse [text]#[response]"
        self.description = "Adds the response, if you have permission."

        self.keys = ["!addresponse", "!newresponse", "!makeresponse"]
        self.permissions = ["Developer", "Moderator", "Moderator-In-Training", ":)"]


    async def command(self, client, message, rawtext):
        pkl = open("./assets/responses.pkl", "rb")
        responses = pickle.load(pkl)
        pkl.close()
        
        msg = rawtext.split("#")
        responses[msg[0].lower()] = msg[1]

        pkl = open("./assets/responses.pkl", "wb")
        responses = pickle.dump(responses, pkl)
        pkl.close()
        
        await self.send(client, message.channel, message="I will now respond to " + msg[0].lower() + "!")
    


if __name__ == "__main__":
    command = Com()
    print(command.help())


