import discord, asyncio, os, platform, sys, youtube_dl
from discord.ext.commands import Bot
from discord.ext import commands
import random

if not os.path.isfile("config.py"):
    sys.exit("'config.py' not found! Please add it and try again.")
else:
    import config

# These setups are came from my old discord bot I created from 2019 ;)


"""
Setup bot intents (events restrictions)
For more information about intents, please go to the following websites:
https://discordpy.readthedocs.io/en/latest/intents.html
https://discordpy.readthedocs.io/en/latest/intents.html#privileged-intents


Default Intents:
intents.messages = True
intents.reactions = True
intents.guilds = True
intents.emojis = True
intents.bans = True
intents.guild_typing = False
intents.typing = False
intents.dm_messages = False
intents.dm_reactions = False
intents.dm_typing = False
intents.guild_messages = True
intents.guild_reactions = True
intents.integrations = True
intents.invites = True
intents.voice_states = False
intents.webhooks = False

Privileged Intents (Needs to be enabled on dev page):
intents.presences = True
intents.members = True
"""

intents = discord.Intents.all()

bot = Bot(command_prefix=config.BOT_PREFIX, intents=intents)

# The code in this even is executed when the bot is ready
@bot.event
async def on_ready():
    bot.loop.create_task(status_task())
    print(f"Logged in as {bot.user.name}")
    print(f"Discord.py API version: {discord.__version__}")
    print(f"Python version: {platform.python_version()}")
    print(f"Running on: {platform.system()} {platform.release()} ({os.name})")
    print("-------------------")

    await bot.change_presence(status=discord.Status.dnd)
# Setup the game status task of the bot
async def status_task():
    while True:
        await bot.change_presence(activity=discord.Game("Minecraft of course!"))
        await asyncio.sleep(3)
        await bot.change_presence(activity=discord.Game("with Cyanide."))
        await asyncio.sleep(3)
        await bot.change_presence(activity=discord.Game("with your mind."))
        await asyncio.sleep(3)
        await bot.change_presence(activity=discord.Game("with humans!"))
        await asyncio.sleep(3)

# Removes the default help command of discord.py to be able to create our custom help command.
bot.remove_command("help")
# yes naa koy custom help command ari ra sa file HAHAHAHAHA

#if __name__ == "__main__":
#    for file in os.listdir("./cogs"):
#        if file.endswith(".py"):
#            extension = file[:-3]
#            try:
#                bot.load_extension(f"cogs.{extension}")
#                print(f"Loaded extension '{extension}'")
#            except Exception as e:
#                exception = f"{type(e).__name__}: {e}"
#                print(f"Failed to load extension {extension}\n{exception}")


## kapoy sig buhat ug commands, bot response lang usah

# The code in this event is executed every time someone sends a message, with or without the prefix
@bot.event
async def on_message(message):
    # Ignores if a command is being executed by a bot or by the bot itself
    if message.author == bot.user or message.author.bot:
        return

    await bot.process_commands(message)

## Bot response working area

    if "idiot" in message.content.lower():
      await message.channel.send("Somebody's calling me?")

## Some Greetings

    if 'appy birthday' in message.content.lower():
        await message.channel.send('Happy Birthday! 🎈🎉')


## Some corny stuffs

    if 'created that bot' in message.content.lower():
        await message.channel.send("I dare not to mention.")

    if 'die' in message.content.lower():
        await message.channel.send("https://media.discordapp.net/attachments/780620475742158889/873401628429021205/828657219091431434.gif")

    if 'dead' in message.content.lower():
        await message.channel.send("https://media.discordapp.net/attachments/780620475742158889/873401628429021205/828657219091431434.gif")

    if 'died' in message.content.lower():
        await message.channel.send("https://media.discordapp.net/attachments/780620475742158889/873401628429021205/828657219091431434.gif")

