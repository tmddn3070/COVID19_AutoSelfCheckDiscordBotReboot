import discord
from discord.ext import commands
import json
import datetime

from variable import *
from embed.help_embed import *


class basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def 명령어(self,ctx):
        global help_embed
        await ctx.send(embed=help_embed)

    @commands.command()
    async def 도움말(self,ctx):
        global help_embed
        await ctx.send(embed=help_embed)

    @commands.command()
    async def 서버목록(self,ctx):
        servers = self.bot.guilds
        await ctx.send(f"현재 {len(servers)}개의 서버에서 실행 중 입니다.")


    @commands.command()
    async def 유저수갱신(self,ctx):
        with open(JSON_FILE_NAME, "r",encoding="utf-8-sig") as json_file:
            user_data=json.load(json_file)
        game = discord.Game(f" {PREFIX}명령어 | {len(user_data.keys())}명의 자가진단을 처리 ")
        await self.bot.change_presence(status=discord.Status.online, activity=game)
        await ctx.send(f"{len(user_data.keys())}명으로 갱신 완료.")

    @commands.command()
    async def Ping(self,ctx):
        await ctx.send(f"pong! `{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}` 기준으로 `{str(round(self.bot.latency*1000))}ms`")
            
    @commands.command()
    async def test(self,ctx):
        await ctx.send("Hello World!")


    
def setup(bot):
    bot.add_cog(basic(bot))