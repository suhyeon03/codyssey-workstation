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

def get_default_quizzes():
    """파일이 없을 때 사용할 기본 퀴즈 목록 (파이썬/Git 주제)"""
    return [
        Quiz("파이썬에서 리스트를 만들 때 쓰는 기호는?",
            ["( )", "[ ]", "{ }", "< >"], 2),
        Quiz("정수를 나타내는 파이썬 자료형은?",
            ["str", "int", "bool", "list"], 2),
        Quiz("조건에 따라 다른 코드를 실행하는 키워드는?",
            ["for", "while", "if", "def"], 3),
        Quiz("함수를 정의할 때 쓰는 키워드는?",
             ["func", "def", "define", "fun"], 2),
        Quiz("Git에서 변경 이력을 저장(기록)하는 명령은?",
            ["git push", "git commit", "git status", "git log"], 2),
        Quiz("원격 저장소를 통째로 복제하는 Git 명령은?",
            ["git pull", "git clone", "git init", "git add"], 2),
    ]



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
            continue

        # 2. 숫자가 아닌 글자를 쳤을 때 (예: abc)
        if not raw.isdigit():   # isdigit() = '숫자로만 이뤄졌나?' True/False
            print("숫자만 입력할 수 있습니다.")
            continue

        number = int(raw)

        if number < min_value or number > max_value:
            print(f"{min_value}부터 {max_value} 사이 숫자를 입력해주세요.")
            continue

        return number

def play_quiz(quizzes):
    print("\n===== 퀴즈 풀기 =====")
    if len(quizzes) == 0:
        print("등록된 퀴즈가 없습니다.")
        return 0

    score = 0
    for quiz in quizzes:
        print()
        quiz.show()
        answer = read_input("정답 번호를 입력하세요: ", 1, 4)
        if quiz.is_correct(answer):
            print("정답입니다!")
            score = score + 1
        else:
            print(f"틀렸어요. 정답은 {quiz.answer}번 입니다.")

    print(f"\n결과: 총 {len(quizzes)}문제 중 {score}문제 정답!")
    return score


def main():
    quizzes = get_default_quizzes()

    while True:
        print(MENU)
        try:
            choice = read_input("메뉴 번호를 선택하세요: ", 1, 5)
        except (KeyboardInterrupt, EOFError):
            print("\n입력이 중단되어 프로그램을 종료합니다.")
            break

        if choice == 1:
            play_quiz(quizzes)
        elif choice == 2:
            print("[퀴즈 추가] - ")
        elif choice == 3:
            print("[퀴즈 목록] - ")
        elif choice == 4:
            print("[점수 확인] - ")
        elif choice == 5:
            print("게임을 종료합니다.")
            break
        input("\n계속하려면 Enter를 누르세요...")


if __name__ == "__main__":
    main()