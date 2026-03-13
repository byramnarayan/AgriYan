import hashlib
import json
import os
import time
import logging
from web3 import Web3
from app.core.config import settings

# Setup logging
logging.basicConfig(
    filename='blockchain.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class BlockchainService:
    def __init__(self):
        self.rpc_url = settings.SHARDEUM_RPC
        self.chain_id = settings.SHARDEUM_CHAIN_ID
        self.admin_private_key = settings.SHARDEUM_ADMIN_PRIVATE_KEY
        
        if self.admin_private_key:
            self.w3 = Web3(Web3.HTTPProvider(self.rpc_url))
            try:
                self.account = self.w3.eth.account.from_key(self.admin_private_key)
                self.admin_address = self.account.address
                logger.info(f"BlockchainService initialized with admin address: {self.admin_address}")
            except Exception as e:
                self.w3 = None
                logger.error(f"Failed to initialize blockchain account: {e}")
        else:
            self.w3 = None
            logger.warning("SHARDEUM_ADMIN_PRIVATE_KEY not set. Blockchain features will be disabled.")

    def record_approval(self, farm_id: str, status: str) -> str:
        """
        Sends a minimal transaction to record the approval on-chain.
        The data field contains a hash of the Farm ID and status for immutability.
        """
        if not self.w3:
            return None

        try:
            # Create a simple hash of the data to record
            record_data = {
                "farm_id": farm_id,
                "status": status,
                "timestamp": str(int(time.time()))
            }
            data_hash = hashlib.sha256(json.dumps(record_data).encode()).hexdigest()
            
            # Prepare transaction
            gas_price = self.w3.eth.gas_price
            nonce = self.w3.eth.get_transaction_count(self.admin_address)
            
            data_hex = self.w3.to_hex(text=f"AgriAssist-Audit:{data_hash}")
            
            tx = {
                'nonce': nonce,
                'to': self.admin_address,
                'value': 0,
                'gas': 100000, # Increased for safety
                'gasPrice': gas_price,
                'data': data_hex,
                'chainId': self.chain_id
            }
            
            # Sign and send
            signed_tx = self.w3.eth.account.sign_transaction(tx, self.admin_private_key)
            tx_hash = self.w3.eth.send_raw_transaction(signed_tx.raw_transaction)
            
            tx_hex = tx_hash.hex()
            logger.info(f"Audit record TX sent for farm {farm_id}. Hash: {tx_hex}")
            return tx_hex
        except Exception as e:
            logger.error(f"Error recording approval on Shardeum for farm {farm_id}: {e}")
            return None

    async def send_reward(self, farmer_wallet: str, amount_shm: float = 0.1) -> str:
        """
        Sends a fixed SHM reward to the farmer's wallet.
        """
        if not self.w3 or not farmer_wallet:
            return None

        try:
            if not self.w3.is_address(farmer_wallet):
                print(f"Invalid farmer wallet address: {farmer_wallet}")
                return None

            nonce = self.w3.eth.get_transaction_count(self.admin_address)
            tx = {
                'nonce': nonce,
                'to': farmer_wallet,
                'value': self.w3.to_wei(amount_shm, 'ether'),
                'gas': 21000,
                'gasPrice': self.w3.eth.gas_price,
                'chainId': self.chain_id
            }
            
            # Sign and send
            signed_tx = self.w3.eth.account.sign_transaction(tx, self.admin_private_key)
            tx_hash = self.w3.eth.send_raw_transaction(signed_tx.raw_transaction)
            
            print(f"Reward of {amount_shm} SHM sent to {farmer_wallet}: {tx_hash.hex()}")
            return tx_hash.hex()
        except Exception as e:
            print(f"Error sending reward on Shardeum: {e}")
            return None

blockchain_service = BlockchainService()
