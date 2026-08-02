# 개발자 작업실 꾸미기 — 내 터미널 실습 가이드

이 문서는 **내 Mac 터미널에서 직접 따라 하면서** 과제 필수 항목을 전부 수행하는 순서입니다.
각 단계마다 명령을 실행하고 **명령어 + 출력**을 캡처(또는 복붙)해서 `README.md`에 옮기세요.

> 환경: macOS + OrbStack(= Docker 엔진 제공, sudo 불필요) + zsh + VSCode
> 준비: 이 폴더(`codyssey-workstation/`) 안에 `app/app.py`, `app/requirements.txt`, `Dockerfile` 이 이미 들어 있습니다.

---

## 0. 사전 준비 — OrbStack 실행

1. OrbStack 앱을 설치/실행합니다. (실행하면 내부적으로 Docker 엔진이 함께 뜹니다)
2. 터미널을 열고 docker 명령이 잡히는지 확인합니다.

```bash
docker --version
```

OrbStack이 켜져 있으면 정상적으로 버전이 출력됩니다. 안 나오면 OrbStack 앱을 먼저 켜세요.

---

## 1. 터미널 기본 조작 + 작업 디렉토리 구성

과제 요구: 현재 위치 / 목록(숨김 포함) / 이동 / 생성 / 복사 / 이동·이름변경 / 삭제 / 내용 확인 / 빈 파일 생성

```bash
# 현재 위치 확인
pwd

# 홈으로 이동 후 실습 폴더 생성
cd ~
mkdir -p ~/codyssey/practice
cd ~/codyssey/practice

# 목록 확인 (숨김 파일 포함)
ls -la

# 빈 파일 생성
touch note.txt

# 파일에 내용 쓰기 + 내용 확인
echo "hello codyssey" > note.txt
cat note.txt

# 복사
cp note.txt note_copy.txt

# 디렉토리 생성 후 이동(이름변경)
mkdir backup
mv note_copy.txt backup/note_backup.txt

# 이름 변경
mv note.txt memo.txt

# 결과 확인
ls -laR

# 삭제
rm backup/note_backup.txt
rm -r backup
ls -la
```

✅ **README에 남길 것**: 위 명령들의 입력과 출력.
📌 **설명 포인트(과제 목표)**: 절대경로(`/Users/이름/codyssey`)와 상대경로(`./practice`, `../`)의 차이를 예시로 정리하세요.

---

## 2. 파일 권한 실습 (파일 1개 + 디렉토리 1개)

과제 요구: 권한 확인/변경, 변경 전/후 비교. r/w/x 및 755/644 해석 설명.

```bash
cd ~/codyssey/practice

# 실습용 파일과 디렉토리 준비
touch perm_file.sh
mkdir perm_dir

# [변경 전] 권한 확인
ls -l perm_file.sh
ls -ld perm_dir

# 파일에 실행 권한 부여 (644 -> 755)
chmod 755 perm_file.sh

# 디렉토리 권한 변경 (예: 700 = 소유자만 접근)
chmod 700 perm_dir

# [변경 후] 권한 확인
ls -l perm_file.sh
ls -ld perm_dir
```

✅ **README에 남길 것**: 변경 전/후 `ls -l` 출력 비교.
📌 **설명 포인트**:
- `r`(읽기=4) `w`(쓰기=2) `x`(실행=1)
- `755` = 소유자 `rwx(7)`, 그룹 `r-x(5)`, 기타 `r-x(5)`
- `644` = 소유자 `rw-(6)`, 그룹 `r--(4)`, 기타 `r--(4)`

---

## 3. Docker 설치/점검

과제 요구: 버전 확인 + 데몬 동작 확인.

```bash
# 버전 확인
docker --version

# 데몬 동작 및 시스템 정보 확인
docker info
```

✅ **README에 남길 것**: 두 명령의 출력(길면 앞부분 발췌 + 스크린샷).
📌 `docker info`가 에러 없이 출력되면 데몬(OrbStack 엔진)이 정상 동작 중이라는 뜻입니다.

---

## 4. Docker 기본 운영 + 컨테이너 실행 실습

### 4-1. hello-world

```bash
docker run hello-world
```

### 4-2. ubuntu 컨테이너 진입 후 명령 실행

