import discord
from discord.ext import commands
import time
from discord.ext.commands import CommandNotFound
from webs import keep_alive
import os
import datetime

#from urllib import parse, request
#import re
import asyncio
import random
global weapons
global debug
global oneup
global autoprotect
global switch
global natalia
autoprotect=True
weapons=False
debug=False
oneup=True
help=True
natalia=True
switch=True
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix=';', description="Mark 3 Shades",help_command=None,intents=intents)

# NON ASYNC DISCORD BOT FUNCTIONS 

#didyoumean 

def dym(text,commands):
  from difflib import SequenceMatcher
  perc=[]
  for i in commands:
   perc.append(SequenceMatcher(None, i, text).ratio())
  return commands[perc.index(max(perc))]
#evaluate a text into math   
def evaluate(text): 
  text=text.replace("^","**")
  text=text.replace("x","*")
  result=eval(text)
  return result


# END OF SECTION

#ASNYC NON DISCORD BOT FUNCTIONS#

async def check1():
 global weapons
 global switch
 while True:
  if switch==True:
  
   weapons=False
   await asyncio.sleep(120) 
  else:
   return
async def performance(channel,start,finish):
  await channel.send(f"Command excecuted in {finish - start} seconds")
#END OF SECTION
@bot.command()
async def warmode(ctx):
  global help
  help=False
  global weapons
  weapons=True
  global debug
  debug=False
  global autoprotect
  autoprotect=True
  global switch
  switch=False
  await ctx.send("Warmode On")
@bot.command()
async def coinflip(ctx):
  x=random.randint(0,1)
  if x==0:
    await ctx.send("Tails")
  else:
     await ctx.send("Heads") 
@bot.command()
async def purge(ctx,number):
 
  messages = await ctx.channel.history().flatten()
 
  for message in messages:
   if(messages.index(message)<=(int(number))):
   
    await message.delete()
@bot.command(name='help', description='Shows this message')
async def help(ctx): 
 global help
 if help: 
  send=""

  for command in bot.commands:
    
    sig =   command.clean_params
    if command.name!="help":
      send+=command.name+" args"+(' '.join( (*sig.keys(),)))+"\n"
  message= await ctx.send(send)
  await message.delete(delay=20)
  
 else:
   await ctx.send("Help Disabled") 
@bot.command(name='weptoggle', description='Toggles weapons.')
async def weptoggle(ctx):
 
  global weapons
  if weapons==True:
    weapons=False
    await ctx.send("Safety On")
    return
   
 
  if weapons==False:
    weapons=True
    await ctx.send("Safety Off")
    return
@bot.command(name='oneupt', description='Toggles oneup')
async def oneupt(ctx):
 
  global oneup
  if oneup==True:
    oneup=False
    await ctx.send("User Protection Off")
    return
   
 
  if oneup==False:
    oneup=True
    await ctx.send("User Protection On")
    return
@bot.command()
async def hackban(ctx,mode,args):
  if mode=="local":
      user = await bot.fetch_user(int(args))
      try:
        await ctx.guild.ban(user,reason="hackban",delete_message_days=0)
      except:
        return
  if mode=="global":
    for guild in bot.guilds:
        user = await bot.fetch_user(int(args))
        try:
          await guild.ban(user,reason="hackban",delete_message_days=0)
        except:
          continue
      
  await ctx.send(user.name+"#"+user.discriminator+" was banned")    
@bot.command()
async def whois(ctx,args):
  if "@" in args.strip(): 
      memid=int(args.replace("<@!"," ").replace(">"," "))
      user = await bot.fetch_user(memid)
  else:   
  
   user = await bot.fetch_user(int(args))
   
  embed=discord.Embed(title="Result",color=discord.Color.blue())
  embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}.png?size=1024".format(user))
  embed.add_field(name="Name", value=str(user.name)+"#"+str(user.discriminator), inline=False)
  embed.add_field(name="Bot", value=user.bot, inline=False)
  embed.add_field(name="Created At ", value=user.created_at, inline=False)
  
  await ctx.send(embed=embed)
  
  

