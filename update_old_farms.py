import os
import sys
from sqlalchemy.orm import Session

# Add app to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from app.db.session import SessionLocal
from app.models.farm import Farm

def update_farms():
    print("--- Updating Existing Farms with Default Wallet ---")
    db = SessionLocal()
    try:
        default_wallet = "0x1683D46eC2997Cb6273e4a58A35aeD57d3DeC30e"
        
        # Find farms without a wallet address
        farms_to_update = db.query(Farm).filter((Farm.wallet_address == None) | (Farm.wallet_address == "")).all()
        
        print(f"Found {len(farms_to_update)} farms to update.")
        
        for farm in farms_to_update:
            farm.wallet_address = default_wallet
            print(f"Updated Farm: {farm.name} ({farm.id})")
            
        db.commit()
        print("✅ Database update completed successfully.")
    except Exception as e:
        print(f"❌ Error during update: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    update_farms()
