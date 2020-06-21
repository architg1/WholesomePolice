import discord
import praw
from textblob import TextBlob
from discord.ext import commands
import random, datetime
from random import choice
from textblob.classifiers import NaiveBayesClassifier
import nltk


#train = [
#    ('I am tired. Life is hard','neg'),
#    ('I want to kill myself man. I hate this', 'neg'),
#    ("Dude I am tired of life","neg"),
#    ('Somebody kill me lol','neg'),
#    ('I feel sad and can not concentrate in my studies','neg'),
#    ('I find faults in all the people around me and I feel lonely and alone','neg'),
#    ('I’m having a terrible day. Angry at everyone.','neg'),
#    ('No I am not depressed dude','pos'),
#    ('All my friends hate depression','pos'),
#    ("I'm not depressed", "pos"),
#    ("Depression doesn't impact me anymore",'pos'),
#    ("Depression can be hard lol","pos"),
#    ('Story of my life. I struggle with these things daily','pos'),
#    ("I don't want to kill myself",'pos')
#        ]

#cl = NaiveBayesClassifier(train)


random.seed(datetime.datetime.now())
quotes = ['You’re off to great places, today is your day.','You always pass failure on the way to success.','You’re braver than you believe, and stronger than you seem, and smarter than you think.', 'Positive thinking will let you do everything better than negative thinking will.', 'The only time you fail is when you fall down and stay down.','Be mindful. Be grateful. Be positive. Be true. Be kind.', 'You can, you should, and if you’re brave enough to start, you will.','Don’t waste your time in anger, regrets, worries, and grudges. Life is too short to be unhappy.','Believe in yourself. You are braver than you think, more talented than you know, and capable of more than you imagine.','Positive thinking will let you do everything better than negative thinking will.','Believe you can and you’re halfway there.','Happiness is not by chance, but by choice.','You are enough just as you are.','Each of us is more than the worst thing we’ve ever done.','Each of us is more than the worst thing we’ve ever done.','Once you choose hope, anything’s possible','The best is yet to be.','We can change our lives. We can do, have, and be exactly what we wish.','Problems are not stop signs, they are guidelines.','Be thankful for what you have; you’ll end up having more.','In the end, everything will be okay. If it’s not okay, it’s not yet the end.','One small positive thought can change your whole day.','Joy is not in things; it is in us.','Be the light in the dark, be the calm in the storm and be at peace while at war.','Life has no limitations, except the ones you make.']
random_quote = random.choice(quotes)
def random_gen_quotes():
    return random.choice(quotes)

replies = ['Please be kind <3', 'You can do better!', ':(','Is this really your best behaviour?','!!!','Hey! Be respectful :)']
random_reply = random.choice(replies)
def random_gen_replies():
    return random.choice(replies)


bot = commands.Bot(command_prefix='wholesome ')

def feel(content):
    txt = TextBlob(content)
    if txt.sentiment.polarity <= -0.75:
        return 1

#def sad(content):
#    if cl.classify(content) == 'neg':
#        return 1

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.listen()
async def on_message(message):


    if message.author == bot.user:
        return

    if message.content == 'ping':
        await message.channel.send('pong')

    if message.content == 'pong':
        await message.channel.send('ping')

    if message.content == "who's the best?":
        await message.channel.send("you're the best <3")

    if feel(message.content):
        await message.channel.send(random_gen_replies())

    if bot.user in message.mentions:
        await message.channel.send('I love you <3')

    if 'to kms' in message.content.lower():
        await message.channel.send("If you're depressed, please seek professional help <3")

    if 'to kill myself' in message.content.lower():
        await message.channel.send("If you're depressed, please seek professional help <3")

#    if sad(message.content):
#        await message.channel.send("If you're depressed, please seek professional help <3")


@bot.command()
async def quote(ctx):
    await ctx.send(random_gen_quotes())

@bot.command()
async def clear(ctx):

    def delete_feel(message):
        msg = message.content
        txt = TextBlob(msg)
        if txt.sentiment.polarity <= -0.75 and message.author.id == ctx.author.id:
            return 1

    await ctx.channel.purge(limit=1000000, check=delete_feel)
    await ctx.send(f'Cleared your non-wholesome messages {ctx.author} <3')
    await ctx.message.delete()

@bot.command()
async def how(ctx):
    await ctx.send('wholesome quote/news/music/meme/clear')

reddit = praw.Reddit(client_id='YOg0dx8s_H5Zrw',
                     client_secret='Ymr2pJFASux_Vr5CZE73r8sXOAU',
                     user_agent='wholesomepolice (by /u/phastnphurious)')

@bot.command()
async def meme(ctx):
    memes_submissions = reddit.subreddit('wholesomememes').hot()
    post_to_pick = random.randint(1, 50)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)

    await ctx.send(submission.url)

@bot.command()
async def news(ctx):
    news_submissions = reddit.subreddit('UpliftingNews').hot()
    post_to_pick = random.randint(1, 50)
    for i in range(0, post_to_pick):
        submission = next(x for x in news_submissions if not x.stickied)

    await ctx.send(submission.url)

@bot.command()
async def music(ctx):
    song_submissions = reddit.subreddit('music').hot()
    post_to_pick = random.randint(1, 50)
    for i in range(0, post_to_pick):
        submission = next(x for x in song_submissions if not x.stickied)

    await ctx.send(submission.url)


bot.run('-------')
