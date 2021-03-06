# -*- coding: utf-8 -*-

import requests
from flask import Flask, request, Response

API_KEY = 'API_KEY'

app = Flask(__name__)


def parse_message(data):
    chat_id = data['message']['chat']['id']
    msg = data['message']['text']

    return chat_id, msg


def send_message(chat_id, text):
    """
    chat_id : 사용자 아이디 코드
    text : 사용자 대화내용

    Return :
    함수에 변수를 할당할때 text='hello' 라고 선언
    --> text에 관련된 값이 전달되지 않으면 hello를 default로 사용

    사용자에게 메세지를 보내는 내용의 함수
    """
    url = 'https://api.telegram.org/bot{token}/sendMessage'.format(token=API_KEY)
    # 변수들을 딕셔너리 형식으로 묶음
    params = {'chat_id': chat_id, 'text': text}

    # Url 에 params 를 json 형식으로 변환하여 전송
    # 메세지를 전송하는 부분
    response = requests.post(url, json=params)
    print(response)
    return response


def send_keyboard(chat_id, text):
    """
    Chat-id 와 text를 변수로 받아 메세지를 보내주는데
    params 안에 키보드를 설정해서 같이 보내주는 방법

    https://core.telegram.org/bots/api#keyboardbutton
    """
    url = 'https://api.telegram.org/bot{token}/sendMessage'.format(token=API_KEY)  # sendMessage
    keyboard = {  # Keyboard 형식
        'keyboard': [[{
            'text': '버튼1'
        },
            {'text': '버튼2'
             }],
            [{'text': '버튼3'},
             {'text': '바튼4'}]
        ],
        'one_time_keyboard': True
    }
    # 변수들을 딕셔너리 형식으로 묶음
    params = {'chat_id': chat_id, 'text': "자 여기 너가 사용할 키보드야", 'reply_markup': keyboard}

    # Url 에 params 를 json 형식으로 변환하여 전송
    # 메세지를 전송하는 부분
    response = requests.post(url, json=params)

    return 0


# 경로 설정, URL 설정
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        message = request.get_json()

        chat_id, msg = parse_message(message)

        """
        실습 01
        새로운 분기를 시켜서 사용자가 처음 들어왔을때 (/start 버튼을 눌렀을때)
        환영인사 (Welcome Message)를 보내도록 해봅시다
        (필요하다면 함수를 선언해도 좋습니다.
        """

        if '버튼' in msg:
            send_keyboard(chat_id, msg)
            return Response('ok', status=200)

        send_message(chat_id, msg)

        return Response('ok', status=200)
    else:
        return 'Hello World!'


# Python 에서는 실행시킬때 __name__ 이라는 변수에
# __main__ 이라는 값이 할당
if __name__ == '__main__':
    app.run(port=80, host='0.0.0.0')
