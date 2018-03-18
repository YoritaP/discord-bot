import discord
import function.bitcoin_init

#get bitcoin block count
def getBlockCount():
    print("called : getBlockCount")
    
    rpc = function.bitcoin_init.bitcoin_init()
    
    block_count = rpc.getblockcount()

    return block_count