## Misc keywords
    if 'yes but no' in message.content.lower():
        await message.channel.send("https://tenor.com/view/well-yes-but-actually-no-well-yes-no-yes-yes-no-gif-13736934")

    if 'yuck' in message.content.lower():
        await message.channel.send("EEEEUGHH?!")

##Rickroll or Toss?
    if 'rick' in message.content.lower():
        await message.channel.send("NEVER GONNA GIVE YOU UP! NEVER GONNA LET YOU DOWN!")

    if "yesn't" in message.content.lower():
        await message.channel.send("Yesn't")

    if "be quiet" in message.content.lower():
        await message.channel.send('Okay.')

    if "mom gae" in message.content.lower():
        await message.channel.send('No u, your mom GAAAAAAAAAAAAEEEEEEEEE!')

    if "mom gay" in message.content.lower():
        await message.channel.send('No u, your mom GAAAAAAAAAAAAYYYYYYYYY!')

    if "confused" in message.content.lower():
        await message.channel.send('https://cdn.discordapp.com/emojis/757578189986988132.gif?v=1')

    if 'Rick' in message.content.lower():
        await message.channel.send("NEVER GONNA GIVE YOU UP! NEVER GONNA LET YOU DOWN!")

    if 'rickroll' in message.content.lower():
        await message.channel.send("https://tenor.com/view/rick-ashtley-never-gonna-give-up-rick-roll-gif-4819894")

    if "Rickroll" in message.content.lower():
        await message.channel.send("https://tenor.com/view/rick-ashtley-never-gonna-give-up-rick-roll-gif-4819894")

    if 'toss' in message.content.lower():
        await message.channel.send("https://tenor.com/view/lion-king-toss-bye-gif-4963915")

    if 'Toss' in message.content.lower():
        await message.channel.send("https://tenor.com/view/lion-king-toss-bye-gif-4963915")

    if 'troll' in message.content.lower():
        await message.channel.send("https://cdn.discordapp.com/emojis/827971392670400522.gif?v=1")

    if "test ping" in message.content.lower():
        await message.channel.send(f'{message.author.mention} :ping_pong: | **Pong!** Client Side Ping Latency took {round(bot.latency * 1000)}ms!')

    if "testping" in message.content.lower():
        await message.channel.send(f'{message.author.mention} :ping_pong: | **Pong!** Client Side Ping Latency took {round(bot.latency * 1000)}ms!')

    if "ping test" in message.content.lower():
        await message.channel.send(f'{message.author.mention} :ping_pong: | **Pong!** Client Side Ping Latency took {round(bot.latency * 1000)}ms!')

## Some swearing words and unwanted sentences
# Added some uppercase and lowercase sentences that will trigger to avoid evasion
    if 'fuck' in message.content.lower():
        await message.channel.send("Hold up! :dagger: Calm down dude.")

    if 'FUCK' in message.content.lower():
        await message.channel.send("Hold up! :dagger: Calm down dude.")

    if 'shit' in message.content.lower():
        await message.channel.send("Hold up! :dagger: Calm down dude.")

    if 'SHIT' in message.content.lower():
        await message.channel.send("Hold up! :dagger: Calm down dude.")

    if 'sex' in message.content.lower():
        await message.channel.send("Hold up! :dagger: Calm down dude.")

    if 'crap' in message.content.lower():
        await message.channel.send("Mhmm?")

    if 'bored' in message.content.lower():
        await message.channel.send("https://c.tenor.com/_iJmK8Aic14AAAAM/bored-anime.gif")

    if 'oring' in message.content.lower():
        await message.channel.send("Let's play Rock-Paper-Scissor! Do `!rps` .")



