from utils import BloxflipLogin

b = BloxflipLogin()

username = ""
password = ""
affiliateCode = "CooLTLN"


headers = {
    'authority': 'api.bloxflip.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://bloxflip.com',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
}

params = {
    'userpass': 'true',
    'clientId': '',
}

json_data = {
    'affiliateCode': affiliateCode,
    'username': username,
    'password': password
}

bruh = b.t.post('https://api.bloxflip.com/user/login', params=params, headers=headers, json=json_data)

token = b.bloxflip_funcap_token(bruh.json()['fieldData'])


params = {
    'userpass': 'true',
    'preAuth': 'false',
    'clientId': '',
}

json_data = {
    'affiliateCode': affiliateCode,
    'username': username,
    'password': password,
    'captchaId': bruh.json()['captchaId'],
    'captchaToken': token,
}

response = b.t.post('https://api.bloxflip.com/user/login', params=params, headers=headers, json=json_data)
if "jwt" in response.json():
    print('Your bloxflip token' + response.json()['jwt'])
else:
    print(response.json())