```bash
# ubuntu 컨테이너에 들어가서(-it) 셸 사용
docker run -it --name my-ubuntu ubuntu bash

# --- 컨테이너 내부 프롬프트(root@...)에서 ---
ls
echo "inside container"
exit
# --- 컨테이너 밖으로 나옴 ---
```

### 4-3. attach vs exec 차이 관찰

```bash
# 백그라운드로 계속 살아있는 컨테이너 실행
docker run -d --name keep-alive ubuntu sleep infinity

# exec: 실행 중인 컨테이너에 "새 프로세스"로 들어가기 (나가도 컨테이너 유지)
docker exec -it keep-alive bash -c "echo hi from exec"

# 운영 명령들
docker ps            # 실행 중 목록
docker ps -a         # 전체(종료 포함) 목록
docker images        # 이미지 목록
docker logs keep-alive   # 로그 확인
docker stats --no-stream # 리소스 확인(1회)

# 정리
docker rm -f keep-alive my-ubuntu
```

✅ **README에 남길 것**: hello-world 성공 출력, ubuntu 내부 명령 결과, `ps`/`images`/`logs`/`stats` 출력.
📌 **설명 포인트**: `exit`로 나가면 메인 프로세스가 끝나 컨테이너가 종료되지만, `exec`로 들어간 셸은 나가도 원래 컨테이너는 계속 살아있음. → attach(메인 프로세스에 붙음) vs exec(새 프로세스) 차이.

---

## 5. Dockerfile 기반 커스텀 이미지 빌드 & 실행

이 폴더에 있는 `Dockerfile`을 사용합니다. (베이스: `python:3.12-slim` + Flask 앱 추가 = B안 커스텀)

```bash
# 이 프로젝트 폴더로 이동 (codyssey-workstation 폴더 위치로 바꿔주세요)
cd /path/to/codyssey-workstation

# 이미지 빌드
docker build -t codyssey-web:1.0 .

# 빌드된 이미지 확인
docker images | grep codyssey-web
```

✅ **README에 남길 것**: 빌드 로그(성공 메시지), `docker images` 출력.
📌 **커스텀 포인트 요약**(README에 적기):
- `LABEL` — 이미지 메타데이터(제목/설명) 부여
- `ENV PORT / DATA_DIR` — 설정을 코드에서 분리
- `HEALTHCHECK` — 컨테이너 자가 상태 점검
- `COPY app/` — 내 애플리케이션 코드 주입

---

## 6. 포트 매핑 접속 증거

과제 요구: `-p <host>:<container>` 실행 후 브라우저 주소창(포트 포함) + 응답 화면.

```bash
# 8080(호스트) -> 5000(컨테이너) 매핑
docker run -d -p 8080:5000 --name web-8080 codyssey-web:1.0

# 터미널로 응답 확인
curl http://localhost:8080

# (2회차) 다른 포트로도 실행
docker run -d -p 8081:5000 --name web-8081 codyssey-web:1.0
curl http://localhost:8081
```

그다음 **브라우저**에서 `http://localhost:8080` 접속 → 주소창(포트 포함)과 페이지가 함께 보이도록 스크린샷.

✅ **README에 남길 것**: `curl` 출력 + 브라우저 스크린샷(주소창 포함).
📌 **설명 포인트**: 컨테이너는 격리돼 있어 내부 5000 포트가 호스트에서 바로 안 보임. `-p`로 호스트 포트와 컨테이너 포트를 연결해야 접속 가능.

```bash
# 정리
docker rm -f web-8080 web-8081
```

---

## 7-A. 바인드 마운트 (호스트 변경 즉시 반영)

호스트의 폴더/파일을 컨테이너 안으로 연결. 호스트에서 바꾸면 컨테이너 안에도 반영됨.

```bash
cd /path/to/codyssey-workstation

# 호스트에 정적 파일 하나 준비
mkdir -p public
echo "<h1>version 1</h1>" > public/index.html

# 호스트의 public 폴더를 컨테이너 /mnt 로 바인드 마운트
docker run -d -p 8082:5000 \
  -v "$(pwd)/public":/mnt \
  --name bind-test codyssey-web:1.0

# [변경 전] 컨테이너 안에서 파일 확인
docker exec bind-test cat /mnt/index.html

# 호스트에서 파일 수정
echo "<h1>version 2 (changed on host)</h1>" > public/index.html

# [변경 후] 컨테이너 안에서 다시 확인 -> 재빌드 없이 반영됨
docker exec bind-test cat /mnt/index.html

# 정리
docker rm -f bind-test
```

