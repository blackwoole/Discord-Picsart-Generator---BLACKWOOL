import tls_client
import colorama
from colorama import Fore
import requests
import random
import string
import os
from tasks import *
from traceback import print_exc
cap_key = '' # Enter Your Captcha Key Here
cap_service = ''#Enter Your Captcha Service Here | Eg : capmonster, capsolver
genned = 0
sucess = Fore.LIGHTGREEN_EX+'[CLAIMED/SUCESS]'+Fore.RESET
error = Fore.LIGHTRED_EX+'[ERROR/FAILURE]'+Fore.RESET
trying = Fore.LIGHTBLUE_EX+'[STARTED]'+Fore.RESET
inputt = Fore.LIGHTWHITE_EX+'[INPUT]'+Fore.RESET
xb = int(input(f"{inputt}Enter How Much Promo You Want To Generate?: "))
proxy = 'http://04RqdeGI-cc-ccus:pas8Tw6B@pa-chicooked-US.ntnt.network:5959'
def gen_rnd_pass():
    lt = 'x', 'y', 'z', 'm', 'n', 'f', 'x', 's', 'i', 'n'
    return f"{random.choice(lt)}{random.randint(900000, 199999999)}{random.choice(lt)}"

def gen_rnd_email():
    lt = 'x', 'y', 'z', 'm', 'n', 'f', 'x', 's', 'i', 'n', 'u', 'l', 'r', 'e'
    return f"{random.choice(lt)}{random.randint(90005, 1999906)}{random.choice(lt)}+eforce@gmail.com"
#https://github.com/notlit69/picsart-promo-gen/blob/main/tasks.py
def rl(len : int) -> str:
    return ''.join(random.choices(string.ascii_letters,k=len))

session = tls_client.Session(

    client_identifier="chrome112",

    random_tls_extension_order=True

)
print(f'''{trying}Generator Has Started!
        Quantity: {xb}      Service: {cap_service}   Key: {cap_key}   Delay After Every Generate: 0(You Can Modify It)''')
def gen():
    captcha = solve(cap_key,cap_service)
    
    if not captcha.get('solved'):
        captcha_excp = captcha.get('excp')
        print(f"{error}Failed to solve captcha! Error : {captcha_excp}")
        return
    gcap_respo = captcha.get('gcap')
    password = gen_rnd_pass()
    email = gen_rnd_email()
    #https://github.com/notlit69/picsart-promo-gen/blob/main/tasks.py
    headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'connection': 'keep-alive',
    'g-recaptcha-action': 'signup',
    'g-recaptcha-token': gcap_respo,
    'origin': 'https://picsart.com',
    'platform': 'website',
    'pragma': 'no-cache',
    'referer': 'https://picsart.com/',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'token': rl(15),
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
}

    data = {
    'password': password,
    'email': email,
    'consents': [],
}
    try:
        resp = session.post('https://api.picsart.com/user-account/auth/signup', headers=headers, json=data, proxy=proxy)
    except Exception as e:
        print(f"{error}:(  Failed To Post Request | {str(e)}")
        return
        
    json : dict = resp.json()
    status = json.get('status')
    if status == 'error':
        err = json.get('message')

        if 'Bot' in err:
            print(f'{error}:( Bot Behaviour Was Detected By Picsart!')
        else:
            print(f'{error}Failed To Signup | Error: {err}')
        return
    access_token = json['token']['access_token']
    api_key = json['key']
    sheaders = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': f'Bearer {access_token}',
    'cache-control': 'no-cache',
    'connection': 'keep-alive',
    'content-type': 'application/json',
    'origin': 'https://picsart.com',
    'platform': 'website',
    'pragma': 'no-cache',
    'referer': 'https://picsart.com/',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.76',
    'x-api-key': api_key,
}

    try:
        sresp = session.get('https://api.picsart.com/discord/link', headers=sheaders, proxy=proxy)
    except Exception as e:
        print(f"{error}Failed To Request | Error : {str(e)}")
        return

    sjson : dict = sresp.json()
    sstatus = sjson.get('status')
    if sstatus == 'success':
        slink = sjson.get('response')
        genned += 1
        print(f"{sucess}Suceed To Generate Promo -> {email}:{password} | Generated {genned} Promos Till Now!")
        with open:
            open('promotion.txt','a').write(f"{slink}\n")  

    else:
        print(f"{error}Unknown Error While Claiming A Promo. Response : {sjson}")
    time.sleep(0)
for i in range(xb):
    gen()