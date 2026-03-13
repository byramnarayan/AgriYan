import sqlite3
import json

def check_data():
    conn = sqlite3.connect('agritech.db')
    cursor = conn.cursor()
    
    print("--- Farm Records (wallet and tx_hash) ---")
    cursor.execute("SELECT id, name, verification_status, wallet_address, shardeum_tx_hash FROM farms")
    farms = cursor.fetchall()
    for f in farms:
        print(f"ID: {f[0]}, Name: {f[1]}, Status: {f[2]}, Wallet: {f[3]}, TX: {f[4]}")
        
    print("\n--- Farmer Records (wallet) ---")
    cursor.execute("SELECT id, name, wallet_address FROM farmers")
    farmers = cursor.fetchall()
    for fm in farmers:
        print(f"ID: {fm[0]}, Name: {fm[1]}, Wallet: {fm[2]}")
        
    conn.close()

if __name__ == "__main__":
    check_data()
