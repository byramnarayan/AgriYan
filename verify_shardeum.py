import os
import sys
from dotenv import load_dotenv

# Add app to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

load_dotenv()

from app.services.blockchain_service import blockchain_service

def test_blockchain():
    print("--- Shardeum Connectivity Test ---")
    if not blockchain_service.w3:
        print("❌ Web3 not initialized. Check your .env file.")
        return

    print(f"✅ Connected to: {blockchain_service.rpc_url}")
    print(f"✅ Admin Address: {blockchain_service.admin_address}")
    
    try:
        balance_wei = blockchain_service.w3.eth.get_balance(blockchain_service.admin_address)
        balance_shm = blockchain_service.w3.from_wei(balance_wei, 'ether')
        print(f"💰 Admin Balance: {balance_shm} SHM")
        
        if balance_shm < 0.1:
            print("⚠️ Balance is low. Transaction tests might fail.")
        
        # Test Audit Record (Standard Transaction)
        print("\nTesting Audit Record...")
        tx_hash = blockchain_service.record_approval("test-farm-123", "approved")
        if tx_hash:
            print(f"✅ Audit Record Success! Tx Hash: {tx_hash}")
        else:
            print("❌ Audit Record Failed.")
            
    except Exception as e:
        print(f"❌ Error during test: {e}")

if __name__ == "__main__":
    test_blockchain()
