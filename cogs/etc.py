import discord,json
from datetime import datetime
from discord.ext import commands

# 導入core資料夾中的自寫模組
from core.classes import Cog_Extension

with open("setting/role.json","r", encoding='UTF-8') as f:
    role_list = json.load(f)

with open("setting/message.json","r", encoding='UTF-8') as f:
    msg = json.load(f)

with open("setting/channel.json","r",encoding='UTF-8') as f:
    channel_dict = json.load(f)


class ETC(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel_id = channel_dict['Welcome'][str(member.guild.id)]
        channel = self.bot.get_channel(int(channel_id))
        embed=discord.Embed(title="🏫 NASH 校園管理", color=0xb8d8af,timestamp=datetime.utcnow())
        embed.set_thumbnail(url=member.avatar.url)
        embed.add_field(name="成員", value=member.mention, inline=False)
        embed.add_field(name="歡迎", value="歡迎你的加入 看完規則就去註冊囉 \n 目前還在收尾階段 如果有BUG或建議歡迎提出", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/1155447235794976868/1157597538703134780/1.png?ex=65193038&is=6517deb8&hm=623b1b12fdb4e257a52316d32e552988e30aef148dfee3589a0d9c56a45bc3c0&")
        embed.set_footer(text=member.guild.name)
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel_id = channel_dict['Leave'][str(member.guild.id)]
        channel = self.bot.get_channel(int(channel_id))
        try:
            embed=discord.Embed(title="🏫 NASH 校園管理", color=0xea8053,timestamp=datetime.utcnow())
            embed.set_thumbnail(url=member.avatar.url)
            embed.add_field(name="成員", value=member.mention, inline=False)
            embed.add_field(name="離開", value="再見 有緣再會吧", inline=False)
            embed.set_image(url="https://cdn.discordapp.com/attachments/1155447235794976868/1157597538313056296/2.png?ex=65193038&is=6517deb8&hm=a9fb289b68c9fcf6d77ddf1e1ab4d5ee3ccfe7d924e927078f3841470168569f&")
            embed.set_footer(text=member.guild.name)
            await channel.send(embed=embed)
        except Exception as e:
            print(e)


# 載入cog中
async def setup(bot):
    await bot.add_cog(ETC(bot))
