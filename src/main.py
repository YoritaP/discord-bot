from initializetion.init import init
from bitcoinrpc.authproxy import JSONRPCException

# main
if __name__ == '__main__':
    rpc_connection = init()

    block_hash = rpc_connection.getblockhash(0)
    block = rpc_connection.getblock(block_hash)

    for block_i in block:
        print(block_i + " : " + str(block[block_i]))