@bot.command()
async def das(ctx,*,memberin:discord.Member):
  danger=False
  for member in ctx.guild.members:
    if member.id==777021127737475094:
      thebot=member
         
    if memberin==ctx.guild.owner:
            danger=True
    if memberin.top_role>thebot.top_role:
              danger=True
        
  
    
 
      
  await ctx.send("Danger= "+str(danger))
   

@bot.command()
async def unrmv(ctx,*,name):
  banlist =  await ctx.guild.bans()
  
  for i in banlist:
    banned =await bot.fetch_user(i.user.id)
    if banned.name==name:
      await ctx.guild.unban(banned)
      await ctx.send(banned.name+"#"+banned.discriminator+" has been unbanned")
    
@bot.command(name='switcht', description='Toggles oneup')
async def switcht(ctx):
 
  global switch
  if switch==True:
    switch=False
    await ctx.send("Auto Switch Off")
    return
   
 
  if switch==False:
    switch=True
    await ctx.send("Auto Switch On")
    return
@bot.command(name='auptog', description='Toggles weapons.')
async def auptog(ctx):
 
  global autoprotect
  if autoprotect==True:
    autoprotect=False
    await ctx.send("Protection Off")
    return
   
 
  if autoprotect==False:
    autoprotect=True
    await ctx.send("Protection On")
    return
@bot.command()
async def destroy(ctx):
  global weapons
  if weapons:
    for channel in ctx.guild.channels:
      await channel.delete()
  else:
    await ctx.send("Safety is Currently Activated")
    
@bot.command(name='kill', description='Pretty self-explanatory.') 
async def kill(ctx, *, member: discord.Member):
  import asyncio
  global weapons
  if weapons:
    
      msg = await ctx.send("Gun systems activating: ")
      await asyncio.sleep(0.1)
      await msg.edit(content='Gun systems activating: ⬜')
      await asyncio.sleep(0.1)
      await msg.edit(content='Gun systems activating: ⬜⬜')
      await asyncio.sleep(0.1)
      await msg.edit(content='Gun systems activating: ⬜⬜⬜')
      await asyncio.sleep(0.1)
      await ctx.send("_Firing machine guns at {0}_".format(member))
  else:
    await ctx.send("Safety is Currently Activated")
@bot.command( name='rmv',description="None") 
async def rmv(ctx,*,member:discord.Member):
  global weapons 
  if weapons:
   await member.ban(reason="rmw")
   await ctx.send(str(member)+"was banned")
  else:
    await ctx.send("Safety is Currently Activated")
 

  
  
   

@bot.command(name='hat', description='hat')
async def hat(ctx):
 
  global help
  if help==True:
    help=False
    
    await ctx.send(help)
    return
   
 
  if help==False:
    help=True
   
    await ctx.send(help)
    return

@bot.command(name='debugt', description='<Insert cmd description here>')
async def debugt(ctx):
 
  global debug
  if debug==True:
    debug=False
    await ctx.send("Debugging Off")
    return
   
 
  if debug==False:
    debug=True
    await ctx.send("Debugging On")
    return  
  

@bot.command(name='bi', description='Info')
async def bi(ctx):
    global help
    global autoprotect
    global oneup
    global weapons
    global switch
    embed=discord.Embed(title="Bot Info Panel ",color=0xab1616 )
    embed.add_field(name="Ping", value=bot.latency, inline=False)
    embed.add_field(name="Weapons Active",value=weapons)
    embed.add_field(name="Debug Active",value=debug)
    embed.add_field(name="Help Active",value=help)
    embed.add_field(name="Auto Off",value=switch)
    embed.add_field(name="User Protection",value=oneup)
    embed.add_field(name="Auto Protection Active",value=autoprotect)
  
   
    await ctx.send(embed=embed)

@bot.command(name='bluep', description='Sends a blueprint.')
async def bluep(ctx,*,args):
 try:
   await ctx.send(file=discord.File("blueprints/"+args+".jpg"))


 except FileNotFoundError:
   await ctx.send("File Not Found")
  
@bot.command(name='arith', description='<Insert description here>')
async def arith(ctx,*,args):
  await ctx.send(evaluate(args))
