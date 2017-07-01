import requests
import json
import discord
import re
import binascii
from yandex_translate import YandexTranslate
 
YANDEX = "trnsl.1.1.20170701T203845Z.de5f0b629b564905.c264ca23f085feee439a87d0827e19d4c9c4a3d2"
TOKEN = ""
user = ''
passw = ""
 
translator = YandexTranslate("https://tech.yandex.com/keys/?service=trnsl")
 
client = discord.Client()
 
async def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    array = []
    for words in text.content:
        array.append(words)
    if len(array) > 1:
        bits = bin(int(binascii.hexlify(text.content[12:].encode(encoding, errors)), 16))[2:]
        x = str(bits.zfill(8 * ((len(bits) + 7) // 8)))
        await client.send_message(text.channel,str(x))
    else:
        await client.send_message(text.channel, "Please specify the text you want to convert.")
 
async def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    array = []
    for words in bits.content:
        array.append(words)
    if len(array) > 1:
        n = int(bits.content[12:], 2)
        z = int2bytes(n).decode(encoding, errors)
        await client.send_message(bits.channel,str(z))
    else:
        await client.send_message(bits.channel, "Please specify the binary you want to convert.")
 
def int2bytes(i):
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))
   
def checkforforeignlanguage(message):
    if translator.detect_language(message.content) == "en":
        return False
    elif message.content.startswith('*meme*'):
        return False
    else:
        return True
 
async def translatetoenglish(message, auto):
    if str(message.author) == "SpiceMeme#0261":
        pass
    else:
        array = []
        for words in message.content:
            array.append(words)
 
        if auto == False:
            messag = message.content[10:]
        else:
            messag = message.content
 
        if len(array) > 0:
            data = translator.translate(messag,"en")
            try:
                if messag == data or messag == data.upper() or messag == data.lower():
                    pass
                else:
                    author = message.author
                    await client.send_message(message.channel,str(message.author)+": "+data)
            except:
               client.send_message(message.channel, "Couldn't translate text at this time.")
        else:
            await client.send_message(message.channel, "Please put the words you want to translate.")
 
async def translate(message, lan, leng):
    array = []
    for words in message.content:
        array.append(words)
 
    if len(array) > 1:
        data = translator.translate(message.content[leng:],lan)
        try:
            author = message.author
            await client.send_message(message.channel,str(message.author)+": "+data)
        except:
            client.send_message(message.channel, "Couldn't translate text at this time.")
    else:
        await client.send_message(message.channel, "Please put the words you want to translate.")
       
 
async def mememaker(message, author):
    array = []
    memes = ["onedoesnotsimply", "firstworldproblems","interestingman","ancientaliens","futuramafry", "braceyourselves","noneofmybusiness","badluckbrain","successkid","grumpycat","picard","aintnobody"]
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
                "firstworldproblems":"61539",
                "interestingman":"61532",
                "ancientaliens":"101470",
                "futuramafry":"61520",
                "braceyourselves":"61546",
                "noneofmybusiness":"16464531",
                "badluckbrian":"61585",
                "successkid":"61544",
                "grumpycat":"405658",
                "picard":"1509839",
                "aintnobody":"442575"
            }  
            imgflip = "https://api.imgflip.com/caption_image"
            values = {"template_id":templates[template],
                      "username":user,
                      "password":passw,
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
        if checkforforeignlanguage(message) == False:
                if message.content.startswith('*meme*'):
                        await mememaker(message, author)
                if message.content.startswith('*memehelp*'):
                        await client.send_message(message.channel, "Here is a list of availiable memes:")
                        await client.send_message(message.channel, """```onedoesnotsimply: One Does Not Simply
firstworldproblems: First World Problems
interestingman: The Most Interesting Man in The World
ancientaliens: Ancient Aliens
futuramafry: Not sure if X or X
braceyourselves: Brace Yourselves X is coming
noneofmybusiness: X, but that's none of my business
badluckbrain: Bad Luck Brain
successkid: Success Kid
grumpycat: Grumpy Cat
picard: Picard Facepalm
aintnobody: Ain't nobody got time for that!
```""")
                if message.content.startswith('*lenny*'):
                        await client.delete_message(message)
                        await client.send_message(message.channel, u"( ͡° ͜ʖ ͡°)")
                if message.content.startswith('*spanish*'):
                        await translate(message, "es", 10)
                if message.content.startswith('*german*'):
                        await translate(message, "de", 9)
                if message.content.startswith('*french*'):
                        await translate(message, "fr", 9)
                if message.content.startswith('*korean*'):
                        await translate(message, "ko", 9)
                if message.content.startswith('*chinese*'):
                        await translate(message, "zh-CHT", 10)
                if message.content.startswith('*japanese*'):
                        await translate(message, "ja", 11)
#if message.content.startswith('*english*'):
#    await translatetoenglish(message)
                if message.content.startswith('*texttobin*'):
                        await text_to_bits(message)
                if message.content.startswith('*bintotext*'):
                        await text_from_bits(message)
                if message.content.startswith('*help*'):
                        await client.send_message(message.channel, """```*meme* <template> <top text> <bottom text> - Generates a meme (you need the <>)
*memehelp* - Shows availiable templates
*lenny* - Makes a lenny
*spanish* <text> - Translates from English to Spanish
*french* <text> - Translates from English to French
*german* <text> - Translates from English to German
*korean* <text> - Translates from English to Korean
*chinese* <text> - Translates from English to Chinese
*japanese* <text> - Translates from English to Japanese
Auto-Translate - Automatically translates anything that isn't English
*bintotext* <binary> - Converts binary to text
*texttobin* <text> - Converts text to binary
*help* - Shows this.
```""")
        elif checkforforeignlanguage(message) == True:
                await translatetoenglish(message, True)
       
       
 
client.run(TOKEN)
