class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question    # 문제 (글자)
        self.choices = choices      # 선택지 4개 (리스트)
        self.answer = answer        # 정답 번호 1~4 (숫자)

    def show(self):
            print(self.question)                 # 문제 출력
            for i in range(len(self.choices)):   # 선택지 개수만큼 반복
                print(f"{i + 1}. {self.choices[i]}")   # "1. 보기내용" 형태로 출력

    def is_correct(self, user_answer):
        return user_answer == self.answer    # 입력한 번호가 정답과 같으면 True




MENU = """ # 바뀌지 않는 값"이라는 관습적 표시
==============================
 파이썬 퀴즈 게임
==============================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
==============================
"""

def read_input(num, min_value, max_value):
    
    while True:
        raw = input(num)
        raw = raw.strip()  # 실수로 넣은 앞뒤 공백을 없앰

        # 1 아무것도 안 치고 Enter만 눌렀을 때
        if raw == '':
            print("아무것도 선택하지않았습니다.")
            countinue

        # 2. 숫자가 아닌 글자를 쳤을 때 (예: abc)
        if not raw.isdigit():   # isdigit() = '숫자로만 이뤄졌나?' True/False
            print("숫자만 입력할 수 있습니다.")
            continue

        number = int(raw)

        if number < min_value or number > max_value:
            print(f"{min_value}부터 {max_value} 사이 숫자를 입력해주세요.")
            continue

        return number

def main():
    while True:
        print(MENU)
        try:
            choice = read_input("메뉴 번호를 선택하세요: ", 1, 5)
        except (KeyboardInterrupt, EOFError):
            print("\n입력이 중단되어 프로그램을 종료합니다.")
            break

        if choice == 1:
            print("[퀴즈 풀기] - ")
        elif choice == 2:
            print("[퀴즈 추가] - ")
        elif choice == 3:
            print("[퀴즈 목록] - ")
        elif choice == 4:
            print("[점수 확인] - ")
        elif choice == 5:
            print("게임을 종료합니다.")
            break


if __name__ == "__main__":
    main()