@bot.command()
async def rrole(ctx,*,role:discord.Role):
  
  
  
 
    o=0
    i=0
    role=role
    for member in ctx.guild.members:
      
       if role in member.roles:
           o+=1
    embed=discord.Embed(title="Role: "+str(role)+" Total Members: "+str(o),color=discord.Color.blue())   
    for member in ctx.guild.members:
       if role in member.roles:
           i+=1
           embed.add_field(name="Member {0}".format(i), value=member.name+"#"+member.discriminator,inline=False)
   
    await ctx.send(embed=embed)
@bot.command()
async def cc(ctx,mode,*,name):
 
 if mode=="a":
   await ctx.guild.create_category(name)
 if mode=="b":
   await ctx.guild.create_voice_channel(name)
 


 if mode=="c":
  await ctx.guild.create_text_channel(name)
 

@bot.command()
async def sinfo(ctx):
  

  
   
  embed = discord.Embed(title=f"{ctx.guild.name}", description="Server Info", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
  
  embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
  embed.add_field(name="Server Owner", value=f"{ctx.guild.owner.name}")
  embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
  embed.add_field(name="Server ID", value=f"{ctx.guild.id}")

  
          
  embed.set_thumbnail(url=ctx.guild.icon_url)
  #embed.set_thumbnail(url=url)

  await ctx.send(embed=embed)

@bot.command(name='error', description='<Insert description here>')
async def error(ctx):
   raise ValueError 

@bot.event
async def on_ready():
    bot.loop.create_task(check1())
    
    user1=await bot.fetch_user(int(os.environ.get("userx")))
    print("Systems Booted")

    await user1.send("Booted Systems ")
@bot.event
async def on_command_error(ctx, error):
 
    if isinstance(error, CommandNotFound):
      if help: 
       cmdnames=[]
       for cmd in bot.commands:
         cmdnames.append(cmd.name)
      
       await ctx.send("Did you mean " +dym(ctx.message.content,cmdnames)+"?")
    else:
      await ctx.send("Exception")
      global debug
      if debug:
       await ctx.send(error)
@bot.command()
async def delete(ctx,*,args):
    guild=ctx.guild
   

      
    for channel in guild.channels:
      
      
      
       channame=channel.name.replace("-"," ").strip()
       
       if (args.strip())==channame:
        await channel.delete()
      
       
      
      
@bot.command()
async def runcode(ctx,*,args):
  outputstr=""
  with open("run.py","w") as python:
    python.write(args.replace("```",""))
    python.close()
  import subprocess
  with open("output.txt", "w+") as output:
    subprocess.call(["python", "run.py"], stdout=output)
    output.close()
  with open("output.txt", "r") as file:
  
    for line in file.readlines():
      outputstr+=line+"\n"
    await ctx.send(outputstr)
    output.close()
  
@bot.event
async def on_guild_join(guild):
    send=""
    user = await bot.fetch_user(int(os.environ.get("userx")))
    await user.send("Shades is now in {0}".format(guild.name))
  
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send('Shades Initiating...')
        break 
@bot.event
async def on_message(message):
  
   global debug
   global autoprotect
   import datetime
   
   userid=os.environ.get("userx")
   user=await bot.fetch_user(userid)
   if autoprotect:
    
     if "aims at" in message.content.lower():
    
      if message.guild!=None:
       
        for member in message.guild.members:
          if member.id==int(userid):
            
            if member.name.lower() in message.content.lower():
              if message.author.id!=int(userid):
               await message.channel.send("_Fires machine guns at {0}_".format(message.author))
              
               await user.send("{0} tried to shoot you at {1} in {2}" .format(message.author,datetime.datetime.now() ,message.guild.name))
            else:
              try: 
                if member.nick.lower() in message.content.lower():
                  if message.author.id!=int(userid):
                   await message.channel.send("_Fires machine guns at {0}_".format(message.author))
                
                   await user.send("{0} tried to shoot you at {1} in {2}" .format(message.author,datetime.datetime.now() ,message.guild.name))
              except:
                print(" o")
  
   
   if message.author.id==int(userid): 
  
      if bot.command_prefix in message.content:
        
          tic= time.perf_counter()
          await bot.process_commands(message)
      
            
          toc=time.perf_counter()
        
          if(debug==True):
           await performance(message.channel,tic,toc)
    
     
keep_alive()

TOKEN=os.environ.get("DISCORD_BOT_SECRET")
bot.run(TOKEN)
