import discord
import random
import time
import os
import schedule
import pandas as pd
from threading import Thread
from keep_alive import keep_alive

intents=discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)

stickerNumber = pd.read_excel(r"Stickers/0-sticker-to-number.xlsx")
titles = stickerNumber.Titles
smites = [["Ceaseless Watcher!", "See this lie, this golden strand of falsehood", "Take it in your gaze and pull it, follow through its curves and twists and knots as it unravels all before you", " Unweave it now, its fear and its falsehood, its hidden teeth and the ones it wears so proudly", "Take all that it is and all that it has", "It", "Is", "Yours"],
["Ceaseless Watcher!", "Turn your gaze upon this wretched thing"], ["Ceaseless Watcher!", "Turn your gaze upon this thing and drink", "Your", "Fill"], 
["Ceaseless Watcher!", "Gaze upon this thing, this lost and broken splinter of fear", "Take what is left of it as your own and leave no trace of it behind", "It", "Is", "Yours"]
]
SWEARSMAX = 10
jurgens = {}

def countFolder(commandFolder):
   dir_path = fr'{commandFolder}'
   count = 0
   for path in os.listdir(dir_path):
      if os.path.isfile(os.path.join(dir_path, path)):
         count += 1
   return count

def schedule_checker():
    while True:
        schedule.run_pending()
        time.sleep(1)

def emptyJurgens():
    global jurgens
    jurgens = {}

