import discord

#get bitcoin block count
def getBlockCount(rpc):
    print("called : getBlockCount")
    block_count = rpc.getblockcount()

    return block_count
