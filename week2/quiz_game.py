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



MENU = """ 
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

class QuizGame:
    def __init__(self):
        self.quizzes = get_default_quizzes()
        self.best_score = None

    def play_quiz(self):
        print("\n===== 퀴즈 풀기 =====")
        if len(self.quizzes) == 0:
            print("등록된 퀴즈가 없습니다.")
            return 0

        score = 0
        for quiz in self.quizzes:
            print()
            quiz.show()
            answer = read_input("정답 번호를 입력하세요: ", 1, 4)
            if quiz.is_correct(answer):
                print("정답입니다!")
                score = score + 1
            else:
                print(f"틀렸어요. 정답은 {quiz.answer}번 입니다.")

        print(f"\n결과: 총 {len(self.quizzes)}문제 중 {score}문제 정답!")

        if self.best_score is None or score > self.best_score:
                self.best_score = score
                print("최고 점수를 갱신했습니다!")

    def add_quiz(self):
        print("\n===== 퀴즈 추가 =====")

        question = input("문제를 입력하세요: ").strip()
        if question == "":
            print("문제가 비어 있어 추가를 취소합니다.")
            return

        choices = []                          # 선택지를 담을 빈 리스트
        for i in range(4):                     # 4번 반복해서 보기 4개 받기
            choice = input(f"{i + 1}번 선택지: ").strip()
            if choice == "":
                print("선택지가 비어 있어 추가를 취소합니다.")
                return
            choices.append(choice)            # 받은 보기를 리스트에 추가

        answer = read_input("정답 번호(1~4): ", 1, 4)

        new_quiz = Quiz(question, choices, answer)   # 입력값으로 Quiz 하나 생성
        self.quizzes.append(new_quiz)                      # 퀴즈 목록에 추가
        print("새 퀴즈가 추가되었습니다!")

    def show_quiz_list(self):
        print("\n===== 퀴즈 목록 =====")
        if len(self.quizzes) == 0:                       # 퀴즈가 없으면
            print("등록된 퀴즈가 없습니다.")
            return

        for i in range(len(self.quizzes)):               # 퀴즈 개수만큼 반복
            print(f"{i + 1}. {self.quizzes[i].question}")   # 번호 + 문제 출력

    def show_score(self):
        print("\n===== 점수 확인 =====")
        if self.best_score is None:                  # 아직 한 번도 안 풀었으면
            print("아직 퀴즈를 풀지 않았습니다.")
        else:
            print(f"최고 점수: {self.best_score}점")


    def run(self):

        while True:
            print(MENU)
            try:
                choice = read_input("메뉴 번호를 선택하세요: ", 1, 5)
            except (KeyboardInterrupt, EOFError):
                print("\n입력이 중단되어 프로그램을 종료합니다.")
                break

            if choice == 1:
                self.play_quiz()
            elif choice == 2:
                self.add_quiz()
            elif choice == 3:
                self.show_quiz_list()
            elif choice == 4:
                self.show_score()
            elif choice == 5:
                print("게임을 종료합니다.")
                break
            input("\n계속하려면 Enter를 누르세요...")


if __name__ == "__main__":
    game = QuizGame()
    game.run()