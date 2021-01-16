import discord,config
from discord.ext import commands

app = commands.Bot(command_prefix='?')
class chatbot(discord.Client):
    async def on_ready(self):
        game = discord.Game("조상님 접선중")
        await client.change_presence(status=discord.Status.online, activity=game)

    async def on_message(self, message):
        if message.author.bot:
            return None
        if message.content == "?Lotto":
            channel = message.channel
            msg = "로또번호를 알고 싶나?"
            await channel.send(msg)
            return None


# 프로그램이 실행되면 제일 처음으로 실행되는 함수
if __name__ == "__main__":
    client = chatbot()
    client.run(config.tokey_key)

