import discord
from discord.ext import commands

# Botトークン
load_dotenv() 
# アクセストークンを設定
TOKEN = os.getenv("TOKEN") 

# Botの設定
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.reactions = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Botが起動したとき
@bot.event
async def on_ready():
    print(f'ログイン成功: {bot.user.name}')

# 📌リアクションが追加されたとき
@bot.event
async def on_reaction_add(reaction, user):
    if user.bot:
        return  # Botの操作を無視

    if reaction.emoji == '📌':
        try:
            if not reaction.message.pinned:
                await reaction.message.pin()
                print(f'固定しました: {reaction.message.content}')
        except discord.Forbidden:
            print('固定権限がありません。')
        except discord.HTTPException as e:
            print(f'固定時にエラーが発生しました: {e}')

# 📌リアクションが削除されたとき
@bot.event
async def on_reaction_remove(reaction, user):
    if user.bot:
        return  # Botの操作を無視

    if reaction.emoji == '📌':
        try:
            if reaction.message.pinned:
                await reaction.message.unpin()
                print(f'固定解除しました: {reaction.message.content}')
        except discord.Forbidden:
            print('固定解除の権限がありません。')
        except discord.HTTPException as e:
            print(f'固定解除時にエラーが発生しました: {e}')

# Botの起動
bot.run(TOKEN)
