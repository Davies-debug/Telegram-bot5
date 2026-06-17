import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.functions.channels import JoinChannelRequest

API_ID = 37266230
API_HASH = "c9f95b37dd021863d56426d500cc7227"
SESSION_STRING = "1BJWap1wBuxK1Re0zo5MHI1EzCKNMHfaNqdQY9pevHMM1iikqM_u6m7hnJO2XVm6e9RwANbyGmly6au5uYEbKXVI60DHwZ4sMUWs6gRENRB7FbZuJMP9-ojtAEK2BIHCN6g4sNs2975riHjQj-KpsykNLQr6FPeC-G6BzI29PlTwZTeXE3-XKjh8CbMkCDxtLJ4qQE01pT3H-0BDyBqFA5GFynt1HBP18T8EGqIHE5chz0wx4NsoGh49skqFA0Uuakt0ZngnNRKaeWnpBDYFV2R5etmFqbx2x_CeZYrM7AHPpjCxRqg00lQKWTvouz0TAviC0C7EBY6j-qc1WZXLy9hlqSddPHXY="

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
        while True:
            print("Envoi des messages...")
            await send_messages(client)
            print("Attente de 20 minutes...")
            await asyncio.sleep(20 * 60)

asyncio.run(main())
