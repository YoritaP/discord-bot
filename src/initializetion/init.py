from bitcoinrpc.authproxy import AuthServiceProxy
import configparser

# bitcoin.conf内のuserとpasswordを使用
def bitcoin_init():
    infile = configparser.ConfigParser()
    infile.read('../config.ini')
    
    return infile.get('bitcoin', 'rpc_name'), infile.get('bitcoin', 'rpc_pass')


# init
def init():
    rpc_name, rpc_pass = bitcoin_init()
    return AuthServiceProxy("http://%s:%s@127.0.0.1:8332"%(rpc_name, rpc_pass))
