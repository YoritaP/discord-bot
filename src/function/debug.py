import discord
import function.bitcoin_init

#get bitcoin balance
def debug(client, message):
    print("called : debug")

    responce = discord.Embed(title='Debug', colour=0xDEADBF)
    responce.add_field(name="user : ", value=message.author.name, inline=False)
    return responce

def exp(client, message):
    print("called : debug:exp")
    
    rpc = function.bitcoin_init.bitcoin_init()

    amount = 10

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


def getMessageMining():
    rpc = function.bitcoin_init.bitcoin_init()

    tx = rpc.generate(1)
    print("MSG : " + tx[0])