## friendship status

    aa = [
  "I don't know.",
  "I am your friend, just a good friend my man.",
  "I am your mom. Problems?",
  "I am living on the internet and what if I'm a human?",
  "You are my dog.\nWoof woof! :service_dog:",
  "A Minecraft player, anything else?",
  "As a bot, It's really dumb to ask something like that. <:disgust:862897347540811776>",
  "Rage quitter, why not?",
  "The owner of new unclaimed nuclear plant.",
  "Not in a good mood right now. Try ask me again.",
  "Try to ask <@440892659264126997> if she's good or being witty.",
  "Ask your parents.\n<:cheeze:862892425877913600>",
  "The one who stole your heart. <:kekwyou:862893918584176640>",
  "I am your husband. <:KEKW:867620478633377802>",
  "I am <@!420554438206554113>'s adopted rat. Sorry for ping, Dad.",
  "https://tenor.com/view/vegeta-dragonballsuper-dragonball-meme-language-of-gods-gif-14707991",
  "You are my inspiration.",
  "Bruh"
       ]

    if message.content.startswith('<@1195291920814063706>'):
      if message.content.endswith('ho are you?'):
        aa = random.choice(aa)
        await message.channel.send(aa)

    if message.content.startswith('<@1195291920814063706>'):
      if message.content.endswith('ho are you'):
        aa = random.choice(aa)
        await message.channel.send(aa)

    if message.content.startswith('<@1195291920814063706>'):
      if message.content.endswith('ho r u?'):
        aa = random.choice(aa)
        await message.channel.send(aa)

    if message.content.startswith('<@1195291920814063706>'):
      if message.content.endswith('ho r u'):
        aa = random.choice(aa)
        await message.channel.send(aa)


    if message.content.startswith('<@1195291920814063706>'):
      if "hat is" in message.content.lower():
        await message.channel.send("I don't know.")



## you there

    ab = [
      "I'm here, behind you pleb.",
      "In the bathroom, please wait.",
      "Maybe?",
      "I guess you saw me earlier, right?"
      "I don't think so.",
      "I'm about to die."
      ]

    if message.content.startswith('<@1195291920814063706>'):
      if "you there" in message.content.lower():
        ab = random.choice(ab)
        await message.channel.send(ab)

    if message.content.startswith('<@1195291920814063706>'):
      if "u there" in message.content.lower():
        ab = random.choice(ab)
        await message.channel.send(ab)
## doing some things

    ac = [
      "Doing my homework, how about you?",
      "Playing Minecraft. Talk to you later.",
      "Spying your messages.",
      "Calm for a sex.\nI mean, sec. Just a typo silly.",
      "Online class. **AAAAAAAAAAAAAAAAAAAAA** ",
      "Uh nothing. I guess?",
      "Crunching noobs. Anything else?",
      "Bored. I don't know what to do."
      ]

    if message.content.startswith('<@1195291920814063706>'):
      if "u doin" in message.content.lower():
        ac = random.choice(ac)
        await message.channel.send(ac)

## beg lmao
    ad = [
      "RIP, I won't.",
      "Aww what a beggar man.",
      "Son of beggar L",
      "Hats off.",
      "What if I don't?",
      "L nah.",
      "Go ask your mom than me."
      ]

    if message.content.startswith('<@1195291920814063706>'):
      if "gimme" in message.content.lower():
        ad = random.choice(ad)
        await message.channel.send(ad)

    if "give me" in message.content.lower():
        ad = random.choice(ad)
        await message.channel.send(ad)

    if "can I" in message.content.lower():
        ad = random.choice(ad)
        await message.channel.send(ad)

    if "can i" in message.content.lower():
        ad = random.choice(ad)
        await message.channel.send(ad)

    if "ill you" in message.content.lower():
        ad = random.choice(ad)
        await message.channel.send(ad)

    if "ill u" in message.content.lower():
        ad = random.choice(ad)
        await message.channel.send(ad)

    if "may " in message.content.lower():
        ad = random.choice(ad)
        await message.channel.send(ad)

