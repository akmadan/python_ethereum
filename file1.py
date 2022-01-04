## Code to just complete a transaction using ganache 

from web3 import Web3 
ganache_url = 'HTTP://127.0.0.1:7545'
web3 = Web3(Web3.HTTPProvider(ganache_url))

act1 = '0xB879b795e62D5D3042ed63E493D521409eC53FF3'
act2 = '0xdbA658C1c58f0C96460236572801e5dC0F2A34Da'

act1_private = 'fa168c23f69f9c37c3686726f8cfe813f901f764c51c5502eead60051b15ed1e'

## Building Transactions

nonce = web3.eth.getTransactionCount(act1)

tx = { 
    "nonce": nonce, 
    "to":act2, 
    "value": web3.toWei(1, 'ether') ,
    "gas": 2000000, 
    "gasPrice": web3.toWei('50', 'gwei')
}

## Signing Trasnaction

signed_tx = web3.eth.account.sign_transaction(tx, act1_private)

## Creating hash
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(tx_hash)
print(web3.toHex(tx_hash))
