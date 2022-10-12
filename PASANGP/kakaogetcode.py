import requests

url = "https://kauth.kakao.com/oauth/authorize?client_id=c40e6d5de6ff29c5bd78935ff33e4451&response_type=code&redirect_uri=https://localhost.com"


response = requests.get(url)

# 요청에 실패했다면,
if response.status_code != 200:
    print("error! because ", response)
else: # 성공했다면,
    #code = response.json()
    print(response.content)