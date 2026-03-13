import sqlite3
import os

db_path = "agritech.db"

def migrate():
    if not os.path.exists(db_path):
        print(f"Error: {db_path} not found.")
        return

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    print("Checking for missing columns in 'farms' table...")
    
    # Get current columns
    cursor.execute("PRAGMA table_info(farms)")
    columns = [column[1] for column in cursor.fetchall()]

    # Add wallet_address if missing
    if 'wallet_address' not in columns:
        print("Adding 'wallet_address' column...")
        cursor.execute("ALTER TABLE farms ADD COLUMN wallet_address VARCHAR(42)")
    
    # Add shardeum_tx_hash if missing
    if 'shardeum_tx_hash' not in columns:
        print("Adding 'shardeum_tx_hash' column...")
        cursor.execute("ALTER TABLE farms ADD COLUMN shardeum_tx_hash VARCHAR(100)")

    # Update old records with default wallet address
    print("Updating old farm records with default wallet address...")
    default_wallet = "0x1683D46eC2997Cb6273e4a58A35aeD57d3DeC30e"
    cursor.execute("UPDATE farms SET wallet_address = ? WHERE wallet_address IS NULL", (default_wallet,))

    # Check farmers table
    print("Checking for missing columns in 'farmers' table...")
    cursor.execute("PRAGMA table_info(farmers)")
    user_columns = [column[1] for column in cursor.fetchall()]

    if 'wallet_address' not in user_columns:
        print("Adding 'wallet_address' column to 'farmers' table...")
        cursor.execute("ALTER TABLE farmers ADD COLUMN wallet_address VARCHAR(42)")
    
    cursor.execute("UPDATE farmers SET wallet_address = ? WHERE wallet_address IS NULL", (default_wallet,))

    conn.commit()
    conn.close()
    print("Migration completed successfully.")

if __name__ == "__main__":
    migrate()
