import os, requests
from dotenv import load_dotenv

load_dotenv()
sid = os.getenv('TWILIO_ACCOUNT_SID')
token = os.getenv('TWILIO_AUTH_TOKEN')

print('--- ACCOUNT BALANCE ---')
res = requests.get(f'https://api.twilio.com/2010-04-01/Accounts/{sid}.json', auth=(sid, token))
if res.status_code == 200:
    data = res.json()
    print(f"Status: {data.get('status')}")
    print(f"Type: {data.get('type')}")
    # Balance is sometimes in a separate sub-resource or properties
else:
    print('Failed to get account info', res.status_code)

print('\n--- USAGE RECORDS (This Month) ---')
res_usage = requests.get(f'https://api.twilio.com/2010-04-01/Accounts/{sid}/Usage/Records/ThisMonth.json', auth=(sid, token))
if res_usage.status_code == 200:
    for record in res_usage.json().get('usage_records', []):
        if float(record.get('price', 0)) > 0:
            print(f"{record.get('category')}: ${record.get('price')} ({record.get('count')} {record.get('usage_unit')})")
else:
    print('Failed to get usage records')
