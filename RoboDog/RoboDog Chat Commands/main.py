import random
import discord
from discord.ext import commands
import os
from discord import app_commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="/", intents=intents, heartbeat_timeout=60)
TOKEN = os.getenv('TOKEN')

wordarray1 = ["gay", "stupid", 'bitch ass', 'retarded', 'fucking', 'son of a', 'gun hating',  "pathetic", "delusional", "worthless", "dense", "clueless", "gullible", "idiotic", "incompetent", "obtuse", "moronic", 'acoustic', 'autistic']
wordarray2 = ["dickhead", "liberal", "dipshit", "assclown", "nigga", "jew", 'twatwaffle', 'mega', 'cockwomble', 'shitstain', 'douchebag', 'cuntmuffin', 'wankstain', 'moron', 'mega', 'dillweed', 'pissmuppet', 'dingleberry', 'prickleshit', 'doucheburger', 'crapmonger', 'pisspickle', 'buttcrust']

random_word1 = random.choice(wordarray1)
random_word2 = random.choice(wordarray2)


@bot.hybrid_command(name="generateinsult", description="help")
async def help(ctx):
    random_word1 = random.choice(wordarray1)
    random_word2 = random.choice(wordarray2)
    message = (f"you're a {random_word1} {random_word2}!")

    await ctx.send(message)

@bot.hybrid_command(name="ginger", description="help")
async def help(ctx):
    message = (f"I fucking hate gingers. They just look so revoltingly bad every time i see such a color of hair, i flinch. But why, why do they look so bad? That is probably your question right now. I’ll explain that to you. First we start with the horrible light color of their skin. I get that you’re white, but you look like a vampire. Every time the sun shines, it actually bounces off your skin like a mirror. Every time i look at their skin color i get temporatily blinded. The color of the gingers’ skin is so bright it gives off radiation. It’s so unbelievably white that racists start to like the blacks just to become racists to you. Gingers’ skin color is so light that it absorbs all the light from the sun to become the sun themselves. Now that i’m done with their skin color, let’s start with their choice of clothing. Every thing the gingers wear looks like clothing knit by their grandmother. The ugly christmas sweaters look way better than what gingers wear. You could put a piece of GAY FURRY ART on your shirt and it would still manage to look better than what gingers wear. The choice of clothing is probably not as bad as their stupid freckles. Having freckles is fine, but just having red hair already makes having freckles way worse. The freckles stand out so much on their bright skin that it makes it impossible to look away. The freckles are so obvious and gigantic that they look like tumors. The freckles are so dark that the blackest color on earth can never be as dark as the freckles of gingers. I’m done with the freckles, so let’s start with the hair. Gingers’ hair looks so bad that if you even see a red hair laying around, it makes you puke. Their hair is so thin too that you can look through it and see their sculp. Their hair color is so weird that scientists think it’s a new color. No wonder that gingers get bullied.")

    await ctx.send(message)

@bot.hybrid_command(name="degenerate", description="help")
async def help(ctx):
    message = (f"Now, let me tell you something about those wretched degenerates. They're everywhere, infecting this world like a plague. These pathetic creatures with their deviant behaviors and twisted desires, they deserve nothing but our utmost contempt. The degenerates, the furries, the SJWs, the queers, the feminists, they're all just a worthless bunch. They parade around, demanding attention and acceptance, but what they really need is a good old-fashioned reality check. They should be locked away, away from normal society, where they can no longer spread their corruption. Oh, how I long for the days when degeneracy was met with scorn and shame, when society had the backbone to stand up against these abominations. But alas, here we are, drowning in a sea of depravity. So yes, my friend, let's raise our voices and yell it from the rooftops: Degenerates are a blight on humanity, and they must be eradicated!")

    await ctx.send(message)

@bot.hybrid_command(name="femboy", description="help")
async def help(ctx):
    message = (f"Femboys are just sad and depressing. They sit in their rooms all day taking gross, raunchy pics to post on the internet for attention. It's a reflection of how sad and alienated our world has become. Most of them look even more unhealthy then furries. most of them just show their disgusting bulges or nasty ass legs for attention without the fear of repulsing others. Its a very sad day and age when I can't scroll through any social media without seeing those degenerates showing off their testicles without consent. They're just a bunch of scrawny, degenerate, gay ass losers, who can't stop showing off their miserable dresses and penises for attention that they don't get from the people in their lives. The worst part is that people patronize, glamorize and defend this disgusting behaviour by calling it cute, and saying that us normal humans who don't support this, are homophobic, transphobic bigots. And, since they're attention whores, they'll do anything for some gay to compliment them. what a bunch of depressing losers, I really hate them! <:femboy:1184574694926602382> <:shoot:1184571361943900160>")

    await ctx.send(message)

@bot.command(name="mute") #This decorator tells that the mute function is a command the bot should process
@commands.has_permissions(manage_messages=True) #Run the mute command only if the message's author has the permission to manage messages
async def mute(ctx, member: discord.Member, reason=None): #Removed the extra arguments' asterisk (*)
#It's discord.Member, not discord.member
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted") #utils, not Utils
    await member.add_roles(mutedRole, reason=reason)
    await ctx.send(f"Muted {member.mention} for reason {reason}")
    await member.send(f"You were muted in {guild.name} for {reason}")

@bot.command(name="unmute") #This decorator tells that the mute function is a command the bot should process
@commands.has_permissions(manage_messages=True) #Run the mute command only if the message's author has the permission to manage messages
async def unmute(ctx, member: discord.Member): #Removed the extra arguments' asterisk (*)
#It's discord.Member, not discord.member
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted") #utils, not Utils
    await member.remove_roles(mutedRole)
    await ctx.send(f"Unmuted {member.mention}")
    await member.send(f"You were unmuted in {guild.name}")
        
@bot.hybrid_command(name="morocco", description="help")
async def help(ctx):
    message = (f"Oh, for fuck's sake, talking about Moroccan, the gaming genius from the land of dust and camels. This dude thinks he's the Sultan of the joystick, but in reality, he's just a sorry excuse for a gamer. I mean, seriously, Morocco, the land of vibrant culture and historic cities, and this moron is the best they can offer in the gaming department? What a fucking embarrassment. First off, let's talk about his skills – or lack thereof. It's like watching a blindfolded toddler trying to find its way through a maze. I've seen potatoes with more strategic thinking than this numbnut. And don't even get me started on his reflexes; they're slower than a snail on tranquilizers. Maybe he's too busy riding his fucking camel to bother improving. Now, the name – Moroccan. Real creative, buddy. Did your brain freeze in the Sahara heat, or are you just too unimaginative to come up with something remotely interesting? I bet his creativity level is on par with a dead fish. 'Moroccan,' really? Might as well call yourself 'Bland-african' for all the excitement your presence brings. And his online demeanor? Holy shit, it's like dealing with a hormonal teenager who just discovered the internet. Every sentence he types is a painful reminder of why some people should never be allowed near a keyboard. I'd rather listen to nails on a chalkboard than endure his inane chatter. So, Peeps, making fun of Moroccan is like shooting fish in a barrel. The guy is a walking, talking joke. I wouldn't be surprised if he thinks the Casablanca movie is a documentary about his epic gaming journey. Get your shit together, Moroccan, or better yet, stick to something you're good at.. like counting grains of sand in the Sahara.")

    await ctx.send(message)

@bot.event
async def on_ready():
    print ("RoboDog Command module booted!")

bot.run(TOKEN)




