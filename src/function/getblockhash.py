import discord
from initializetion import init
import re

#get bitcoin block hash
def getBlockHash(client, message):
    print("called : getBlockHash")
    block_number = re.search(r"(?P<count>-?[0-9]+)[dD ](?P<surface>-?[0-9]+)((?P<op>\<=|\>=|\<|\>|=<|=>)(?P<status>-?[0-9]+))?(\s(?P<skill>.*))?", message.content)
    print("number : " + str(block_number))
    block_hash = init.rpc_connection.getblockhash(block_number)

    responce = discord.Embed(title='getBlockHash', colour=0xDEADBF)
    responce.set_author(name=client.user.name, icon_url=client.user.default_avatar_url)
        
    responce.add_field(name="block :" + str(block_number), value=block_hash, inline=False)
    return responce
