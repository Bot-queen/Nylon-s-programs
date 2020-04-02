import discord
from discord.ext import commands
import time

a = commands.Bot(command_prefix = "n.")

@a.event
async def on_ready():
    await a.change_presence(status=discord.Status.idle, activity=discord.CustomActivity("Singing in my head"))
    print("Bot has started")

@a.event
async def on_user_join(member):
    print(f"{member} has joined")

@a.event
async def on_user_leave(member):
    print(f"{member} just left")

@a.event
async def command_error(ctx, error):
    await ctx.send("Do it right, idiot!")

@a.command()
async def info(ctx):
    await ctx.send("I am Ny, a discord bot created by a dumbass.")
    time.sleep(0.4)
    await ctx.send("I can do stuff but I probably won't listen to you. Anyways, hi!")

@a.command()
async def greet(ctx, num=5):
    if num > 26:
        await ctx.send("Don't wanna spam")
    else:
        for i in range(0, num):
            await ctx.send("Hello")

@a.command()
async def emoji(ctx):
    await ctx.send(":poop:")

@a.command()
async def copy(ctx, word):
    await ctx.send("**COPIED**")
    await ctx.send(word)

@a.command()
@commands.has_role("Pengu")
async def clear(ctx, amount=1):
    await ctx.channel.purge(limit=amount)
    await ctx.send(amount, "msgs deleted")

@a.command()
@commands.has_role("Pengu")
async def kick(ctx, member : discord.Member, *, reason=None):
    try:
        await member.kick(reason=reason)
        await ctx.send(f"{member.mention} has been kicked")
    except:
        await ctx.send("I won't do it because I can't or I don't want to.")

@a.command()
@commands.has_role("Pengu")
async def ban(ctx, member : discord.Member, *, reason=None):
    try:
        await member.ban(reason=reason)
        await ctx.send(f"{member.mention} has been banned")
    except:
        await ctx.send("I won't do it because I can't or I don't want to.")

@a.command()
@commands.has_role("Pengu")
async def unban(ctx, *, member):
    try:
        bu = await ctx.guild.bans()
        a, b = member.split("#")

        for j in bu:
            u = j
            if (u.x, u.y) == (a, b):
                await ctx.guild.unban(u)
                await ctx.send(f"Unbanned {u.x}#{u.y}")
    except:
        await ctx.send("I won't do it because I can't or I don't want to.")

a.run(TOKEN)
