import discord
import function.bitcoin_init
import re

#get bitcoin balance
def faucet(client, message):
    print("called : tip:faucet")
    
    rpc = function.bitcoin_init.bitcoin_init()

    balance = rpc.getbalance("")
    print("Amount : " + str(balance))
    amount = balance / 100

    id = str(message.author.id)

    address = rpc.getaddressesbyaccount(id)
    if address:
        address = address[0]
        balance = float(rpc.getbalance(id))
    else:
        rpc.getnewaddress(id)
        address = rpc.getaddressesbyaccount(id)
        address = address[0]

    print(address)
    tx = rpc.sendtoaddress(address, amount)

    print(tx)
    responce = discord.Embed(title='Faucet', colour=0xDEADBF)
    responce.add_field(name="user : ", value=message.author.name, inline=False)
    responce.add_field(name="amount : ", value=amount, inline=False)
    responce.add_field(name="txid : ", value=tx, inline=False)
    return responce

def tip(client, message):
    print("called : tip:tip")
    
    rpc = function.bitcoin_init.bitcoin_init()

    pattern = r'([+-]?[0-9]+\.?[0-9]*)'
    address2 = message.content[5:40]
    amount = message.content[41:]
    amount = re.findall(pattern, amount)[0]

    id = str(message.author.id)

    address1 = rpc.getaddressesbyaccount(id)
    if address1:
        address1 = address1[0]
        balance = float(rpc.getbalance(id))
    else:
        rpc.getnewaddress(id)
        address1 = rpc.getaddressesbyaccount(id)
        address1 = address1[0]
        balance = float(rpc.getbalance(id))

    if float(amount) > balance:
        responce = discord.Embed(title='Tip', colour=0xDEADBF)
        responce.add_field(name="user : ", value=message.author.name, inline=False)
        responce.add_field(name="Error : ", value="Low balance", inline=False)
        return responce

    tx = rpc.sendfrom(id, address2, amount)

    print(tx)
    responce = discord.Embed(title='Tip', colour=0xDEADBF)
    responce.add_field(name="user : ", value=message.author.name, inline=False)
    responce.add_field(name="amount : ", value=amount, inline=False)
    responce.add_field(name="From : ", value=address1, inline=False)
    responce.add_field(name="To : ", value=address2, inline=False)
    responce.add_field(name="txid : ", value=tx, inline=False)
    return responce
