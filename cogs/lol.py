import discord
from discord.ext import commands
from __main__ import bot
from riotwatcher import RiotWatcher
import json
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

#APIKey = config.get('RIOT_API', 'ApiKey')
APIKey = 'RGAPI-701535ae-6431-4525-bf17-70c9114d38a1'
watcher = RiotWatcher(APIKey)

with open('champion_data.txt') as json_file:
    data = json.load(json_file)

class League_Commands:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='lol.getinfo', decription="Gets information about a summoner", brief="Gets summoner info", pass_context=True)
    async def get_info(self, context, region, summonerName):
        summoner = watcher.summoner.by_name(region.lower() + '1', summonerName)
        print(summoner)
        await bot.say("{name}(ID: {id}) is a level {level} summoner playing on {region}, {mention}".format(name=summoner['name'],
                                                                                                            id=summoner['id'],
                                                                                                            level=summoner['summonerLevel'],
                                                                                                            region=region,
                                                                                                            mention=context.message.author.mention))
        print("League Get Info " + str(summoner['name']) + "\n\n")

    @commands.command(name='lol.getrank', decription="Gets ranked info about a summoner", brief="Gets ranked info", pass_context=True)
    async def get_rank(self, context, region, summonerName):
        summoner = watcher.summoner.by_name(region.lower() + '1', summonerName)
        print(summoner)
        rank_info = watcher.league.by_summoner(region.lower() + '1', summoner['id'])
        print(rank_info)
        queue = 0
        if len(rank_info) == 1:
            queue = 0
        elif rank_info[0]['queueType'] == 'RANKED_SOLO_5x5':
            queue = 0
        elif rank_info[1]['queueType'] == 'RANKED_SOLO_5x5':
            queue = 1
        elif len(ranked_info) == 3:
            queue = 2
        else:
            if rank_info[0]['queueType'] == 'RANKED_FLEX_SR':
                queue = 0
            else:
                queue = 1

        queueType = rank_info[queue]['queueType']
        if queueType == 'RANKED_SOLO_5x5':
            queueType = 'Solo/Duo'
        elif queueType == 'RANKED_FLEX_SR':
            queueType = 'Flex'
        else:
            queueType = 'Twisted Treeline'

        await bot.say("{name} is in {tier} {div}, and has {lp} LP in {type}, {mention}".format(name=summoner['name'], tier=rank_info[queue]['tier'], div=rank_info[queue]['rank'], lp=rank_info[queue]['leaguePoints'], type=queueType, mention=context.message.author.mention))
        print("League Get Rank " + str(summoner['name'])  + "\n\n")


    @commands.command(name='lol.getmastery', desciption="Gets mastery level and points for a champion", brief="Gets mastery", pass_context=True)
    async def get_mastery(self, context, region, summonerName, champion):
        summoner = watcher.summoner.by_name(region.lower() + '1', summonerName)
        print(summoner)
        print(data)
        champ = data['data']['{champion}'.format(champion=champion)]
        print(champ)
        champ_ID = champ['id']
        champ_mastery = watcher.champion_mastery.by_summoner_by_champion(region.lower() + '1', summoner['id'], champ_ID)
        print(champ_mastery)
        await bot.say("{name} is mastery {lvl} on {champ} and has {points} champion points, {mention}".format(name=summoner['name'],
                                                                                                                                                                                    lvl=champ_mastery['championLevel'],
                                                                                                                                                                                    champ=champ['name'],
                                                                                                                                                                                    points=champ_mastery['championPoints'],
                                                                                                                                                                                    mention=context.message.author.mention))
        print("League Get Mastery " + str(summoner['name']) + " " + str(champ['name']) + "\n\n")

def setup(bot):
    bot.add_cog(League_Commands(bot))
