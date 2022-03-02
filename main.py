import os
import discord
import requests
import json
import random
from discord.ext import commands
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix = '+', intents=intents)
client.remove_command('help')

rcv = ["bye chicko"]

reply = ["Bye"]

ask_chicko = ["How are you?","how are you?","how are you","how are u","How about you?","how about you?","how about you","how about u","how bout you","how bout u?","how bout u","How bout u?"]

reply_chicko = ["I'm fine. :relaxed: thank you for asking."]

normal_rcv = ["i'm fine","im okay","i'm okay","boleh ah","boleh lah","i'm good","i'm Good","I'm okay","I'm fine"]

normal_reply = ["It's good to know that, but remember to smile always. :innocent:"," I see, i hope your day gets better. :relieved:","Alhamdulillah. :innocent:","Good to hear that :hugging:","Narukodo! :thinking:","Ouh, I see :hugging:"]

happy_words = ["happy","delighted","best","seronok"]

happy_reply = ["That's a very good news :innocent:","Its really good to know that :innocent:","Nice! :star_struck:","I'm happy because you are happy :relaxed:","That's so wonderful :star_struck:","Wow, I am happy to hear that. :star_struck:","Good, I hope your day keeps on getting better. :relaxed:","Alhamdulillah. :innocent:"]

sad_words = ["i'm sad", "aku sedih", "i'm depress", "unhappy", "aku kecewa", "i'm angry", "i'm miserable", "i'm useless", "i feel not so okay","i'm not good"," i'm bad","i'm not okay","i'm stress"]

thanks_rcv = ["Tq", "thanks", "trimas", "terima kasih", "thank you", "kamsahamnida", "gomawo","tq"]

thanks_reply = ["You're welcome :innocent:", "I'm always here to help :relieved:", "Sama-sama :relieved:", "No problemo :ok_hand:"]

starter_encourange = ["Hang in there, I know you can do it. :muscle:", "Don't be sad :pleading_face:, I'm here with you", "Don't worry, everything will be fine :hugging:","Don't worry, You got this! :muscle:","I hope you don't feel alone as you go through this time. My thoughts and prayers are with you all the way. :hugging:","I know it's hard but I am rooting for you every minute of everyday. :hugging:","Jangan berputus asa! :hugging:","Don't stop believe in yourself :punch:"]

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)  

def get_joke():
    response = requests.get("https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,racist&type=single")
    json_data = json.loads(response.text)
    joke = json_data["joke"]
    return (joke)
    
@client.event
async def on_ready():
  print('we have logged in as {0.user}'.format(client))

@client.command(name = 'hai')
async def hai(ctx):
  await ctx.send("Hello, I am you")

@client.command(name = 'meme')
async def meme(ctx):
  content = requests.get("https://meme-api.herokuapp.com/gimme")
  data = json.loads(content.text)
  meme = discord.Embed(title=f"{data['title']}", Color = discord.Color.random()).set_image(url=f"{data['url']}")
  await ctx.reply(embed=meme)


@client.command(name = 'join')
async def join(ctx):
  if(ctx.author.voice):
    channel = ctx.message.author.voice.channel
    await channel.connect()
  else:
    await ctx.send("You are not in the voice channel")

@client.command(name = 'leave')
async def leave(ctx):
  if (ctx.voice_client):
    await ctx.guild.voice_client.disconnect()
    await ctx.send("I have left the voice channel")
  else:
    await ctx.send("I am not in any voice channel")

@client.command(pass_context = True)
async def help(ctx):
    author = ctx.message.author
    embed = discord.Embed(colour = discord.Colour.blue()
    )
    embed.set_author(name = 'Hey I am Chicko!',url = 'https://emojipedia.org/hatching-chick/',icon_url = 'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/twitter/282/hatching-chick_1f423.png')
    embed.set_footer(text = 'I hope we can get along well.')
    embed.add_field(name = ':question: Help commands :question:', value = 'Here is the list of my commands:', inline=False)
    embed.add_field(name='+hello',value='Say Hello to me :wave: :hatched_chick:', inline=False)
    embed.add_field(name='+inspire',value='I will inspire you with my quotes :sparkles:', inline=False)
    embed.add_field(name='+joke',value='I will try my best to make you laugh with my jokes :joy:', inline=False)
    embed.add_field(name='+meme',value='I will get you some fresh new memes :fire:', inline=False)
    embed.add_field(name='Extra',value='I will also monitor most of the events taking place in the server and notify all of you about what is going on. For example when a person joined a channel i will let you guys know. And I can also react to some of your conversation, so you can talk to me. ', inline=False)

    
    await ctx.send("Thank you for using help command. %s"%author.name,embed = embed)

@client.event
async def on_member_join(member):
  channel = client.get_channel(913116093437079552)
  await channel.send('Hello! welcome to our discord server %s :heart_eyes:. How are you?' %member.name)
  
@client.event
async def on_member_remove(member):
  channel = client.get_channel(913116093437079552)
  await channel.send('It is sad to part ways with %s :pensive:,but i guess every good things come to an end' %member.name)

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('+hello'):
    name = message.author.name
    await message.channel.send('Hello %s! how are you?' %(name))

  if msg.startswith('+inspire'):
    quote = get_quote()
    await message.channel.send(quote)

  if msg.startswith('+joke'):
    joke = get_joke()
    await message.channel.send(joke)

  if any(word in msg for word in sad_words):
    name = message.author.name
    await message.channel.send(random.choice(starter_encourange)+" %s"%(name))

  if any(word in msg for word in thanks_rcv):
    name = message.author.name
    await message.channel.send(random.choice(thanks_reply)+" %s"%(name))

  if any(word in msg for word in normal_rcv):
    name = message.author.name
    await message.channel.send(random.choice(normal_reply)+" %s"%(name))

  if any(word in msg for word in rcv):
    name = message.author.name
    await message.channel.send(random.choice(reply)+" %s"%(name))

  if any(word in msg for word in happy_words):
    name = message.author.name
    await message.channel.send(random.choice(happy_reply)+" %s"%(name))

  if any(word in msg for word in ask_chicko):
    name = message.author.name
    await message.channel.send(random.choice(reply_chicko))

  #process commands
  await client.process_commands(message)

my_secret = os.environ['TOKEN']
keep_alive()
client.run(my_secret)
