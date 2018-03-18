from initializetion import init
import getMessage
import discord
from bitcoinrpc.authproxy import AuthServiceProxy

# bitcoin rpc
rpc_connection = AuthServiceProxy
#discord client
discord_client = discord.Client()

#bot ready!
@discord_client.event
async def on_ready():
    print("Logged in as")
    print(discord_client.user.name)
    print(discord_client.user.id)
    print("---------------")

@discord_client.event
async def on_message(message):
    await getMessage.getMessage(discord_client, message)

if __name__ == '__main__':
    token = init.discord_init()
    discord_client.run(token)
