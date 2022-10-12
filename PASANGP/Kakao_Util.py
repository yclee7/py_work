import json
import requests
import datetime
import os

# 카카오 토큰을 저장할 파일명
KAKAO_TOKEN_FILENAME = "res/kakao_message/kakao_token.json"

# 저장하는 함수
def save_tokens(filename, tokens):
    with open(filename, "w") as fp:
        json.dump(tokens, fp)

# 읽어오는 함수
def load_tokens(filename):
    with open(filename) as fp:
        tokens = json.load(fp)

    return tokens

# refresh_token으로 access_token 갱신하는 함수
def update_tokens(app_key, filename) :
    tokens = load_tokens(filename)

    url = "https://kauth.kakao.com/oauth/token"
    data = {
        "grant_type" : "refresh_token",
        "client_id" : app_key,
        "refresh_token" : tokens['refresh_token']
    }
    response = requests.post(url, data=data)

    # 요청에 실패했다면,
    if response.status_code != 200:
        print("error! because ", response.json())
        tokens = None
    else: # 성공했다면,
        print(response.json())
        # 기존 파일 백업
        now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_filename = filename+"."+ now
        os.rename(filename, backup_filename)
        # 갱신된 토큰 저장
        tokens['access_token'] = response.json()['access_token']
        save_tokens(filename, tokens)
        
    return tokens


def send_message(filename, template) :
    # 저장된 토큰 정보를 읽어 옴
    tokens = load_tokens(KAKAO_TOKEN_FILENAME)


    # request parameter 설정
    headers = {
        "Authorization": "Bearer " + tokens['access_token']
    }

    # JSON 형식 -> 문자열 변환
    payload = {
        "template_object" : json.dumps(template)
    }

    # 메시지 url
    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
    # 나에게 카카오톡 메시지 보내기 요청 
    res = requests.post(url, headers=headers, data=payload)

    return res
