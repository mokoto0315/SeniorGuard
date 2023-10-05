from datetime import datetime
import discord,json
from discord import app_commands
from discord.ext import commands
from core.classes import Cog_Extension

with open("setting/role.json","r", encoding='UTF-8') as f:
    role = json.load(f)

with open("setting/channel.json","r",encoding='UTF-8') as f:
    chas = json.load(f)


class Record(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self, member):
        cha = self.bot.get_channel(int(chas['record']))
        try:
            embed = discord.Embed(title="🏫 NASH 學生紀錄",description="學生狀態:註冊入學",color=0xb8d8af,timestamp=datetime.utcnow())
            embed.set_thumbnail(url=member.avatar.url)
            embed.add_field(name="學生:", value=member.mention, inline=False)
            embed.set_footer(text=member.guild.name)

            await cha.send(embed=embed)
            # 在這裡為新成員設置基本的身分組
        except Exception as e:
            print(e)
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        cha = self.bot.get_channel(int(chas['record']))
        try:
            embed = discord.Embed(title="🏫 NASH 學生紀錄",description="學生狀態:退學",color=0xe1c3c3,timestamp=datetime.utcnow())
            embed.set_thumbnail(url=member.avatar.url)
            embed.add_field(name="學生:", value=member.mention, inline=True)
            embed.set_footer(text=member.guild.name)
        
            await cha.send(embed=embed)
        except Exception as e:
          print(e)
    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        cha = self.bot.get_channel(int(chas['record']))  # 將 YOUR_CHANNEL_ID 替換成你希望記錄訊息的頻道ID

        try:
            embed = discord.Embed(title="訊息編輯紀錄", description="訊息內容已更新", color=0xdedf9f, timestamp=datetime.utcnow())
            embed.set_thumbnail(url=before.author.avatar.url)
            embed.add_field(name="原訊息內容", value="```" + before.content + "```", inline=False)
            embed.add_field(name="新訊息內容", value="```" + after.content + "```", inline=False)
            embed.set_footer(text=before.guild.name)

            await cha.send(embed=embed)
        except Exception as e:
            print(e)
    @commands.Cog.listener()
    async def on_message_delete(self, message):
 # 將 YOUR_CHANNEL_ID 替換成你希望記錄訊息的頻道ID
        cha = self.bot.get_channel(int(chas['record'])) 
        try:
            embed = discord.Embed(title="訊息刪除紀錄", description="訊息內容已被刪除", color=0xe1c3c3, timestamp=datetime.utcnow())
            embed.set_thumbnail(url=message.author.avatar.url)
            embed.add_field(name="原訊息內容", value="```"+message.content+"```", inline=False)
            embed.set_footer(text=message.guild.name)

            await cha.send(embed=embed)
        except Exception as e:
            print(e)
    @commands.Cog.listener()
    async def on_guild_channel_delete(self,channel):
        cha = self.bot.get_channel(int(chas['record'])) 
        try:
            embed = discord.Embed(title="頻道紀錄", description="頻道已刪除", color=0xe1c3c3, timestamp=datetime.utcnow())
            embed.add_field(name="變更頻道", value="```#" + str(channel) + "```", inline=False)
            embed.set_footer(text=channel.guild.name)

            await cha.send(embed=embed)
        except Exception as e:
            print(e)
    @commands.Cog.listener()
    async def on_guild_channel_create(self,channel):
        cha = self.bot.get_channel(int(chas['record'])) 
        try:
            embed = discord.Embed(title="頻道紀錄", description="頻道已創建", color=0xb8d8af, timestamp=datetime.utcnow())
            embed.add_field(name="變更頻道", value=channel.mention, inline=False)
            embed.set_footer(text=channel.guild.name)

            await cha.send(embed=embed)
        except Exception as e:
            print(e)
    @commands.Cog.listener()
    async def on_guild_channel_update(self, before, after):
        cha = self.bot.get_channel(int(chas['record']))  # 將 YOUR_CHANNEL_ID 替換成你希望記錄訊息的頻道ID

        try:
            embed = discord.Embed(title="頻道紀錄", description="頻道已更新", color=0xdedf9f, timestamp=datetime.utcnow())
            embed.add_field(name="原頻道內容", value="```" + str(before) + "```", inline=False)
            embed.add_field(name="新頻道內容", value="```" + str(after) + "```", inline=False)
            embed.set_footer(text=before.guild.name)

            await cha.send(embed=embed)
        except Exception as e:
            print(e)
    @commands.Cog.listener()
    async def on_error(self,event,args,kwargs):
        cha = self.bot.get_channel(int(chas['record'])) 
        try:
            embed = discord.Embed(title="程式紀錄", description="偵測錯誤", color=0xdedf9f, timestamp=datetime.utcnow())
            embed.add_field(name="錯誤代碼", value="```" + event + "```", inline=False)
            embed.add_field(name="錯誤位置", value=args.mention, inline=False)
            embed.add_field(name="錯誤資料", value="```"+kwargs+"```")
            embed.set_footer(text=event.guild.name)

            await cha.send(embed=embed)
        except Exception as e:
            print(e)
    @commands.Cog.listener()
    async def on_voice_state_update(self,member,before,after):
        cha = self.bot.get_channel(int(chas['record'])) 
        try:
            embed = discord.Embed(title="語音紀錄", description="語音狀態", color=0xdedf9f, timestamp=datetime.utcnow())
            embed.add_field(name="學生", value=member.mention, inline=False)
            embed.add_field(name="離開", value=before, inline=False)
            embed.add_field(name="加入", value=after, inline=False)
            embed.set_footer(text=member.guild.name)

            await cha.send(embed=embed)
        except Exception as e:
            print(e)



async def setup(bot:commands.Bot):
    await bot.add_cog(Record(bot))