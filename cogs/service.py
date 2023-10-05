import discord,json
from discord.ext import commands
from datetime import datetime
# 導入core資料夾中的自寫模組
from core.classes import Cog_Extension

with open("setting/channel.json","r",encoding='UTF-8') as f:
    channel_id = json.load(f)
with open("setting/role.json","r",encoding='UTF-8') as f:
    admin_id = json.load(f)
admin = admin_id.get("admin", [])

# 繼承Cog_Extension的self.bot物件
class Service(Cog_Extension):

    @commands.Cog.listener()
    async def on_interaction(self, interaction: discord.Interaction):
        # interaction.data 是一個包含交互資訊的字典
        # 有些交互不包含 custom_id，需要判斷式處理來防止出錯
        dele= discord.ui.Button(
                label = "✔ 服務完成",
                style = discord.ButtonStyle.green,
                custom_id = "delete"
            )
        try:
            if "custom_id" in interaction.data:
                if interaction.data["custom_id"] == "register":
                    category = discord.utils.get(interaction.guild.categories, id=1155424278410440735)
                    permissions = {
                        interaction.guild.default_role: discord.PermissionOverwrite(read_messages=False),
                        interaction.guild.owner: discord.PermissionOverwrite(read_messages=True),
                        interaction.user: discord.PermissionOverwrite(read_messages=True)
                    }
                    cha = await interaction.guild.create_text_channel(name="申報代碼 "+interaction.user.name,category=category,overwrites=permissions)
                    await interaction.response.send_message(cha.mention + " 已創建", ephemeral=True)
                    view = discord.ui.View()
                    view.add_item(dele)
                    embed=discord.Embed(title="🏫 NASH 校園服務", color=0xea8053,timestamp=datetime.utcnow())
                    embed.add_field(name="目前提供以下服務",value="", inline=False)
                    embed.set_footer(text=cha.guild.name)
                    await cha.send(embed=embed,view=view)
                if interaction.data["custom_id"] == "delete":
                    try:
                        if interaction.user.id in admin:
                            await interaction.channel.delete()
                        else:
                            await interaction.response.send_message("此為管理員專用",ephemeral=True)
                    except Exception as e:
                        print(e)

        except Exception as e:
            print(e)

    @commands.Cog.listener()
    async def on_ready(self):
        # 宣告 View
        try:
            view = discord.ui.View()
            # 使用 class 方式宣告 Button 並設置 custom_id
            register = discord.ui.Button(
                label = "✉ 校園服務",
                style = discord.ButtonStyle.blurple,
                custom_id = "register"
            )
            # 將 Button 添加到 View 中
            view.add_item(register)
            channel = self.bot.get_channel(int(channel_id['School']))
            await channel.purge(check=lambda msg: msg.author == self.bot.user)
            embed=discord.Embed(title="🏫 NASH 校園服務", color=0xea8053,timestamp=datetime.utcnow())
            embed.add_field(name="按下下方按紐尋求校園援助",value="目前提供以下服務\n```1.詢問問題\n2.舉報違規```", inline=False)
            embed.set_footer(text=channel.guild.name)
            await channel.send(embed=embed,view=view)
        except Exception as e:
            print(e)

# 載入cog中
async def setup(bot:commands.Bot):
    await bot.add_cog(Service(bot))