import json
import requests

# 카카오 토큰이 저장된 폴더 및 파일명
KAKAO_TOKEN_FILENAME = "res/kakao_message/kakao_token.json"
# 텍스트 메시지 보낼 url
url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"


# 토큰 저장하는 함수
def save_tokens(filename, tokens):
    with open(filename, "w") as fp:
        json.dump(tokens, fp)

# 토큰 읽어오는 함수
def load_tokens(filename):
    with open(filename) as fp:
        tokens = json.load(fp)

    return tokens


# 저장된 토큰 정보를 읽어 옴
tokens = load_tokens(KAKAO_TOKEN_FILENAME)

# request parameter 설정
headers = {
    "Authorization": "Bearer " + tokens['access_token']
}

data = {
    "template_object" : json.dumps({ "object_type" : "text",
                                     "text" : "3 Hello, world!, kakao talk test message  보냈음",
                                     "link" : {
                                         "web_url" : "www.naver.com"
                                     },
                                     "button_title" : "클릭버튼"
                                     })
}
#print(data)


# 나에게 카카오톡 메시지 보내기 요청 (text)
response = requests.post(url, headers=headers, data=data)
print(response.status_code)

# 요청에 실패했다면,
if response.status_code != 200:
    print("error! because ", response.json())
else: # 성공했다면,
    print('메시지를 성공적으로 보냈습니다.')