## nou

    ae = [
      "No, you.",
      "Nou.",
      "UNO!",
      "<:nou:871682805686468669>",
      "https://tenor.com/view/confused-what-nigga-please-really-loop-gif-4966361"

      ]

    if message.content.startswith('<@1195291920814063706>'):
      if "nou" in message.content.lower():
        ae = random.choice(ae)
        await message.channel.send(ae)

    if "no, you" in message.content.lower():
        ae = random.choice(ae)
        await message.channel.send(ae)

    if "no, you" in message.content.lower():
        ae = random.choice(ae)
        await message.channel.send(ae)

    if "no u" in message.content.lower():
        ae = random.choice(ae)
        await message.channel.send(ae)

    if message.content.endswith("umb"):
      ae = random.choice(ae)
      await message.channel.send(ae)

## answer meeeee

    af = [
        "What if I don't?",
        "What is it?",
        "Shut down please.\n I mean up.",
        "What do you mean?",
        "Maybe I'm out of words to say. Try again and I'll mark your words."
      ]

    if message.content.startswith('<@1195291920814063706>'):
      if "swer me" in message.content.lower():
        af = random.choice(af)
        await message.channel.send(af)

## why not
    ag = [
        "Why not?",
        "Because yes.",
        "Because no.",
        "¯\_(ツ)_/¯"
      ]

    if message.content.startswith('<@1195291920814063706>'):
       if message.content.endswith('why'):
        ag = random.choice(ag)
        await message.channel.send(ag)

    if message.content.endswith('why?'):
        ag = random.choice(ag)
        await message.channel.send(ag)

## play something

    ah = [
        "Minecraft?",
        "Can't play right now."
      ]

    if message.content.startswith('<@1195291920814063706>'):
        if "lets play" in message.content.lower():
          ah = random.choice(ah)
          await message.channel.send(ah)

        if "let's play" in message.content.lower():
          ah = random.choice(ah)
          await message.channel.send(ah)


## nothing ig
    ai = [
        "Okay.",
        "Impossible. Just tell me what is it.",
        "Why it would be nothing?",
        "*Lies*"
     ]

    if message.content.startswith('<@1195291920814063706>'):
      if "nothing" in message.content.lower():
        ai = random.choice(ai)
        await message.channel.send(ai)

## yes no maybe
    aj = [
        "Alright.",
        "Mhmm?",
        "So what is it?"
      ]

    if message.content.startswith('<@1195291920814063706>'):
      if message.content.endswith("no"):
        aj = random.choice(aj)
        await message.channel.send(aj)

    if "nope" in message.content.lower():
      aj = random.choice(aj)
      await message.channel.send(aj)

    if "maybe" in message.content.lower():
      aj = random.choice(aj)
      await message.channel.send(aj)

    if "date me " in message.content.lower():
      aj = random.choice(aj)
      await message.channel.send(aj)


## heyy

    ak = [
      "f{message.author.mention} yesss?",
      "Yes dear?",
      "Yes hun?"
    ]

    if message.content.startswith('<@1195291920814063706>'):
      if "hey" in message.content.lower():
        ak = random.choice(ak)
        await message.channel.send(ak)

## Commands area, just basic lang usah

# help
@bot.command(name="help")
async def help_command(context):
    """
    List all commands the bot has loaded.
    """
    prefix = config.BOT_PREFIX
    if not isinstance(prefix, str):
        prefix = prefix[0]
    embed = discord.Embed(title="Help", description="List of available commands:", color=config.success)
    for command in bot.commands:
        command_list = [sub_command.name for sub_command in command.commands] if isinstance(command, commands.Group) else [command.name]
        command_description = [sub_command.help for sub_command in command.commands] if isinstance(command, commands.Group) else [command.help]
        help_text = '\n'.join(f'{prefix}{n} - {h}' for n, h in zip(command_list, command_description))
        embed.add_field(name=command.name.capitalize(), value=f'```{help_text}```', inline=False)
    await context.send(embed=embed)



# purge

