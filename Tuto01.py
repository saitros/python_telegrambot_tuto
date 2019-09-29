# -*- coding: utf-8 -*-
from flask import Flask, request, Response
import json
import os

# Flask 객체를 생성 __name__ 을 인수로 입력
app = Flask(__name__)


# 경로 설정, URL 설정
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        message = request.get_json()
        print(message)
        # 메세지가 어떤식으로 들어오는지 json 파일로 저장
        with open('response.json', 'w', encoding='UTF-8') as f:
            json.dump(message, f, indent=4, ensure_ascii=False)

        return Response('ok', status=200)
    else:
        return "Hello World!"


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
