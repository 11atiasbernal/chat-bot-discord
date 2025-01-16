import discord
import random
from app import gen_pass
from discord.ext import commands


#configuración del bot
intenciones=discord.Intents.default()
intenciones.message_content=True

bot=commands.Bot(command_prefix="/",intents=intenciones)


@bot.command()
async def hola(ctx):
    await ctx.send(f"hola como estas {ctx.author.name}")

@bot.command()
async def gener(ctx):
    await ctx.send(f"esta es tu contraseña: {gen_pass}")

@bot.command()
async def admin(ctx):
    await ctx.send("hola admin que gusto tenerte de vuelta en el server😊")

@bot.command()
async def b(ctx):
    await ctx.send("hoy es día de pizza a drisfrutar 🍕😋")

@bot.event
async def on_ready():
    print("EL BOT ESTA EN LINEA")
    
bot.run("TOKEN OF YOUR BOT")