def checkSticker(message):
    message = message[1:]
    stickerNum = 1
    for title in titles:
        for word in message.split():
            if len(word)>3 and word.upper() in title.split():
                return stickerNum
        stickerNum += 1
    return stickerNum

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.author.id not in jurgens:
        jurgens[message.author.id] = [0]
    
    if str(message.type) == "MessageType.new_member":
        await message.channel.send(f"{message.author.name}, you're welcome to the Magnus Institute")
        statementBegins = open(r"Stickers/15.webp", "rb")
        #archivist.send_chat_action(message.chat.id, "typing")
        time.sleep(1)
        await message.channel.send("The name in Jonathan Sims")
        #archivist.send_chat_action(message.chat.id, "typing")
        time.sleep(2)
        await message.channel.send("Head Archivist of the Magnus Institute")
        #archivist.send_chat_action(message.chat.id, "typing")
        time.sleep(2)
        await message.channel.send("London")
        #archivist.send_chat_action(message.chat.id, "typing")
        time.sleep(2)
        await message.channel.send(file=discord.File(statementBegins))
        return

    if message.content.startswith('/greet'):
        statementBegins = open(r"Stickers/15.webp", "rb")
        #archivist.send_chat_action(message.chat.id, "typing")
        time.sleep(1)
        await message.channel.send("The name in Jonathan Sims")
        #archivist.send_chat_action(message.chat.id, "typing")
        time.sleep(2)
        await message.channel.send("Head Archivist of the Magnus Institute")
        #archivist.send_chat_action(message.chat.id, "typing")
        time.sleep(2)
        await message.channel.send("London")
        #archivist.send_chat_action(message.chat.id, "typing")
        time.sleep(2)
        await message.channel.send(file=discord.File(statementBegins))
        return
    
    if message.content == "/sticker":
        randomNum = random.randint(1, len(titles))
        sticker = open(rf"Stickers/{randomNum}.webp", "rb")
        await message.channel.send(file = discord.File(sticker))
        sticker.close()
        return

    if message.content == "/fandom":
        randomNum = random.randint(1, countFolder("Fandompics"))
        fandomPic = open(rf"Fandompics/{randomNum}.jpg", "rb")
        await message.channel.send(file = discord.File(fandomPic))
        fandomPic.close()
        return

    if message.content == "/lies":
        await message.channel.send(smites[0][0])
        for i in range(1, len(smites[0])):
            if smites[0][i] == "It" or smites[0][i] == "Is" or smites[0][i] == "Yours":
                #archivist.send_chat_action(message.chat.id, "typing")
                time.sleep(1)
                await message.channel.send(smites[0][i])
            else: 
                #archivist.send_chat_action(message.chat.id, "typing")
                time.sleep(2)
                await message.channel.send(smites[0][i])

    if message.content == "/help":
        helpMessage = open(r"Utilities/help.txt", "r")
        await message.channel.send(helpMessage.read())
        helpMessage.close()

    if message.content.startswith("/"):
        stickerNum = checkSticker(message.content)
        if stickerNum <= countFolder(r"Stickers")-1:
            sticker = open(fr"Stickers/{stickerNum}.webp", "rb")
            await message.channel.send(file = discord.File(sticker))
            sticker.close()

    swearsFile = open("swears.txt", "r")
    swears = (swearsFile.read()).split("\n")
    swearsFile.close()
    for word in message.content.split():
        for swear in swears:    
            if word.lower() == swear or (len(word) > len(swear) and swear in word.lower()):
                jurgens[message.author.id][0] += 1
                if jurgens[message.author.id][0] == SWEARSMAX:
                    await message.author.edit(nick = "Jurgen Leitner")
                    await message.reply("JURGEN LEITNER?")
                    time.sleep(1)
                    await message.channel.send("STUPID IDIOT MOTHERFUCKING JURGEIN LEITNER GOD DAMN FOOL BOOK COLLECTING DUST EATING RAT OLD BASTARD SHITHEAD IDIOT AVATAR OF THE WHORE BIGGEST CLOWN IN THE CIRCUS LAUGHED OUT OF TOWN COWBOY MOTHERFUCKING JURGEIN LEITNER")
                    time.sleep(1)
                    await message.channel.send("STOP PINNING ME WHEN I TALK ABOUT JURGEIN LEITENER I HATE HIM SO MUCH WHY DOES HE HAVE SO MANY FUCKED UP BOOKS WHY DID HE DECIDE TO FUCK AROUND AND FIND OUT JUST SET THEM LOOSE IS HE DEAD IS HE A BASTARD MAN HAS SUCH A VISCERAL AFFECT ON ME NOT EVEN IN THE ROOM NEVER SEEN THIS MANS FACE AND I KNOW HE HAS THE WORLDS SHITTIEST BEARD GET AWAY FROM ME")
                    time.sleep(1)
                    await message.channel.send("if i wanted to get into heaven and god said jurgein leitner's waiting inside i would piss on gods feet for the sole purpose of getting sent back down")
                    time.sleep(1)
                    await message.channel.send("if i have to deal with jurgein leitner speaking one word in person on voice in podcast not only will i close the tab i will delete my bookmark out of spite and have to rewatch the entire series again for the experience of being able to skip all the times when he is mentioned or alive")
                    time.sleep(1)
                    await message.channel.send("i dont even know why i hate him so much. he collects books but i am just mad because i am angy")
                    time.sleep(1)
                    await message.channel.send("he better have some fucked up backstory to explain this if hes just some rich shithead whos a fan of creepypasta and wanted the irl version ill go ham")
                    time.sleep(1)
                    await message.channel.send("BETTER have had a book make him kill a man cuz if he didnt Im going to make him")
                    time.sleep(1)
                    await message.channel.send("paypal.com/IFuckingHateJurgeinLeitner")
                    time.sleep(1)
                    await message.channel.send("episodes not even about him. vaguely mentioned what is supposed to maybe be his library and I lost it")
                    time.sleep(1)
                    await message.channel.send("where the fuck is jurgein leitner if hes still alive im going to so deeply wish he wasnt")
                    time.sleep(1)
                    await message.channel.send("crusty old man")
                    time.sleep(1)
                    await message.channel.send("ill punch leitner and his sad frail old man twig bones will simply flake apart under my epic huge meat fist and he will disintegrate until all thats left is one final book he kept on him at all times simply titled Now You Fucked Up in ancient yiddish")
                    time.sleep(1)
                    await message.channel.send("im not breathing im hyperventilating at this point")
                    time.sleep(1)
                    await message.channel.send("i hope theres a date given for when jurgen died or will die so i can make it a reminder on my phone")
                    time.sleep(1)
                    await message.channel.send("everyday once a year i will see it and do anything but pay respects to the man who had so many fucked up if true books")
                    jurgens[message.author.id][0] = 0
                else:
                    randomNum = random.randint(0, len(smites)-1)
                    #archivist.send_chat_action(message.chat.id, "typing")
                    await message.reply(smites[randomNum][0])
                    for i in range(1, len(smites[randomNum])):
                        if smites[randomNum][i] == "It" or smites[randomNum][i] == "Is" or smites[randomNum][i] == "Yours":
                            #archivist.send_chat_action(message.chat.id, "typing")
                            time.sleep(1)
                            await message.channel.send(smites[randomNum][i])
                        else: 
                            #archivist.send_chat_action(message.chat.id, "typing")
                            time.sleep(2)
                            await message.channel.send(smites[randomNum][i])

if __name__ == "__main__":
    TOKEN = os.environ['TOKEN']
    schedule.every().day.at("08:00").do(emptyJurgens)
    Thread(target=schedule_checker).start() 
    try:
        keep_alive()
        client.run(TOKEN)
    except discord.errors.HTTPException:
        print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
        system("python restarter.py")
        system('kill 1')