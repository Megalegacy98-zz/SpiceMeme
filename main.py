import requests
import json
import discord
import re

client = discord.Client()

async def mememaker(message, author):
    array = []
    memes = ["onedoesnotsimply", "batmanrobin","interestingman","ancientaliens","futuramafry"]
    text = re.findall(r'<(.*?)>', message.content)
    for eachTitle in text:
        array.append(eachTitle)

    if len(array) < 3:
        await client.send_message(message.channel, "You are missing an argument! It is supposed to be '*meme* <template> <top text> <bottom text>' WITH the <>. Use *memehelp* to see availiable templates.")
    else:
        x = 0
        for meme in memes:
            if array[0] == meme:
                x += 1
        if x > 0:
            template = array[0]
            text0 = array[1]
            text1 = array[2]
            templates = {
                "onedoesnotsimply":"61579",
                "batmanrobin":"438680",
                "interestingman":"61532",
                "ancientaliens":"101470",
                "futuramafry":"61520"
            }  
            imgflip = "https://api.imgflip.com/caption_image"
            values = {"template_id":templates[template],
                      "username":"insert user here",
                      "password":"put password here",
                      "text0":text0,
                      "text1":text1}
            headers = {}
            headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'

            req = requests.get(url=imgflip, params=values, headers=headers)
            data = json.loads(req.text)
            await client.send_message(message.channel, data['data']['url'] + " made by " + "@" + str(author))
            
        else:
            await client.send_message(message.channel, "That's not a template! Use *memehelp* to see availiable templates.")

      
        

@client.event
async def on_message(message):
    author = message.author
    if message.content.startswith('*meme*'):
        await mememaker(message, author)
    if message.content.startswith('*memehelp*'):
        await client.send_message(message.channel, "Here is a list of availiable memes:")
        await client.send_message(message.channel, """```onedoesnotsimply: One Does Not Simply
batmanrobin: Batman Slapping Robin
interestingman: The Most Interesting Man in The World
ancientaliens: Ancient Aliens
futuramafry: Not sure if X or X```""")
    if message.content.startswith('*lenny*'):
        await client.delete_message(message)
        await client.send_message(message.channel, u"( ͡° ͜ʖ ͡°)")

client.run('put token here')
