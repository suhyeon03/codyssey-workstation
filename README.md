# 내 컴퓨터에 개발자용 '작업실' 꾸미기

> 실습을 진행하면서 아래 `_______` / `(붙여넣기)` 부분을 실제 명령어·출력·스크린샷으로 채우세요.
> 실습 순서와 명령어는 [GUIDE.md](./GUIDE.md) 참고.

## 1) 프로젝트 개요
로컬 개발 워크스테이션을 구축하는 미션. 리눅스 CLI(터미널), Docker(컨테이너),
Git/GitHub(버전관리·협업)를 사용해 "재현 가능한 실행 환경"을 만든다.
간단한 Flask 웹서버를 Dockerfile로 컨테이너화하고, 포트 매핑·바인드 마운트·볼륨으로
동작을 직접 검증한다.

## 2) 실행 환경
- OS: macOS _______ (예: Sequoia 15.x)
- Shell: zsh
- 터미널: _______ (예: iTerm2 / 기본 터미널)
- 컨테이너 런타임: OrbStack (Docker 엔진 제공)
- Docker: `docker --version` 결과 → _______
- Git: `git --version` 결과 → _______

## 3) 수행 항목 체크리스트
- [ ] 터미널 기본 조작 및 폴더 구성
- [ ] 권한 변경 실습 (파일 1 + 디렉토리 1)
- [ ] Docker 설치/점검 (`docker --version`, `docker info`)
- [ ] hello-world / ubuntu 컨테이너 실행
- [ ] Dockerfile 커스텀 이미지 빌드/실행
- [ ] 포트 매핑 접속(2회)
- [ ] 바인드 마운트 반영
- [ ] 볼륨 영속성
- [ ] Git 설정 + GitHub/VSCode 연동

---

## 4) 수행 로그 및 검증

### 4-1. 터미널 기본 조작
검증: 아래 명령으로 생성/복사/이동/삭제가 정상 동작함을 확인.
```bash
(붙여넣기: pwd / ls -la / mkdir / touch / cp / mv / rm 등 명령과 출력)
```
> 절대경로 vs 상대경로 설명: _______

### 4-2. 권한 실습
검증: `chmod` 전/후 `ls -l` 비교.
```bash
(붙여넣기: 변경 전 ls -l)
(붙여넣기: chmod 755 / chmod 700)
(붙여넣기: 변경 후 ls -l)
```
> r/w/x 및 755·644 해석: _______

### 4-3. Docker 설치/점검
```bash
(붙여넣기: docker --version)
(붙여넣기: docker info 발췌)
```

### 4-4. 컨테이너 실행 실습
```bash
(붙여넣기: docker run hello-world)
(붙여넣기: ubuntu 진입 후 ls/echo)
(붙여넣기: docker ps / ps -a / images / logs / stats)
```
> attach vs exec 차이 관찰: _______

### 4-5. Dockerfile 커스텀 이미지
- 선택한 베이스: `python:3.12-slim` (B안 — Linux 베이스 + 기능 추가)
- 커스텀 포인트:
  - `LABEL` 이미지 메타데이터 부여
  - `ENV PORT/DATA_DIR` 설정과 코드 분리
  - `HEALTHCHECK` 자가 상태 점검
  - `COPY app/` 애플리케이션 코드 주입
```bash
(붙여넣기: docker build -t codyssey-web:1.0 . 로그)
(붙여넣기: docker images | grep codyssey-web)
```

### 4-6. 포트 매핑 접속 증거 (2회)
```bash
(붙여넣기: docker run -d -p 8080:5000 ... + curl 결과)
(붙여넣기: docker run -d -p 8081:5000 ... + curl 결과)
```
> 브라우저 접속 스크린샷(주소창 포함):
> ![포트매핑 접속](스크린샷경로.png)

> 포트 매핑이 필요한 이유: _______

### 4-7. 바인드 마운트 반영
```bash
(붙여넣기: -v $(pwd)/public:/mnt 실행)
(붙여넣기: 변경 전 cat)
(붙여넣기: 호스트에서 파일 수정 후 변경 후 cat)
```

### 4-8. 볼륨 영속성
```bash
(붙여넣기: docker volume create mydata)
(붙여넣기: 컨테이너 실행 + /count 접속)
(붙여넣기: 삭제 전 cat /data/count.txt)
(붙여넣기: docker rm -f + 새 컨테이너 재실행)
(붙여넣기: 삭제 후 cat /data/count.txt → 유지 확인)
```
> Docker 볼륨(영속 데이터) 설명: _______

### 4-9. Git 설정 + GitHub 연동
```bash
(붙여넣기: git config --list, 이메일은 마스킹 가능)
```
> VSCode GitHub 로그인/연동 스크린샷:
> ![GitHub 연동](스크린샷경로.png)

> Git vs GitHub 역할 차이: _______

---

## 5) 트러블슈팅 (2건 이상)

### 트러블슈팅 1: _______
- 문제: _______
- 원인 가설: _______
- 확인: _______
- 해결/대안: _______

### 트러블슈팅 2: _______
- 문제: _______
- 원인 가설: _______
- 확인: _______
- 해결/대안: _______

---

## 6) 보안 확인
- [ ] 로그/스크린샷에 토큰·비밀번호·개인키·인증코드 없음(마스킹 완료)
- [ ] `.env`, `*.key`, `id_rsa` 등은 `.gitignore`로 제외됨
