import requests

url = "https://kauth.kakao.com/oauth/token"

data = {
    "grant_type" : "authorization_code",
    "client_id" : "c40e6d5de6ff29c5bd78935ff33e4451",
    "redirect_uri" : "https://localhost.com",
    "code" : "1chFAwbNVwSrAQprSzDrGoZ2rlLduac2o-DG6CvnrYuTSNQW3f4u7GBaMcWV0n0WpAMcpwopb1QAAAGDsADwmQ"
}

response = requests.post(url, data=data)

# 요청에 실패했다면,
if response.status_code != 200:
    print("error! because ", response.json())
else: # 성공했다면,
    tokens = response.json()
    print(tokens)