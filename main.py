import requests
from GeneateImage import GenerateImage
from instabot import Bot
from time import sleep
import shutil
import getpass


try:
    shutil.rmtree("config")
except:
    pass


bot = Bot()


def CreateQuote(path, styleIndex,username):
    response = requests.get('http://api.quotable.io/random')
    quote_data = response.json()

    quote_content = quote_data['content']
    quote_author = quote_data['author']

    final_path = GenerateImage(quote_author, quote_content, path, styleIndex, username)
    return str(final_path)


# CreateQuote("quotes/", 1)




def InstagramLogin(username, password):
    bot.login(username=username, password=password)
    LoopCount = 0

    while True:

        if (LoopCount % 2) == 0:
            photo = CreateQuote("quotes/", 0,username)
        else:
            photo = CreateQuote("quotes/", 1,username)
        LoopCount +=1
        sleep(1.5)
        bot.upload_photo(photo , caption="LIKE SHARE AND FOLLOW PLEASE #quotes #love #motivation #life #inspiration #quoteoftheday #instagram #motivationalquotes #instagood #quote #follow #bhfyp #like #happiness #positivevibes #success #believe #loveyourself #lifestyle #selflove #inspirationalquotes #happy #lovequotes #yourself #poetry #mindset #goals #quotestagram #quotestoliveby #bhfyp")


username = input("Enter Username: ")
password = getpass.getpass("Enter Password:")

InstagramLogin(username,password)
