import discord

class Client(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')


intents = discord.Intents.default()
intents.message_content = True


client = Client(intents=intents)
client.run('MTQ5NTE1OTExMjkyMzYxMTI3OA.Grueb0.p9UBzO_bc5xZmDKR_BAzYw_Nq1Lo6kdwEgULrM')
