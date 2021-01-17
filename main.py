import discord,config,random,seek
from discord.ext import commands

client = commands.Bot(command_prefix='?')
@client.event
async def on_ready():
    game = discord.Game("조상님과 상담중")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.command(aliases=['lotto'])
async def Lotto(ctx,number_of_ticket=1):
    if (number_of_ticket > 0 and number_of_ticket <= 10):
        welcome_msg = "로또번호를 알고 싶나? ㅋㅋ"
        price_msg = f"{number_of_ticket}게임이면 {number_of_ticket * 1000}원이네"
        welcome_msg = welcome_msg + "\n" + price_msg
        for ticket in range(number_of_ticket):
            lotto_num_sample = random.sample(range(1, 46), 6)
            lotto_num_sample.sort()
            lotto_num = str(lotto_num_sample).replace("[", "").replace("]", "")
            welcome_msg = welcome_msg + "\n" + "Game" + str(ticket + 1) + " : " + lotto_num
        await ctx.send(welcome_msg)
    elif (number_of_ticket <= 0):
        await ctx.send("요건 뭐시냥?")
    else:
        await ctx.send("10게임 초과는 ㄴㄴ")

@client.command(aliases=['seek'])
async def Seek(ctx):
    win_num=[]
    for num in seek.win_num:
        win_num.append(num.text)
    win_num=str(win_num).replace("[", "").replace("]", "").replace("'","")
    lotto_result = discord.Embed(title=f"{seek.current_ed} 당첨번호",description="당첨번호 조회결과")
    lotto_result.add_field(name="당첨번호",value=win_num,inline=False)
    lotto_result.add_field(name="보너스번호",value=seek.bonus_num,inline=False)
    await ctx.send(embed=lotto_result)

@client.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.BadArgument):
        await ctx.send("그건 못해유")


client.run(config.tokey_key)