✅ **README에 남길 것**: 변경 전/후 `cat` 출력 비교.
📌 바인드 마운트 = "호스트 경로"를 그대로 연결 → 개발 중 코드/콘텐츠 즉시 반영에 유용.

---

## 7-B. Docker 볼륨 (데이터 영속성)

컨테이너를 삭제해도 데이터가 남는지 검증. (앱의 `/count` 가 `/data/count.txt`에 기록함)

```bash
# 볼륨 생성
docker volume create mydata
docker volume ls

# 볼륨을 /data 에 연결해서 실행
docker run -d -p 8083:5000 -v mydata:/data --name vol-test codyssey-web:1.0

# 몇 번 접속해서 카운트를 파일에 기록
curl http://localhost:8083/count
curl http://localhost:8083/count
curl http://localhost:8083/count   # {"count": 3, ...}

# [삭제 전] 데이터 확인
docker exec vol-test cat /data/count.txt

# 컨테이너 완전 삭제
docker rm -f vol-test

# 같은 볼륨으로 새 컨테이너 실행
docker run -d -p 8083:5000 -v mydata:/data --name vol-test2 codyssey-web:1.0

# [삭제 후] 데이터가 그대로 남아있는지 확인
docker exec vol-test2 cat /data/count.txt   # 여전히 3
curl http://localhost:8083/count            # {"count": 4, ...} 이어서 증가

# 정리
docker rm -f vol-test2
# (볼륨까지 지우려면) docker volume rm mydata
```

✅ **README에 남길 것**: 컨테이너 삭제 전/후 `count.txt` 값이 유지됨을 보이는 출력.
📌 **설명 포인트**: 컨테이너는 일회용(삭제 시 내부 데이터 소멸). 볼륨은 컨테이너와 수명이 분리되어 데이터가 영속됨.

---

## 8. Git 설정 + GitHub 연동

```bash
# 사용자 정보 설정
git config --global user.name "본인이름"
git config --global user.email "본인이메일@example.com"

# 기본 브랜치를 main 으로
git config --global init.defaultBranch main

# 설정 확인
git config --list
```

프로젝트를 저장소로 만들고 커밋:

```bash
cd /path/to/codyssey-workstation

git init
git add .
git commit -m "feat: 개발 워크스테이션 실습 산출물"
```

GitHub 연동 (둘 중 하나):

```bash
# GitHub에서 빈 저장소를 먼저 만든 뒤, HTTPS 주소로 연결
git remote add origin https://github.com/본인계정/저장소이름.git
git branch -M main
git push -u origin main
```

또는 **VSCode**에서: 좌측 Source Control 패널 → "Publish to GitHub" → GitHub 로그인 → 저장소 생성/푸시.

✅ **README에 남길 것**: `git config --list` 출력(이메일은 마스킹 가능), VSCode GitHub 로그인/연동 스크린샷.
📌 **설명 포인트**: Git = 내 컴퓨터의 로컬 버전관리. GitHub = 원격 저장·협업 플랫폼. `push`로 로컬 커밋을 원격에 올림.

---

## 9. 보안 체크 (제출 전 필수)

- [ ] 스크린샷/로그에 토큰, 비밀번호, 개인키, 인증코드가 없는지 확인 (있으면 가림 처리)
- [ ] `.env`, `*.key`, `id_rsa` 등은 `.gitignore`로 커밋 제외 (이미 설정됨)
- [ ] 실수로 올린 민감정보가 있다면 즉시 삭제 후 재발급

---

## 10. 제출 전 최종 정리

```bash
# 남은 실습 컨테이너 정리
docker ps -a
docker rm -f $(docker ps -aq)   # (필요 시) 전체 컨테이너 삭제

# 최종 커밋 & 푸시
git add .
git commit -m "docs: README 실습 로그/증거 정리"
git push
```

제출: **GitHub 저장소 링크**. README만 보고 평가자가 전 과정을 따라올 수 있으면 완료입니다.
