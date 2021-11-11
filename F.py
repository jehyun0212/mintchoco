#run.py
import asyncio, discord
from typing import ContextManager
from dice import *
from discord.ext import commands

import datetime
import pytz




game = discord. Game("F 도움말 입력")
token = ("OTAxNDM4NzgwMTQ4NDE2NTUy.YXP4SQ.g23hV5xeFjy4TKsPnwX265jKlUg")


bot = commands.Bot(command_prefix="F " ,status = discord.Status.online, active = game)

@bot.event
async def on_ready():
    print("다음으로 로그인합니다 : ")
    print(bot.user.name)
    print(bot.user.id)
    print("==========")
    game = discord.Game("F 봇 작동")
    await bot.change_presence(status=discord.Status.online, activity=game)
        
                

@bot.command()
async def 에프봇(ctx):
    await ctx.send("F 봇 입니다. 모르는것이 있으면 F 도움말을 입력해 주세요 ")

@bot.command()
async def 초대(ctx):
    await ctx.send(f'{ctx.message.author.mention}님 F 봇 초대링크: https://discord.com/api/oauth2/authorize?client_id=901438780148416552&permissions=8&scope=bot')

@bot.command()
async def 따라말하기(ctx, *, txt):
    await ctx.send (txt)



@bot.command()
async def 따라해(ctx, *, txt):
    await ctx.send (txt)

@bot.command()
async def Efg(ctx, *, txt):
    await ctx.send (txt)

@bot.command()
async def 주연(ctx):
    await ctx.send("착한 쥬쥬")

@bot.command()
async def 보라(ctx):
    await ctx.send("보라돌이")

@bot.command()
async def 짱구(ctx):
    await ctx.send("존잘")

@bot.command()
async def 시크릿쥬쥬(ctx):
    await ctx.send("주연님은 시크릿 쥬쥬 (아니라고 해도 맞음)")

@bot.command()
async def 도배(ctx):
    await ctx.channel.send("어쩔티비")

@bot.command()
async def 퍼플(ctx):
    await ctx.send("눈맨 나빠")

@bot.command()
async def 녹차(ctx):
    await ctx.send("눈맨 보다 잘났음 ㄲ")

@bot.command()
async def 계발자(ctx):
    await ctx.send(f'{ctx.message.author.mention}님 보다 잘생긴 존잘 짱구')

@bot.command()
async def 개발자(ctx):
    await ctx.send(f'{ctx.message.author.mention}님 보다 잘생긴 존잘 짱구')

@bot.command()
async def 민초(ctx):
    await ctx.send("맛있음")
    await ctx.send("https://img1.daumcdn.net/thumb/R1280x0.fpng/?fname=http://t1.daumcdn.net/brunch/service/user/6yAc/image/vzH4u71GGlPqEMmzeLxfnNWZPZc.png")

@bot.command()
async def 정보(ctx):
    date = datetime.datetime.utcfromtimestamp(((int(ctx.author.id) >> 22) + 1420070400000) / 1000)
    embed = discord.Embed(color=0x00ff00, title = "내 정보")
    embed.add_field(name="닉네임", value='\n', inline=True)
    embed.add_field(name="서버 닉네임", value=ctx.author.display_name, inline=True)
    embed.add_field(name="아이디", value=ctx.author.id, inline=True)
    embed.add_field(name="디스코드 가입일", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일", inline=True)
    embed.set_thumbnail(url=ctx.author.avatar_url)
    await ctx.send(embed=embed)


@bot.command()
async def 그냥나임(ctx):
    await ctx.send("그냥너임")

@bot.command()
async def 핑(ctx):
    embed = discord.Embed(color=0x00ff00, title = "F 봇 현재 핑")
    embed.add_field(name="F 봇의 현재 핑", value='현재의 핑 상테는 {0}초'.format(bot.latency), inline = True)
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/901438780148416552/c668ce80f840e02f0ca7caaf1d3a66a3.png")
    await ctx.send(embed=embed)
    

@bot.command()
async def 눈맨(ctx):
    await ctx.send("𝐽𝑢𝐽𝑢님 노예인 눈사람")

@bot.command()
async def 도움말(ctx):
    await ctx.send("F 주사위는 주사위 게임을 할 수 있습니다, F 따라말하기 <원하는 말>, F 바보 F 봇을 놀리면.... 어마무시한 벌을 받습니다., F 정보 자신의 정보를 나타냅니다., F 핑 현재의 핑을 알 수 있습니다.")

@bot.command()
async def 바보(ctx):
    for j in range(500000):
        await ctx.author.send(f'{ctx.message.author.mention}님도 바보')

#@bot.command()
#async def 청소(message):
    #number = int(message.content.split("")[1])
    #await message.delete()
    #await message.channel.purge(limit=number)
    #await message.channel.send(f"{number}개의 메세지가 삭제되었습니다.")
    #else:
        #await message.delete()
        #await message.channel.send("{}, 당신은 명령어를 사용할 수 있는 권한이 없습니다".format(message.author.mention))


#@bot.event
#async def on_message(message):
    #if message.content.startswith ("F 청소"):
        #if message.author.guild_permissions.administrator:
            #amount = message.content[4:]
            #await message.delete()
            #await message.channel.purge(limit=int(amount))

            #embed = discord.Embed(title="메시지 삭제 알림", description="최근 디스코드 채팅 {}개가\n관리자 {}님의 요청으로 인해 정상 삭제 조치 되었습니다".format(amount, message.author), color=0x000000)
            #embed.set_footer(text="청소", icon_url="https://cdn.discordapp.com/avatars/901438780148416552/c668ce80f840e02f0ca7caaf1d3a66a3.png")
            #await message.channel.send(embed=embed)
        
        

# 
@bot.command()
async def 주사위(ctx):
    result, _color, bot, user = dice()
    embed = discord.Embed(title = "주사위 게임 결과", description = None, color = _color)
    embed.add_field(name = "F 봇의 숫자", value = ":game_die: " + bot, inline = True)
    embed.add_field(name = ctx.author.name+"의 숫자", value = ":game_die: " + user, inline = True)
    embed.set_footer(text="결과: " + result)
    await ctx.send(embed=embed)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("명령어를 찾을 수 없네")

bot.run(token)
