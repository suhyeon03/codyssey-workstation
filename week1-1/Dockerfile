# 1) 베이스 이미지 선택: 가벼운 파이썬 공식 이미지
FROM python:3.12-slim

# 2) 이미지 메타데이터 (커스텀 포인트)
LABEL org.opencontainers.image.title="codyssey-flask-web"
LABEL org.opencontainers.image.description="Codyssey 워크스테이션 실습용 Flask 웹서버"

# 3) 환경 변수 (설정과 코드의 분리)
ENV PORT=5000
ENV DATA_DIR=/data
ENV PYTHONUNBUFFERED=1

# 4) 작업 디렉토리
WORKDIR /app

# 5) 의존성 먼저 복사/설치 (레이어 캐시 활용)
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 6) 애플리케이션 소스 복사
COPY app/ .

# 7) 데이터 디렉토리 생성 (볼륨 마운트 지점)
RUN mkdir -p /data

# 8) 컨테이너가 사용하는 포트 명시(문서화 목적)
EXPOSE 5000

# 9) 헬스체크 (컨테이너 상태 자가 점검)
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s \
  CMD python -c "import urllib.request,os; urllib.request.urlopen('http://localhost:'+os.environ.get('PORT','5000')+'/health')" || exit 1

# 10) 실행 명령
CMD ["python", "app.py"]
