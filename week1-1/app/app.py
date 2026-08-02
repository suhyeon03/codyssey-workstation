from flask import Flask
import datetime
import os

app = Flask(__name__)

# 환경 변수로 데이터 저장 경로를 받는다 (볼륨/바인드 마운트 실습용)
DATA_DIR = os.environ.get("DATA_DIR", "/data")


@app.route("/")
def index():
    return (
        "<h1>Hello, Codyssey Workstation!</h1>"
        "<p>이 페이지는 Docker 컨테이너 안에서 실행 중인 Flask 웹서버입니다.</p>"
        f"<p>현재 서버 시간: {datetime.datetime.now().isoformat()}</p>"
        '<p><a href="/health">/health</a> | <a href="/count">/count</a></p>'
    )


@app.route("/health")
def health():
    return {"status": "ok"}


@app.route("/count")
def count():
    """접속할 때마다 파일에 기록 -> 볼륨 영속성 검증에 사용."""
    os.makedirs(DATA_DIR, exist_ok=True)
    counter_file = os.path.join(DATA_DIR, "count.txt")

    current = 0
    if os.path.exists(counter_file):
        with open(counter_file) as f:
            current = int(f.read().strip() or "0")

    current += 1
    with open(counter_file, "w") as f:
        f.write(str(current))

    return {"count": current, "data_file": counter_file}


if __name__ == "__main__":
    # 0.0.0.0 으로 바인딩해야 컨테이너 밖(호스트)에서 접속 가능
    port = int(os.environ.get("PORT", "5000"))
    app.run(host="0.0.0.0", port=port)
