from flask import Flask   # flask 클래스를 가져온다.
app = Flask(__name__)     # 플라스크 객체를 생성한다. __name__은 현재 실행 중인 모듈 이름을 전달하는 것이다.

@app.route('/')           # 기본서버 127.0.0.1:5000 뒤에 붙는 주소를 적어준다.
def main():              # 위의 주소를 호출 시 보여 줄 것을 함수로 작성해 준다. 중복되지 않도록만 적어주면된다.
    return 'Hello woobin'  # 문자열이 출력된다.
    
@app.route('/api/channel')
def channel():
    return 'Hello woobin'

@app.route('/api/hello', methods=['POST'])
def hello():
    # body = request.get_json() # 사용자가 입력한 데이터

    responseBody = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "시작하셔도 됩니다."
                    }
                }
            ]
        }
    }

    return responseBody

if __name__ == '__main__':# 다른데서 부르면 실행하지 마라는 뜻이다.
    app.run()