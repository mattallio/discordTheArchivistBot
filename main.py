import discord
import random
import time
import os
import json
import requests
import schedule
import pandas as pd
from threading import Thread
from keep_alive import keep_alive

intents=discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)

#list of all the smites used by the archivist
smites = [["Ceaseless Watcher!", "See this lie, this golden strand of falsehood", "Take it in your gaze and pull it, follow through its curves and twists and knots as it unravels all before you", " Unweave it now, its fear and its falsehood, its hidden teeth and the ones it wears so proudly", "Take all that it is and all that it has", "It", "Is", "Yours"],
["Ceaseless Watcher!", "Turn your gaze upon this wretched thing"], ["Ceaseless Watcher!", "Turn your gaze upon this thing and drink", "Your", "Fill"], 
["Ceaseless Watcher!", "Gaze upon this thing, this lost and broken splinter of fear", "Take what is left of it as your own and leave no trace of it behind", "It", "Is", "Yours"]
]
#tolerance of the archivist towards swearing
SWEARSMAX = 10
#bad archival assistants will be put in the jurgens dictionary and will be punished if persistent with the swearing
jurgens = {}
#list of chats where the archivist has sent a sticker in the recent past
timer = []

def countFolder(commandFolder):
   dir_path = fr'{commandFolder}'
   count = 0
   for path in os.listdir(dir_path):
      if os.path.isfile(os.path.join(dir_path, path)):
         count += 1
   return count

#checks if any of the scheduled functions is to be run
def schedule_checker():
    while True:
        schedule.run_pending()
        time.sleep(1)

#the archivist forgives the bad archival assistants
def emptyJurgens():
    global jurgens
    jurgens.clear()

#after 2 minutes the archivist can send a sticker based on the context again
def emptyTimer():
    global timer
    timer.clear()

#checks if a message sent by a user has a sticker reference
def checkSticker(message, type):
    stickerNumber = pd.read_excel(r"Stickers/0-sticker-to-number.xlsx")
    if type == "titles":
        words = stickerNumber.Titles
    elif type == "words":
        words = stickerNumber.Words
    stickerNum = 1
    for word in words:
        for wordMessage in message.split():
            if len(wordMessage)>3 and wordMessage.upper() in word.split():
                del stickerNumber
                del words
                return stickerNum
        stickerNum += 1
    del stickerNumber
    del words
    return stickerNum

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

#the archivist spits hate towards a specific target (default=jurgein leitner)
async def jurgenRant(message, victim):
    victimSplitted = victim.split(" ")
    victimNoSpace = ""
    for el in victimSplitted:
        victimNoSpace = victimNoSpace + el[0].upper() + el[1:].lower()
    await message.reply(f"{victim.upper()}?")
    await message.channel.typing()
    time.sleep(2)
    await message.channel.send(f"STUPID IDIOT MOTHERFUCKING {victim.upper()} GOD DAMN FOOL BOOK COLLECTING DUST EATING RAT OLD BASTARD SHITHEAD IDIOT AVATAR OF THE WHORE BIGGEST CLOWN IN THE CIRCUS LAUGHED OUT OF TOWN COWBOY MOTHERFUCKING {victim.upper()}")
    await message.channel.typing()
    time.sleep(7)
    await message.channel.send(f"STOP PINNING ME WHEN I TALK ABOUT {victim.upper()} I HATE HIM SO MUCH WHY DOES HE HAVE SO MANY FUCKED UP BOOKS WHY DID HE DECIDE TO FUCK AROUND AND FIND OUT JUST SET THEM LOOSE IS HE DEAD IS HE A BASTARD MAN HAS SUCH A VISCERAL AFFECT ON ME NOT EVEN IN THE ROOM NEVER SEEN THIS MANS FACE AND I KNOW HE HAS THE WORLDS SHITTIEST BEARD GET AWAY FROM ME")
    await message.channel.typing()
    time.sleep(9)
    await message.channel.send(f"if i wanted to get into heaven and god said {victim.lower()}'s waiting inside i would piss on gods feet for the sole purpose of getting sent back down")
    await message.channel.typing()
    time.sleep(5)
    await message.channel.send(f"if i have to deal with {victim.lower()} speaking one word in person on voice in podcast not only will i close the tab i will delete my bookmark out of spite and have to rewatch the entire series again for the experience of being able to skip all the times when he is mentioned or alive")
    await message.channel.typing()
    time.sleep(7)
    await message.channel.send("i dont even know why i hate him so much. he collects books but i am just mad because i am angy")
    await message.channel.typing()
    time.sleep(4)
    await message.channel.send("he better have some fucked up backstory to explain this if hes just some rich shithead whos a fan of creepypasta and wanted the irl version ill go ham")
    await message.channel.typing()
    time.sleep(6)
    await message.channel.send("BETTER have had a book make him kill a man cuz if he didnt Im going to make him")
    await message.channel.typing()
    time.sleep(4)
    await message.channel.send(f"paypal.com/IFuckingHate{victimNoSpace}")
    await message.channel.typing()
    time.sleep(4)
    await message.channel.send("episodes not even about him. vaguely mentioned what is supposed to maybe be his library and I lost it")
    await message.channel.typing()
    time.sleep(4)
    await message.channel.send(f"where the fuck is {victim.lower()} if hes still alive im going to so deeply wish he wasnt")
    await message.channel.typing()
    time.sleep(4)
    await message.channel.send("crusty old man")
    await message.channel.typing()
    time.sleep(3)
    await message.channel.send(f"ill punch {victim.lower()} and his sad frail old man twig bones will simply flake apart under my epic huge meat fist and he will disintegrate until all thats left is one final book he kept on him at all times simply titled Now You Fucked Up in ancient yiddish")
    await message.channel.typing()
    time.sleep(8)
    await message.channel.send("im not breathing im hyperventilating at this point")
    await message.channel.typing()
    time.sleep(4)
    await message.channel.send(f"i hope theres a date given for when {victim.lower()} died or will die so i can make it a reminder on my phone")
    await message.channel.typing()
    time.sleep(5)
    await message.channel.send("everyday once a year i will see it and do anything but pay respects to the man who had so many fucked up if true books")

