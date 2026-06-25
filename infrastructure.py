```python id="r6jw39"
from web3 import Web3
from datetime import datetime
import json

RPC_URL = "https://mainnet.base.org"
PRIVATE_KEY = "YOUR_PRIVATE_KEY"
CONTRACT_ADDRESS = (
    "0x1234567890123456789012345678901234567890"
)

web3 = Web3(
    Web3.HTTPProvider(RPC_URL)
)

account = web3.eth.account.from_key(
    PRIVATE_KEY
)

project_info = {
    "sector": "defi",
    "action": "swap",
    "network_type": "chain"
}

nonce = web3.eth.get_transaction_count(
    account.address
)

transaction = {
    "to": Web3.to_checksum_address(
        CONTRACT_ADDRESS
    ),
    "value": 0,
    "gas": 150000,
    "gasPrice": web3.eth.gas_price,
    "nonce": nonce,
    "chainId": 8453,
    "data": "0x"
}

signed_transaction = (
    web3.eth.account.sign_transaction(
        transaction,
        PRIVATE_KEY
    )
)

result = {
    "wallet": account.address,
    "category": project_info["sector"],
    "operation": project_info["action"],
    "network": project_info["network_type"],
    "signed_at": datetime.utcnow().isoformat(),
    "hash": signed_transaction.hash.hex()
}
