import function

async def getMessage(client, message):
    
    if message.content.startswith("!command"):
        responce = function.command.command(client, message)
        await client.send_message(message.channel, embed=responce)

    if message.content.startswith("!debug"):
        responce = function.debug.debug(client, message)
        await client.send_message(message.channel, embed=responce)

    if message.content.startswith("!die"):
        if message.author.id == "282462612497891328":
            print("bot logout!")
            await client.send_message(message.channel, "bot Logout!")
            await client.logout()
    
    if message.content.startswith("!getBlockCount"):
        responce = function.getblockcount.getBlockCount()
        res = "block : " + str(responce)
        print(res)
        await client.send_message(message.channel, res)
    
    if message.content.startswith("!getBlockHash "):
        responce = function.getblockhash.getBlockHash(client, message)
        await client.send_message(message.channel, embed=responce)

    if message.content.startswith("!getBlock "):
        responce = function.getblock.getBlock(client, message)
        await client.send_message(message.channel, embed=responce)

    if message.content.startswith("!mining"):
        responce = function.generate.mining(client, message)
        await client.send_message(message.channel, embed=responce)

    if message.content.startswith("!pre_mining"):
        responce = function.generate.pre_mining(client, message)
        await client.send_message(message.channel, embed=responce)

    if message.content.startswith("!faucet"):
        responce = function.tip.faucet(client, message)
        await client.send_message(message.channel, embed=responce)

    if message.content.startswith("!balance"):
        responce = function.balance.getbalance(client, message)
        await client.send_message(message.channel, embed=responce)

    function.debug.getMessageMining()