#here are all the bot's command and features
@client.event
async def on_message(message):

    #the archivist doesn't answer to its own messages
    if message.author == client.user:
        return
    
    #initializes every member of the chat to the bad list, just in case
    if message.author.id not in jurgens:
        jurgens[message.author.id] = [0]
    
    #the archivist greets a new member
    if str(message.type) == "MessageType.new_member":
        await message.channel.send(f"{message.author.name}, you're welcome to the Magnus Institute")
        statementBegins = open(r"Stickers/15.webp", "rb")
        await message.channel.typing()
        time.sleep(1)
        await message.channel.send("The name in Jonathan Sims")
        await message.channel.typing()
        time.sleep(2)
        await message.channel.send("Head Archivist of the Magnus Institute")
        await message.channel.typing()
        time.sleep(2)
        await message.channel.send("London")
        await message.channel.typing()
        time.sleep(2)
        await message.channel.send(file=discord.File(statementBegins))
        return

    #the archivist introduces himself
    if "/greet" in message.content:
        statementBegins = open(r"Stickers/15.webp", "rb")
        await message.channel.typing()
        time.sleep(1)
        await message.channel.send("The name in Jonathan Sims")
        await message.channel.typing()
        time.sleep(2)
        await message.channel.send("Head Archivist of the Magnus Institute")
        await message.channel.typing()
        time.sleep(2)
        await message.channel.send("London")
        await message.channel.typing()
        time.sleep(2)
        await message.channel.send(file=discord.File(statementBegins))
    
    #the archivist sends a random sticker
    if "/sticker" in message.content:
        stickerNumber = pd.read_excel(r"Stickers/0-sticker-to-number.xlsx")
        titles = stickerNumber.Titles
        randomNum = random.randint(1, len(titles))
        sticker = open(rf"Stickers/{randomNum}.webp", "rb")
        await message.channel.send(file = discord.File(sticker))
        sticker.close()
        del titles
        del stickerNumber

    #the archivist sends a random fandom pic
    if "/fandom" in message.content:
        randomNum = random.randint(1, countFolder("Fandompics"))
        fandomPic = open(rf"Fandompics/{randomNum}.jpg", "rb")
        await message.channel.send(file = discord.File(fandomPic))
        fandomPic.close()

    #the archivist simtes the the liar
    if "/lies" in message.content:
        await message.channel.send(smites[0][0])
        for i in range(1, len(smites[0])):
            if smites[0][i] == "It" or smites[0][i] == "Is" or smites[0][i] == "Yours":
                await message.channel.typing()
                time.sleep(1)
                await message.channel.send(smites[0][i])
            else: 
                await message.channel.typing()
                time.sleep(2)
                await message.channel.send(smites[0][i])

    #the archivist spits hate towards juergein leitner
    if "/avatar of the whore" in message.content:
        await jurgenRant(message, "jurgein leitner")

    #the archivist spits hate towards a specific target
    if "/obliterate" in message.content:
        victimList = (message.content).split(" ")
        victimList = victimList[(victimList.index("/obliterate")+1):]
        victim = ""
        for name in victimList:
            if victim == "":
                victim = name
            else: 
                victim += " " + name
        if victim != "":
            await jurgenRant(message, victim)

    #the archivist connects to a huggingface model and generates an answer to the message
    if "ARCHIVIST" in message.content.upper():
        url = 'https://api-inference.huggingface.co/models/mattallio/Archivist-medium-dialoGPT'
        huggingToken = os.environ['HUGGINGFACE_TOKEN']
        headers = {
            'Authorization': 'Bearer {}'.format(huggingToken)
        }
        payload = {
        "inputs": message.content,
        "options": {"wait_for_model":True}
        }
        data = json.dumps(payload)
        res = requests.request('POST', url, headers=headers, data=data)
        ret = json.loads(res.content.decode('UTF-8'))
        answer = ret.get('generated_text', None)
        try:
            await message.reply(answer)
        except:
            print("Model response:", ret)

    #the archivist shows off with his abilities
    if "/help" in message.content:
        helpMessage = open(r"Utilities/help.txt", "r")
        await message.channel.send(helpMessage.read())
        helpMessage.close()

    #command to send a sticker specified after "/"
    if "/" in message.content:
        messageText = message.content
        index = messageText.index("/")
        messageText = messageText[index+1:]
        if " " in messageText:
            index2 = messageText.index(" ")
            messageText = messageText[:index2]
        stickerNum = checkSticker(messageText, "titles")
        if stickerNum <= countFolder(r"Stickers")-1:
            sticker = open(fr"Stickers/{stickerNum}.webp", "rb")
            await message.channel.send(file = discord.File(sticker))
            sticker.close()

    #if the message.channel is in the timer list the archivist will not send a sticker every time a word that's in a sticker is said
    #the timer list will be resetted every two minutes so that the archivist can send a sticker based on the context every 2 minutes
    if message.channel not in timer:
        stickerNum = checkSticker(message.content, "words")
        if stickerNum <= countFolder(r"Stickers")-1:
            sticker = open(fr"Stickers/{stickerNum}.webp", "rb")
            await message.channel.send(file = discord.File(sticker))
            sticker.close()
            timer.append(message.channel)

    #the archivist checks if in the message there is any swear and if so will proceed to smite the user while taking note of his bad behaviour
    swearsFile = open("swears.txt", "r")
    swears = (swearsFile.read()).split("\n")
    swearsFile.close()
    for word in message.content.split():
        for swear in swears:    
            if word.lower() == swear or (len(word) > len(swear) and swear in word.lower()):
                jurgens[message.author.id][0] += 1
                if jurgens[message.author.id][0] == SWEARSMAX:
                    await message.author.edit(nick = "Jurgen Leitner")
                    await jurgenRant(message, "jurgein leitner")
                    jurgens[message.author.id][0] = 0
                else:
                    randomNum = random.randint(0, len(smites)-1)
                    await message.channel.typing()
                    await message.reply(smites[randomNum][0])
                    for i in range(1, len(smites[randomNum])):
                        if smites[randomNum][i] == "It" or smites[randomNum][i] == "Is" or smites[randomNum][i] == "Yours":
                            await message.channel.typing()
                            time.sleep(1)
                            await message.channel.send(smites[randomNum][i])
                        else: 
                            await message.channel.typing()
                            time.sleep(2)
                            await message.channel.send(smites[randomNum][i])

if __name__ == "__main__":
    TOKEN = os.environ['TOKEN']
    schedule.every().day.at("08:00").do(emptyJurgens)
    schedule.every(2).minutes.do(emptyTimer)
    Thread(target=schedule_checker).start() 
    try:
        keep_alive()
        client.run(TOKEN)
    except discord.errors.HTTPException:
        print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
        os.system("python3 restarter.py")
        os.system('kill 1')