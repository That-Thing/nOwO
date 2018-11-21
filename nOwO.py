#nOwO
#is made of very strong and good materials.
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

#bot prefix
bot = commands.Bot(command_prefix='n.')

#bot startup message
@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name='Removing OwO', url='https://www.twitch.tv/monstercat',type=1))
    print ("   ▄   ████▄   ▄ ▄   ████▄")
    print ("    █  █   █  █   █  █   █")
    print ("██   █ █   █ █ ▄   █ █   █")
    print ("█ █  █ ▀████ █  █  █ ▀████")
    print ("█  █ █        █ █ █       ")
    print ("█   ██         ▀ ▀         ")

@bot.event 
async def on_message(message):
    if bot.user.id != message.author.id:
        print (message.content.lower)
    if message.author.id == ("204721061411946496"): #exception for me
       pass
    elif message.author.id == ("507974654846304266"): #exception for nOwO
       pass
    elif message.author.id == ("425082463845482506"): #exception for Anti-UwU gun
       pass
    elif message.author.id == ("439205512425504771"): #exception for NotSoBot
       pass
    elif message.author.id == ("172002275412279296"): #exception for Tatsumaki
       pass
    elif message.author.id == ("155149108183695360"): #exception for Dyno Bot
       pass
             
#the magnificent list of banned words
    elif "UwU" in message.content:
        await bot.send_message(message.channel, "__**GET THE HELL OUT OF HERE WITH YOUR GAY UwU's**__")
        await bot.kick(message.author)
        await bot.add_reaction(message, emoji="🖕")
        print ("Another libtard PWNED")
    elif "uwu" in message.content:
        await bot.send_message(message.channel, "__**GET THE HELL OUT OF HERE WITH YOUR GAY UwU's**__")
        await bot.kick(message.author)
        await bot.add_reaction(message, emoji="🖕")
        print ("Another libtard PWNED")
    elif "OwO" in message.content:
        await bot.send_message(message.channel, "__**GET THE HELL OUT OF HERE WITH YOUR GAY OwO's**__")
        await bot.kick(message.author)
        await bot.add_reaction(message, emoji="🖕")
        print ("Another libtard PWNED")
    elif "owo" in message.content:
        await bot.send_message(message.channel, "__**GET THE HELL OUT OF HERE WITH YOUR GAY OwO's**__")
        await bot.kick(message.author)
        await bot.add_reaction(message, emoji="🖕")
        print ("Another libtard PWNED")
    elif "regional_indicator_u regional_indicator_w regional_indicator_u" in message.content:
        await bot.send_message(message.channel, "__**GET THE HELL OUT OF HERE WITH YOUR GAY OwO's**__")
        await bot.kick(message.author)
        await bot.add_reaction(message, emoji="🖕")
        print ("Another libtard PWNED")
    elif "UwO" in message.content:
        await bot.send_message(message.channel, "__**GET THE HELL OUT OF HERE WITH YOUR GAY UwO's**__")
        await bot.kick(message.author)
        await bot.add_reaction(message, emoji="🖕")
        print ("Another libtard PWNED")
    elif "uwo" in message.content:
        await bot.send_message(message.channel, "__**GET THE HELL OUT OF HERE WITH YOUR GAY UwO's**__")
        await bot.kick(message.author)
        await bot.add_reaction(message, emoji="🖕")
        print ("Another libtard PWNED")
    elif "ЦwЦ" in message.content:
        await bot.send_message(message.channel, "__**GET THE HELL OUT OF HERE WITH YOUR GAY ЦwЦ's**__")
        await bot.kick(message.author)
        await bot.add_reaction(message, emoji="🖕")
        print ("Another libtard PWNED")
    elif "ЮwЮ" in message.content:
        await bot.send_message(message.channel, "__**GET THE HELL OUT OF HERE WITH YOUR GAY ЮwЮ's**__")
        await bot.kick(message.author)
        await bot.add_reaction(message, emoji="🖕")
        print ("Another libtard PWNED")
    elif "OHWOH" in message.content:
        await bot.send_message(message.channel, "__**GET THE HELL OUT OF HERE WITH YOUR GAY OHWOH's**__")
        await bot.kick(message.author)
        await bot.add_reaction(message, emoji="🖕")
        print ("Another libtard PWNED")
    elif "$w$" in message.content:
        await bot.send_message(message.channel, "__**GET THE HELL OUT OF HERE WITH YOUR GAY $w$'s**__")
        await bot.kick(message.author)
        await bot.add_reaction(message, emoji="🖕")
        print ("Another libtard PWNED")
    elif "Uwu" in message.content:
        await bot.send_message(message.channel, "__**GET THE HELL OUT OF HERE WITH YOUR GAY UwU's**__")
        await bot.kick(message.author)
        await bot.add_reaction(message, emoji="🖕")
        print ("Another libtard PWNED")
    elif "uwU" in message.content:
        await bot.send_message(message.channel, "__**GET THE HELL OUT OF HERE WITH YOUR GAY UwU's**__")
        await bot.kick(message.author)
        await bot.add_reaction(message, emoji="🖕")
        print ("Another libtard PWNED")
    elif "owO" in message.content:
        await bot.send_message(message.channel, "__**GET THE HELL OUT OF HERE WITH YOUR GAY OwO's**__")
        await bot.kick(message.author)
        await bot.add_reaction(message, emoji="🖕")
        print ("Another libtard PWNED")
    elif "Owo" in message.content:
        await bot.send_message(message.channel, "__**GET THE HELL OUT OF HERE WITH YOUR GAY OwO's**__")
        await bot.kick(message.author)
        await bot.add_reaction(message, emoji="🖕")
        print ("Another libtard PWNED")
    elif "oWo" in message.content:
        await bot.send_message(message.channel, "__**GET THE HELL OUT OF HERE WITH YOUR GAY OwO's**__")
        await bot.kick(message.author)
        await bot.add_reaction(message, emoji="🖕")
        print ("Another libtard PWNED")
    elif "OWO" in message.content:
        await bot.send_message(message.channel, "__**GET THE HELL OUT OF HERE WITH YOUR GAY OwO's**__")
        await bot.kick(message.author)
        await bot.add_reaction(message, emoji="🖕")
        print ("Another libtard PWNED")
    elif "UWU" in message.content:
        await bot.send_message(message.channel, "__**GET THE HELL OUT OF HERE WITH YOUR GAY UwU's**__")
        await bot.kick(message.author)
        await bot.add_reaction(message, emoji="🖕")
        print ("Another libtard PWNED")
    elif "Uwu" in message.content:
        await bot.send_message(message.channel, "__**GET THE HELL OUT OF HERE WITH YOUR GAY UwU's**__")
        await bot.kick(message.author)
        await bot.add_reaction(message, emoji="🖕")
        print ("Another libtard PWNED")
    elif "0w0" in message.content:
        await bot.send_message(message.channel, "__**STOP TRYING TO CHEAT THE SYSTEM**__")
        await bot.kick(message.author)
        await bot.add_reaction(message, emoji="🖕")
        print ("Another libtard PWNED")        
    elif "AwA" in message.content:
        await bot.send_message(message.channel, "__**GET THE HELL OUT OF HERE WITH YOUR GAY AwA's**__")
        await bot.kick(message.author)
        await bot.add_reaction(message, emoji="🖕")
        print ("Another libtard PWNED")
    elif "0wO" in message.content:
        await bot.send_message(message.channel, "__**STOP TRYING TO CHEAT THE SYSTEM**__")
        await bot.kick(message.author)
        await bot.add_reaction(message, emoji="🖕")
        print ("Another libtard PWNED")        
    elif "Ow0" in message.content:
        await bot.send_message(message.channel, "__**STOP TRYING TO CHEAT THE SYSTEM**__")
        await bot.kick(message.author)
        await bot.add_reaction(message, emoji="🖕")
        print ("Another libtard PWNED")
    elif "ow0" in message.content:
        await bot.send_message(message.channel, "__**STOP TRYING TO CHEAT THE SYSTEM**__")
        await bot.kick(message.author)
        await bot.add_reaction(message, emoji="🖕")
        print ("Another libtard PWNED")  
    elif "0wo" in message.content:
        await bot.send_message(message.channel, "__**STOP TRYING TO CHEAT THE SYSTEM**__")
        await bot.kick(message.author)
        await bot.add_reaction(message, emoji="🖕")
        print ("Another libtard PWNED")                      
    elif "OwU" in message.content:
        await bot.send_message(message.channel, "__**GET THE HELL OUT OF HERE WITH YOUR GAY OwU's**__")
        await bot.kick(message.author)
        await bot.add_reaction(message, emoji="🖕")
        print ("Another libtard PWNED")
    elif "owu" in message.content:
        await bot.send_message(message.channel, "__**GET THE HELL OUT OF HERE WITH YOUR GAY OwU's**__")
        await bot.kick(message.author)
        await bot.add_reaction(message, emoji="🖕")
        print ("Another libtard PWNED")
    elif "Owu" in message.content:
        await bot.send_message(message.channel, "__**GET THE HELL OUT OF HERE WITH YOUR GAY OwU's**__")
        await bot.kick(message.author)
        await bot.add_reaction(message, emoji="🖕")
        print ("Another libtard PWNED")
    elif "owU" in message.content:
        await bot.send_message(message.channel, "__**GET THE HELL OUT OF HERE WITH YOUR GAY OwU's**__")
        await bot.kick(message.author)
        await bot.add_reaction(message, emoji="🖕")
        print ("Another libtard PWNED")
    elif "UwO" in message.content:
        await bot.send_message(message.channel, "__**GET THE HELL OUT OF HERE WITH YOUR GAY UwO's**__")
        await bot.kick(message.author)
        await bot.add_reaction(message, emoji="🖕")
        print ("Another libtard PWNED")
    elif "uwO" in message.content:
        await bot.send_message(message.channel, "__**GET THE HELL OUT OF HERE WITH YOUR GAY UwO's**__")
        await bot.kick(message.author)
        await bot.add_reaction(message, emoji="🖕")
        print ("Another libtard PWNED")
    elif "Uwo" in message.content:
        await bot.send_message(message.channel, "__**GET THE HELL OUT OF HERE WITH YOUR GAY UwO's**__")
        await bot.kick(message.author)
        await bot.add_reaction(message, emoji="🖕")
        print ("Another libtard PWNED")
    elif "UWO" in message.content:
        await bot.send_message(message.channel, "__**GET THE HELL OUT OF HERE WITH YOUR GAY UwO's**__")
        await bot.kick(message.author)
        await bot.add_reaction(message, emoji="🖕")
        print ("Another libtard PWNED")
    elif "uwo" in message.content:
        await bot.send_message(message.channel, "__**GET THE HELL OUT OF HERE WITH YOUR GAY UwO's**__")
        await bot.kick(message.author)
        await bot.add_reaction(message, emoji="🖕")
        print ("Another libtard PWNED")
    elif "öwò" in message.content:
        await bot.send_message(message.channel, "__**GET THE HELL OUT OF HERE WITH YOUR GAY OwO's**__")
        await bot.kick(message.author)
        await bot.add_reaction(message, emoji="🖕")
        print ("Another libtard PWNED")
    elif "üwü" in message.content:
        await bot.send_message(message.channel, "__**GET THE HELL OUT OF HERE WITH YOUR GAY UwU's**__")
        await bot.kick(message.author)
        await bot.add_reaction(message, emoji="🖕")
        print ("Another libtard PWNED")
    elif "ОwО" in message.content:
        await bot.send_message(message.channel, "__**GET THE HELL OUT OF HERE WITH YOUR RUSSIAN OwO's**__")
        await bot.kick(message.author)
        await bot.add_reaction(message, emoji="🖕")
        print ("Another libtard PWNED")
    elif "ОwO" in message.content:
        await bot.send_message(message.channel, "__**GET THE HELL OUT OF HERE WITH YOUR RUSSIAN OwO's**__")
        await bot.kick(message.author)
        await bot.add_reaction(message, emoji="🖕")
        print ("Another libtard PWNED")
    elif "Оwo" in message.content:
        await bot.send_message(message.channel, "__**GET THE HELL OUT OF HERE WITH YOUR RUSSIAN OwO's**__")
        await bot.kick(message.author)
        await bot.add_reaction(message, emoji="🖕")
        print ("Another libtard PWNED")
    elif "owO" in message.content:
        await bot.send_message(message.channel, "__**GET THE HELL OUT OF HERE WITH YOUR RUSSIAN OwO's**__")
        await bot.kick(message.author)
        await bot.add_reaction(message, emoji="🖕")
        print ("Another libtard PWNED")
    elif "оwO" in message.content:
        await bot.send_message(message.channel, "__**GET THE HELL OUT OF HERE WITH YOUR RUSSIAN OwO's**__")
        await bot.kick(message.author)
        await bot.add_reaction(message, emoji="🖕")
        print ("Another libtard PWNED")
    elif "оwо" in message.content:
        await bot.send_message(message.channel, "__**GET THE HELL OUT OF HERE WITH YOUR RUSSIAN OwO's**__")
        await bot.kick(message.author)
        await bot.add_reaction(message, emoji="🖕")
        print ("Another libtard PWNED")
    elif "оwO" in message.content:
        await bot.send_message(message.channel, "__**GET THE HELL OUT OF HERE WITH YOUR RUSSIAN OwO's**__")
        await bot.kick(message.author)
        await bot.add_reaction(message, emoji="🖕")
        print ("Another libtard PWNED")
    elif "оWо" in message.content:
        await bot.send_message(message.channel, "__**GET THE HELL OUT OF HERE WITH YOUR RUSSIAN OwO's**__")
        await bot.kick(message.author)
        await bot.add_reaction(message, emoji="🖕")
        print ("Another libtard PWNED")
    elif "öwø" in message.content:
        await bot.send_message(message.channel, "__**GET THE HELL OUT OF HERE WITH YOUR GAY OwO's**__")
        await bot.kick(message.author)
        await bot.add_reaction(message, emoji="🖕")
        print ("Another libtard PWNED")
    elif "öwø" in message.content:
        await bot.send_message(message.channel, "__**GET THE HELL OUT OF HERE WITH YOUR GAY OwO's**__")
        await bot.kick(message.author)
        await bot.add_reaction(message, emoji="🖕")
        print ("Another libtard PWNED")
    elif "()w()" in message.content:
        await bot.send_message(message.channel, "__**GET THE HELL OUT OF HERE WITH YOUR GAY OwO's**__")
        await bot.kick(message.author)
        await bot.add_reaction(message, emoji="🖕")
        print ("Another libtard PWNED")
    elif "OmO" in message.content:
        await bot.send_message(message.channel, "__**GET THE HELL OUT OF HERE WITH YOUR GAY OmO's**__")
        await bot.kick(message.author)
        await bot.add_reaction(message, emoji="🖕")
        print ("Another libtard PWNED")
        await bot.add_reaction(message, emoji="🖕")
        print ("Another libtard PWNED")
    elif "UmU" in message.content:
        await bot.send_message(message.channel, "__**GET THE HELL OUT OF HERE WITH YOUR GAY UmU's**__")
        await bot.kick(message.author)
        await bot.add_reaction(message, emoji="🖕")
        print ("Another libtard PWNED")
    elif "UmO" in message.content:
        await bot.send_message(message.channel, "__**GET THE HELL OUT OF HERE WITH YOUR GAY UmO's**__")
        await bot.kick(message.author)
        await bot.add_reaction(message, emoji="🖕")
        print ("Another libtard PWNED")
    elif "OmU" in message.content:
        await bot.send_message(message.channel, "__**GET THE HELL OUT OF HERE WITH YOUR GAY OmU's**__")
        await bot.kick(message.author)
        await bot.add_reaction(message, emoji="🖕")
        print ("Another libtard PWNED")
    elif "omu" in message.content:
        await bot.send_message(message.channel, "__**GET THE HELL OUT OF HERE WITH YOUR GAY OmU's**__")
        await bot.kick(message.author)
        await bot.add_reaction(message, emoji="🖕")
        print ("Another libtard PWNED")
    elif "umo" in message.content:
        await bot.send_message(message.channel, "__**GET THE HELL OUT OF HERE WITH YOUR GAY UmO's**__")
        await bot.kick(message.author)
        await bot.add_reaction(message, emoji="🖕")
        print ("Another libtard PWNED")
    elif "0ŵО" in message.content:
        await bot.send_message(message.channel, "__**GET THE HELL OUT OF HERE WITH YOUR GAY OwO's**__")
        await bot.kick(message.author)
        await bot.add_reaction(message, emoji="🖕")
        print ("Another libtard PWNED")
    elif "O​wO" in message.content:
        await bot.send_message(message.channel, "__**GET THE HELL OUT OF HERE WITH YOUR GAY OwO's**__")
        await bot.kick(message.author)
        await bot.add_reaction(message, emoji="🖕")
        print ("Another libtard PWNED")












bot.run("NTA3OTc0NjU0ODQ2MzA0MjY2.Dr47Lw.scaF9djFdZPF9ntS9jwuYk4tZvk")
