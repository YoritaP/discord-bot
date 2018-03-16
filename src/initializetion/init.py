from bitcoinrpc.authproxy import AuthServiceProxy
import configparser
import discord

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
    return discord_token, rpc_connection
