import asyncio, discord
try:
    from _command import Command
except:
    from coms._command import Command
import pickle


class Com(Command):
    def __init__(self):
        self.usage = "!rule [number]"
        self.description = "Lists the rule!"

        self.keys = ["!rule", "rule", ".rule"]
        self.permissions = ["*"]


    async def command(self, client, message, rawtext):
        pkl = open("./assets/rules.pkl", "rb")
        rules = pickle.load(pkl)
        pkl.close()
        await self.send(client, message.channel, rules[rawtext])
    


if __name__ == "__main__":
    command = Com()
    print(command.help())


