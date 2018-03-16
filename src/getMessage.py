import function

async def getMessage(rpc, client, message):
    if message.content.startswith("!getBlockCount"):
        responce = function.getblockcount.getBlockCount(rpc)
        res = "block : " + str(responce)
        print(res)
        await client.send_message(message.channel, res)
    elif message.content.startswith("!getBlockHash "):
        responce = function.getblockhash.getBlockHash(rpc, client, message)
        await client.send_message(message.channel, embed=responce)
