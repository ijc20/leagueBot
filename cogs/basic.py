import discord
from discord.ext import commands
from __main__ import bot

import random
import urllib

class Basic_Commands:

    __author__ = "James"

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='square', description="Squares a number inputted by the user", brief="Squares a number", pass_context=True)
    async def square(self, context, number: int):
        squared_number = (number * number)
        await bot.say("**{number}** squared is **{squared_number}**, {mention}".format(number = number,
                                                                                                squared_number=squared_number,
                                                                                                mention = context.message.author.mention))
        print ("square " + str(squared_number)  + "\n\n")

    @commands.command(name='add', description="Adds two integers together", brief="Adds two numbers", pass_context=True)
    async def do_addition(self, context, first: int, second: int):
        total = first + second
        await bot.say("The sum of **{first}** and **{second}** is **{total}**, {mention}".format(first = first,
                                                                                                 second = second,
                                                                                                 total = total,
                                                                                                 mention = context.message.author.mention))
        print("add " + str(total)  + "\n\n")

    @commands.command(name='clear', description="Clears messages from a channel", brief="Clears messages", pass_context=True)
    async def clear(self, context, number):
        mgs = []
        number = int(number)
        async for x in bot.logs_from(context.message.channel, limit=number):
            mgs.append(x)
        print("clear " + str(number)  + "\n\n")
        await bot.delete_messages(mgs)

def setup(bot):
    bot.add_cog(Basic_Commands(bot))
