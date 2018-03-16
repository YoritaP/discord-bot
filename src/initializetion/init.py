from bitcoinrpc.authproxy import AuthServiceProxy
import configparser
import discord

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

# bitcoin.conf内のuserとpasswordを使用
def bitcoin_init():
    infile = configparser.ConfigParser()
    infile.read('../config.ini')
    
    rpc_name = infile.get('bitcoin', 'rpc_name')
    rpc_pass = infile.get('bitcoin', 'rpc_pass')

    return AuthServiceProxy("http://%s:%s@127.0.0.1:8332"%(rpc_name, rpc_pass))

# set discord token
def discord_init():
    infile = configparser.ConfigParser()
    infile.read('../config.ini')

    return infile.get('discord', 'token')

def init():
    rpc_connection = bitcoin_init()
    discord_token = discord_init()
    discord_client.run(discord_token)
