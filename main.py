import asyncio
import json
import random
import re
import discord
import requests
from discord.ext import commands
import token.txt

global v_c
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
}

bot = commands.Bot(command_prefix='><')
client = discord.Client()
last_news = ({
                "genshin_hub"
                "genshin_giarts"
            })
global v_c


def main():
    def separation():
        printing = "-"
        for i in range(100):
            printing = printing + "-"
        return printing

    def umg(text):
        url_text = r'http(?:s)?://\S+'
        link_img = re.findall(url_text, text)
        for item in link_img:
            item = str(item).replace("]", "")
            item = str(item).replace("[", "")
            item = str(item).replace("'", "")
            up_link_img = "*" + item + "*"
            caption = text.replace(item, up_link_img)
            text = caption
        return text

    @bot.event
    async def on_ready():  # Start bot
        print('Bot connect')
        while True:
            await genshin_hub()  # GenshinImpact art

            # await command_dis.news_stopgame(bot)  # StopGame news
            await asyncio.sleep(1)
            await news_genshinimpact()  # GenshinImpact news
            await asyncio.sleep(1)
            await free_game()
            await asyncio.sleep(1)
            await genshin_giarts()  # GenshinImpact art
            await asyncio.sleep(1)
            await promo_genshinimpact()
            await asyncio.sleep(1)
            await epic_games()
            random_poss = random.randint(55, 180)
            await asyncio.sleep(random_poss)

    @bot.event  # Event + news_day
    async def news_stopgame():
        channel = bot.get_channel(982738188911132683)
        passers_1 = requests.get("https://stopgame.ru/news")
        html = BS(passers_1.content, 'html.parser')
        title = html.find('div', class_='caption')
        score = int(len(str(title)))
        old = (str(title))

        tegg = ""
        tred = 0
        j = 44
        while j < int(score):
            if old[j] == ">":
                j = int(score)
            else:
                tegg = tegg + old[j]
                j = j + 1
        score_2 = int(len(tegg))
        Remove_last = tegg[:score_2 - 1]
        ends = "https://stopgame.ru/" + Remove_last
        las_end = "Последнии новости на stopgame.ru: " + ends

        messages = await channel.history(limit=200).flatten()
        word = las_end
        i = 0
        for msg in messages:
            if msg.content == word:
                no_post_1 = 0
                break
            else:
                no_post_1 = 1

        if no_post_1 == 1:
            await channel.send(separation())
            await channel.send(las_end)

    async def genshin_hub():
        channel = bot.get_channel(954827377085669396)
        vk_pars = "133a17f4133a17f4133a17f4421346fe9c1133a133a17f471a7b0c5bcca6560b561d7f0"
        vk_ver = "5.131"
        domain = "genshin_hub"

        reponse = requests.get('https://api.vk.com/method/wall.get',
                               params={
                                   'access_token': vk_pars,
                                   'v': vk_ver,
                                   'domain': domain,
                                   'count': 1,
                                   'offset': 1
                               }
                               )
        posts = reponse.json()['response']['items']
        # i = 0
        for post in posts:
            try:
                data = post["date"]
                with open("last_news.json") as file_json:
                    last_news = json.load(file_json)

                if data != last_news["genshin_hub"]:
                    last_news["genshin_hub"] = data
                    with open("last_news.json", "w") as file_json:
                        json.dump(last_news, file_json, indent=4, ensure_ascii=False)
                    if "attachments" in post:
                        post = post["attachments"]
                        if post[0]["type"] == "photo":
                            for i in range(len(post)):
                                url_photo = post[i]['photo']['sizes'][-1]['url']
                                await channel.send(url_photo)
                                await asyncio.sleep(1)
            except:
                pass

    async def genshin_giarts():
        channel = bot.get_channel(954827377085669396)
        vk_pars = "133a17f4133a17f4133a17f4421346fe9c1133a133a17f471a7b0c5bcca6560b561d7f0"
        vk_ver = "5.131"
        domain = "giarts"

        reponse = requests.get('https://api.vk.com/method/wall.get',
                               params={
                                   'access_token': vk_pars,
                                   'v': vk_ver,
                                   'domain': domain,
                                   'count': 1,
                                   'offset': 1
                               }
                               )
        posts = reponse.json()['response']['items']

        i = 0
        for post in posts:
            try:
                data = post["date"]
                with open("last_news.json") as file_json:
                    last_news = json.load(file_json)

                if data != last_news["genshin_giarts"]:
                    last_news["genshin_giarts"] = data
                    with open("last_news.json", "w") as file_json:
                        json.dump(last_news, file_json, indent=4, ensure_ascii=False)
                    if "attachments" in post:
                        post = post["attachments"]
                        if post[0]["type"] == "photo":
                            for i in range(len(post)):
                                url_photo = post[i]['photo']['sizes'][-1]['url']
                                await channel.send(url_photo)
                                await asyncio.sleep(1)
            except:
                pass

    async def epic_games():
        channel = bot.get_channel(982738188911132683)
        vk_pars = "133a17f4133a17f4133a17f4421346fe9c1133a133a17f471a7b0c5bcca6560b561d7f0"
        vk_ver = "5.131"
        domain = "-198731846"

        reponse = requests.get('https://api.vk.com/method/wall.get',
                               params={
                                   'access_token': vk_pars,
                                   'v': vk_ver,
                                   'owner_id': domain,
                                   'count': 1,
                                   'offset': 1
                               }
                               )
        data = reponse.json()['response']['items']
        for post in data:
            try:
                text_post = post['text']
                text_post = umg(text_post)
            except:
                text_post = 'pass'

        messages = await channel.history(limit=500).flatten()
        i = 0
        for msg in messages:
            if msg.content == text_post:
                no_post_2 = 0
                break
            else:
                no_post_2 = 1
        if no_post_2 == 1:
            await channel.send(separation())
            await channel.send(text_post)

    async def free_game():
        channel = bot.get_channel(982738188911132683)
        vk_pars = "133a17f4133a17f4133a17f4421346fe9c1133a133a17f471a7b0c5bcca6560b561d7f0"
        vk_ver = "5.131"
        domain = "frexgames"

        reponse = requests.get('https://api.vk.com/method/wall.get',
                               params={
                                   'access_token': vk_pars,
                                   'v': vk_ver,
                                   'domain': domain,
                                   'count': 1,
                                   'offset': 1
                               }
                               )
        data = reponse.json()['response']['items']
        for post in data:
            try:
                text_post = post['text']
                text_post = umg(text_post)
            except:
                text_post = ''
            try:
                img_post = post['attachments'][0]['photo']['sizes'][-1]['url']
            except:
                img_post = ''
        messages = await channel.history(limit=500).flatten()
        i = 0
        for msg in messages:
            if msg.content == text_post:
                no_post_2 = 0
                break
            else:
                no_post_2 = 1
        if no_post_2 == 1:
            await channel.send(separation())
            await channel.send(text_post)
            await channel.send(img_post)

    async def news_genshinimpact():
        channel = bot.get_channel(982738188911132683)
        vk_pars = "133a17f4133a17f4133a17f4421346fe9c1133a133a17f471a7b0c5bcca6560b561d7f0"
        vk_ver = "5.131"
        domain = "genshinimpact"

        reponse = requests.get('https://api.vk.com/method/wall.get',
                               params={
                                   'access_token': vk_pars,
                                   'v': vk_ver,
                                   'domain': domain,
                                   'count': 1,
                                   'offset': 1
                               }
                               )
        data = reponse.json()['response']['items']
        vid_p = "https://vk.com/video"
        vid_post_1 = ''
        vid_post_2 = ''
        vid_img = ''
        for post in data:
            try:
                text_post = post['text']
                text_post = umg(text_post)
            except:
                text_post = 'pass'

            try:
                if post['attachments'][0]['type']:
                    img_post = post['attachments'][0]['photo']['sizes'][-1]['url']
                else:
                    img_post = ''
            except:
                img_post = ''

            try:
                if post['owner_id']:
                    vid_post_1 = post['owner_id']
                else:
                    vid_post_1 = ''
            except:
                vid_post_1 = ''
            try:
                if post['attachments'][0]['type']:
                    vid_post_2 = post['attachments'][0]['video']['id']
                else:
                    vid_post_2 = ''
            except:
                vid_post2 = ''
            try:
                if post['attachments'][0]:
                    vid_img = post['attachments'][0]['video']['image'][8]['url']
                else:
                    vid_img = ''
            except:
                vid_img = ''

        vid_p = vid_p + str(vid_post_1) + "_" + str(vid_post_2)
        if vid_p == "https://vk.com/video" or vid_p == "https://vk.com/video-183293188_":
            vid_p = ''
        vk_poser = "Genshin Impact последнии новости:\n" + text_post + " *" + vid_p + "*"
        messages = await channel.history(limit=500).flatten()
        word = vk_poser
        i = 0
        for msg in messages:
            if msg.content == word:
                no_post_2 = 0
                break
            else:
                no_post_2 = 1
        if no_post_2 == 1:
            await channel.send(separation())
            await channel.send(vk_poser)
            try:
                await channel.send(vid_img)
            except:
                pass
            try:
                await channel.send(img_post)
            except:
                pass

    async def promo_genshinimpact():
        channel = bot.get_channel(982738188911132683)
        vk_pars = "133a17f4133a17f4133a17f4421346fe9c1133a133a17f471a7b0c5bcca6560b561d7f0"
        vk_ver = "5.131"
        domain = "genshinpromo"

        reponse = requests.get('https://api.vk.com/method/wall.get',
                               params={
                                   'access_token': vk_pars,
                                   'v': vk_ver,
                                   'domain': domain,
                                   'count': 1,
                                   'offset': 1
                               }
                               )
        data = reponse.json()['response']['items']
        for post in data:
            text_post = post['text']
            if "Промокоды:" in text_post:
                promokod = 1
            else:
                promokod = 0

            messages = await channel.history(limit=600).flatten()
            i = 0
            for msg in messages:
                if msg.content == text_post:
                    no_post_2 = 0
                    break
                else:
                    no_post_2 = 1
            if no_post_2 == 1:
                if promokod == 1:
                    await channel.send(separation())
                    await channel.send("<@&983836821383442462> " + text_post)


if __name__ == '__main__':
    main()
bot.run("token.txt")

