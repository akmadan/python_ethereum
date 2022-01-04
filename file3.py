## Getting Blockchain Info using Infura URL from Etherscan


## We can interact with blockchain using web3
from web3 import Web3 

infura_url = "https://mainnet.infura.io/v3/01f5d8e49726484a85c9fb2d26286f19"

web3  = Web3(Web3.HTTPProvider(infura_url))

print(web3.eth.blockNumber) ## printing latest block no. added to eth blockchain
print(web3.eth.getBlock(web3.eth.blockNumber))

hash  = '0x4b0bf337f94fe9e1ba1a6376118a7537c1ce307ddb0a68ef60d40f5292547e48'

print(web3.eth.getTransactionByBlock(hash, 2))