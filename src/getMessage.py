import function

async def getMessage(client, message):
    if message.content.startswith("!getBlockCount"):
        responce = function.getblockcount.getBlockCount(client)
        await client.send_message(message.channel, embed=responce)
    elif message.content.startswith("!getBlockHash "):
        responce = function.getblockhash.getBlockHash(client, message)
        await client.send_message(message.channel, embed=responce)
    elif message.content.startswith("!debug"):
        function.debug.debug()
        await client.send_message(message.channel, "Hello World!")
