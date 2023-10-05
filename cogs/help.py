import discord,json
from discord import app_commands
from typing import Optional
from discord.app_commands import Choice
from discord.ext import commands
# 導入core資料夾中的自寫模組
from core.classes import Cog_Extension

with open("setting/channel.json","r",encoding='UTF-8') as f:
    chaid = json.load(f)

class Help(Cog_Extension):
    # 教學指令
    @commands.Cog.listener()
    async def on_ready(self):
        channel = self.bot.get_channel(int(chaid['role']))
        await channel.purge(check=lambda msg: msg.author == self.bot.user)
        embed=discord.Embed(title="🏫 NASH 校規", color=0x84e1e0)
        embed.add_field(name="", value="沒太多規則 煩請遵守", inline=False)
        embed.add_field(name="Ⅰ 尊重別人", value="這裡是自由開放環境 但也要尊重別人喔(包括不要騷擾)", inline=False)
        embed.add_field(name="Ⅱ 不要吵架", value="都高中生了 脾氣管理要好意點喔", inline=False)
        embed.add_field(name="Ⅲ 拒絕R18與血腥", value="擦邊球請加暴雷提醒 其餘去陰暗處喔", inline=False)
        embed.add_field(name="Ⅳ 不討論政治", value="除公民系可部分接受外 不要吵政治話題喔", inline=False)
        embed.add_field(name="Ⅴ 不討論宗教", value="學科必要討論外 不要隨意批判宗教", inline=False)
        embed.add_field(name="Ⅵ	尊重作者", value="尊重作者權益 有用就標出來源", inline=False)
        embed.add_field(name="Ⅶ 不要詐騙", value="小心我們撥打165?", inline=False)
        embed.add_field(name="Ⅷ 不要宣傳", value="要宣傳請提前申請 正經的我們都會考慮", inline=False)
        embed.add_field(name="Ⅸ 不要洗頻", value="這裡是聊天區 不是清潔區", inline=False)
        embed.add_field(name="Ⅹ 維護語音秩序", value="勿於公頻大吵/撥放詭譎音樂 私人頻道若忘記上鎖也請勿重複進出他人語音頻道", inline=False)
        embed.add_field(name="Ⅺ 尊重管理員", value="不服聯絡正/副校長不要自己吵起來", inline=False)
        embed.add_field(name="Ⅿ 尊重Discord", value="除以上規則 還是要遵守DC的規則喔\nhttps://discord.com/guidelines", inline=False)
        await channel.send(embed=embed)


# 載入cog中
async def setup(bot):
    await bot.add_cog(Help(bot))