import discord
from discord.ext import commands
import json,os 
from variable import *

#bot 설정
with open(JSON_FILE_NAME, "r",encoding="utf-8-sig") as json_file:
    user_data=json.load(json_file)
game = discord.Game(f" {PREFIX}명령어 | {len(user_data.keys())}명의 자가진단을 처리함 ")
bot = commands.Bot(command_prefix=PREFIX,activit=game)

#Cogs 수집
for filename in os.listdir('./Cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'Cogs.{filename[:-3]}')

#교1육부는 ㅄ이다

#봇 실행
bot.run(TOKEN)
