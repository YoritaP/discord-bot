from bitcoinrpc.authproxy import AuthServiceProxy
import configparser

# bitcoin.conf内のuserとpasswordを使用
def bitcoin_init():
    infile = configparser.ConfigParser()
    infile.read('../config.ini')
    
    rpc_name = infile.get('bitcoin', 'rpc_name')
    rpc_pass = infile.get('bitcoin', 'rpc_pass')

    return AuthServiceProxy("http://%s:%s@127.0.0.1:8332"%(rpc_name, rpc_pass))
