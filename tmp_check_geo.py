import os, requests
from dotenv import load_dotenv

load_dotenv()
sid = os.getenv('TWILIO_ACCOUNT_SID')
token = os.getenv('TWILIO_AUTH_TOKEN')

print('--- SMS GEO-PERMISSIONS (INDIA) ---')
# Messaging Permissions API
res_msg = requests.get(f'https://messaging.twilio.com/v1/Services/default/Permissions/Countries/IN', auth=(sid, token))
if res_msg.status_code == 200:
    print("India SMS Enabled:", res_msg.json().get('enabled'))
else:
    # Try general messaging permissions if service default fails
    res_msg2 = requests.get(f'https://api.twilio.com/2010-04-01/Accounts/{sid}/Messaging/Permissions/Countries/IN.json', auth=(sid, token))
    if res_msg2.status_code == 200:
        print("India SMS Enabled:", res_msg2.json().get('enabled'))
    else:
        print('Failed to get messaging permissions', res_msg.status_code)

print('\n--- VOICE GEO-PERMISSIONS (INDIA) ---')
res_voice = requests.get(f'https://voice.twilio.com/v1/Permissions/Countries/IN', auth=(sid, token))
if res_voice.status_code == 200:
    print("India Voice Enabled:", res_voice.json().get('enabled'))
else:
    print('Failed to get voice permissions', res_voice.status_code)