@bot.command(name="purge")
async def purge(context, number):
    """
    Delete a number of messages.
    """
    if context.message.author.guild_permissions.administrator:
        try:
            number = int(number)
        except ValueError:
            embed = discord.Embed(
                title="Error!",
                description=f"`{number}` is not a valid number.",
                color=config.error
            )
            await context.send(embed=embed)
            return
        if number < 1:
            embed = discord.Embed(
                title="Error!",
                description=f"`{number}` is not a valid number.",
                color=config.error
            )
            await context.send(embed=embed)
            return
        purged_messages = await context.message.channel.purge(limit=number)
        embed = discord.Embed(
            title="Chat Cleared!",
            description=f"**{context.message.author}** cleared **{len(purged_messages)}** messages!",
            color=config.success
        )
        await context.send(embed=embed)
    else:
        embed = discord.Embed(
            title="Error!",
            description="You don't have the permission to use this command.",
            color=config.error
        )
        await context.send(embed=embed)


## info

@bot.command(name="info", aliases=["botinfo"])
async def info_command(context):
    """
    Get some useful (or not) information about the bot.
    """
    embed = discord.Embed(
        description="Silent Bot",
        color=config.success
    )
    embed.set_author(
        name="Bot Information"
    )
    embed.add_field(
        name="Owner:",
        value="kjay23",
        inline=True
    )
    embed.add_field(
        name="Python Version:",
        value=f"{platform.python_version()}",
        inline=True
    )
    embed.add_field(
        name="Prefix:",
        value=f"{config.BOT_PREFIX}",
        inline=False
    )
    embed.set_footer(
        text=f"Version 5.0"
    )
    await context.send(embed=embed)


@bot.command(name="poll")
async def poll_command(context, *args):
    """
    Create a poll where members can vote.
    """
    poll_title = " ".join(args)
    embed = discord.Embed(
        title="A new poll has been created!",
        description=f"{poll_title}",
        color=config.success
    )
    embed.set_footer(
        text=f"Poll created by: {context.message.author} • React to vote!"
    )
    embed_message = await context.send(embed=embed)
    await embed_message.add_reaction("👍")
    await embed_message.add_reaction("👎")
    await embed_message.add_reaction("🤷")

@bot.command(name="8ball")
async def eight_ball_command(context, *args):
    """
    Ask any question to the bot.
    """
    answers = ['It is certain.', 'It is decidedly so.', 'You may rely on it.', 'Without a doubt.',
               'Yes - definitely.', 'As I see, yes.', 'Most likely.', 'Outlook good.', 'Yes.',
               'Signs point to yes.', 'Reply hazy, try again.', 'Ask again later.', 'Better not tell you now.',
               'Cannot predict now.', 'Concentrate and ask again later.', 'Don\'t count on it.', 'My reply is no.',
               'My sources say no.', 'Outlook not so good.', 'Very doubtful.', 'Mhmm idk']
    embed = discord.Embed(
        title="**My Answer:**",
        description=f"{answers[random.randint(0, len(answers))]}",
        color=config.success
    )
    embed.set_footer(
        text=f"Question asked by: {context.message.author}"
    )
    await context.send(embed=embed)


## events ay basta panghitabo ug kanus.a mupansin ang bot
@bot.event
async def on_command_completion(ctx):
    fullCommandName = ctx.command.qualified_name
    split = fullCommandName.split(" ")
    executedCommand = str(split[0])
    print(f"Executed {executedCommand} command in {ctx.guild.name} (ID: {ctx.message.guild.id}) by {ctx.message.author} (ID: {ctx.message.author.id})")

# The code in this event is executed every time a valid commands catches an error
@bot.event
async def on_command_error(context, error):
    if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(
            title="Error!",
            description="This command is on a %.2fs cool down" % error.retry_after,
            color=config.error
        )
        await context.send(embed=embed)
    raise error

# Assuming the token is in the first element of the list
bot.run(config.TOKEN[0])

