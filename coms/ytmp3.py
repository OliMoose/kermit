from __future__ import unicode_literals
import asyncio, discord
try:
    from _command import Command
except:
    from coms._command import Command
    
import functools
from concurrent.futures import ThreadPoolExecutor
from youtube_dl import YoutubeDL
import math
import os
import time


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192'}],
    'outtmpl': './assets/%(title)s.%(ext)s'
}


class Downloader:
    def __init__(self, max_workers=3):
        self.thread_pool = ThreadPoolExecutor(max_workers=max_workers)
        self.ydl = YoutubeDL(ydl_opts)

    async def extract_info(self, loop, url, *args, on_error=None, **kwargs):
        try:
            return await loop.run_in_executor(self.thread_pool, functools.partial(self.ydl.extract_info, url, *args, **kwargs))

        except Exception as e:
            if asyncio.iscoroutinefunction(on_error):
                asyncio.ensure_future(on_error(e), loop=loop)

            elif asyncio.iscoroutine(on_error):
                asyncio.ensure_future(on_error, loop=loop)

            elif not callable(on_error):
                pass

            else:
                loop.call_soon_threadsafe(on_error, e)



downloader = Downloader()


class Com(Command):
    def __init__(self):
        self.usage = "!ytmp3 [YT link]"
        self.description = "Downloads the video as an mp3 and sends it to you!"

        self.keys = ["!ytmp3", "!youtubeaudio", "give me mp3"]
        self.permissions = ["*"]


    async def command(self, client, message, rawtext):
        await self.send(client, message.channel, "**Downloading/Converting...** (pls wait a bit)")
        songdata = await downloader.extract_info(client.loop, rawtext)
        await self.send(client, message.channel, "**Got mp3! Sending...** (pls wait a longer bit)")
        
        mp3file = "./assets/" + songdata["title"] + ".mp3"

        size = os.path.getsize(mp3file)
        chunks = math.ceil(size / 8000000)
        

        if chunks == 1:
            await message.channel.send(file=discord.File(mp3file))

        else:
            await self.send(client, message.channel, "*Your mp3 is over 8Mb! It will send in " + str(chunks) + " installments.*")

            os.system("ffmpeg -i \"" + mp3file + "\" -f segment -segment_time " + str(60 * 5.8) + " -c copy \"./assets/" +
                    songdata["title"] + "%03d.mp3\"")

            for x in range(chunks):
                lastcount = await self.send(client, message.channel, "*Sending file " + str(x + 1) + "/" + str(chunks) + "*")

                suffix = str(x)
                while len(suffix) < 3:
                    suffix = "0" + suffix
                
                await message.channel.send(file=discord.File("./assets/" + songdata["title"] + suffix + ".mp3"))
                os.remove("./assets/" + songdata["title"] + suffix + ".mp3")
                await lastcount.delete()


        await self.send(client, message.channel, "***Done! :)***")
        os.remove(mp3file)
            


if __name__ == "__main__":
    command = Com()
    print(command.help())


