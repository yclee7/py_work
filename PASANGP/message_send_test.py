from regex import template
import Kakao_Util

# 카카오 토큰을 저장할 파일명
KAKAO_TOKEN_FILENAME = "res/kakao_message/kakao_token.json"


KAKAO_APP_KEY = "c40e6d5de6ff29c5bd78935ff33e4451"
tokens = Kakao_Util.update_tokens(KAKAO_APP_KEY, KAKAO_TOKEN_FILENAME)
# 토큰 업데이트 -> 토큰 저장 필수!
Kakao_Util.save_tokens(KAKAO_TOKEN_FILENAME, tokens)

template_text = {
    "object_type" : "text",
    "text" : "7Hello, world!, kakao talk test message  보냈음",
    "link" : {
        "web_url" : "www.naver.com"
    },
    "button_title" : "클릭버튼"
}

template_list = {
    "object_type" : "list",
    "header_title" : "초밥 사진",
    "header_link" : {
        "web_url" : "www.naver.com",
        "mobile_web_url" : "www.naver.com"
    },
    "contents" : [
        {
            "title" : "1. 광어초밥",
            "description" : "광어는 맛있다",
            "image_url" : "https://search1.kakaocdn.net/argon/0x200_85_hr/8x5qcdbcQwi",
            "image_width" : 50, "image_height" : 50,
            "link" : {
                "web_url" : "www.naver.com",
                "mobile_web_url" : "www.naver.com"
            }
        },
        {
            "title" : "2. 참치초밥",
            "description" : "아니다 참치가 더 맛있다",
            "image_url" : "https://search2.kakaocdn.net/argon/0x200_85_hr/IjIToH1S7J1",
            "image_width" : 50, "image_height" : 50,
            "link" : {
                "web_url" : "www.naver.com",
                "mobile_web_url" : "www.naver.com"
            }
        }

    ],
    "buttons" : [
        {
            "title" : "웹으로 이동",
            "link" : {
                "web_url" : "www.naver.com",
                "mobile_web_url" : "www.naver.com"
            }
        }
    ]
}

template = template_list


res = Kakao_Util.send_message(KAKAO_TOKEN_FILENAME,template)
# 요청에 실패했다면,
if res.status_code != 200:
    print("error! because ", res.json())
else: # 성공했다면,
    print('메시지를 성공적으로 보냈습니다.')