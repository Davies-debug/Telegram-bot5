import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.functions.channels import JoinChannelRequest

API_ID = 37266230
API_HASH = "c9f95b37dd021863d56426d500cc7227"
SESSION_STRING = "1BJWap1sBu8CDYReT05DdYWcMnQ4f5489z5E4yu3foLnf5ElZr9nUGNbtLWwY3SkhisCbkIrN2HID72R9QVFKy6h2CL3pMekMVyZrl_Kw7fpg5H5DnKE1pWdC7UDj5Tv7QCqjC4AE71ojC9Fm5OWpi3fNdu-5Zo-l1xUCkWADqdBoR0vb_y6KBPVgHx9n5WWyEzADCulsef5rlEyK_CGPpWJ0EOZVsQMc18vw_GxQpZ6lsS42vm8qyYPX9VgLYqabNTXs-O1Jljozkve86mK0hxKW5eypZo1_HHDvH3p6JFS2BI9AvjT7e_VwX3hGYj5RSyPvlRl1WC33tblt_uPHh-FE74tXpLE="

CHAT_IDS = [
    "@ChezMendoza",
    "@avietalpacino_pub",
    "@quadblade",
    "@chezkanoe",
    "@chezyatsu",
    "@chezalpha",
    "@chezz9",
    "@chezphineasesimsfr",
    "@chezdsavv",
    "@chezrass",
    "@chezdh",
    "@ChezObsidianV2",
    "@chezqui",
    "@creditviro261",
    "@pedrofabiente",
    "@chezZurgkennedy",
    "@plans_sous92",
    "@Chez_DuckLand",
    "@ChezHouse",
    "@chezlasolucee",
    "@onpaiepaslatva",
    "@chezlenfoiree",
    "@in_heisenberg_house",
    "@CvbienspasserUHQ",
    "@paradisduscam",
    "@blackwolfgroupe",
    "@chezmyflunch",
    "@vagabod",
    "@commecheztoi",
    "@LaLoiDuTalion",
    "@chezlocalbusnessChat",
    "@Aidefinaciere",
    "@CHEZSMAKA",
    "@aidefinancieres",
    "@chezdalton",
    "@chezbenzema",
    "@cheznyzoo",
    "@chezmekoi",
    "@ChezYtem",
    "@xbetcoupon90",
    "@groupeinfopositive",
    "@argentgratuitparrainage",
    "@prronooos",
    "@LACRIZ_OMIC",
    "@chezelea",
    "@chezelproffesor75",
    "@chezkaisencard"
]

SOURCE_CHANNEL = -1004297379788

async def send_messages(client):
    try:
        messages = await client.get_messages(SOURCE_CHANNEL, limit=1)
        if not messages:
            print("Aucun message trouve dans le canal source")
            return
        last_message = messages[0]
        for chat_id in CHAT_IDS:
            try:
                await client.forward_messages(chat_id, last_message)
                print(f"Message transfere a {chat_id}")
            except Exception as e:
                print(f"Erreur pour {chat_id}: {e}")
            await asyncio.sleep(10)
    except Exception as e:
        print(f"Erreur canal source: {e}")

async def main():
    async with TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH) as client:
        print("Bot demarre...")
        try:
            await client(JoinChannelRequest(SOURCE_CHANNEL))
        except Exception:
            pass
        while True:
            print("Envoi des messages...")
            await send_messages(client)
            print("Attente de 14 minutes...")
            await asyncio.sleep(14 * 60)

asyncio.run(main())
