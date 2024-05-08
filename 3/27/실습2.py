class Account:  # 클래스 이름은 대문자로 시작하는 것이 파이썬의 관례입니다.
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, money):  # self 매개변수 추가
        if money < 0:
            print("금액은 양수여야 합니다.")
            return
        self.balance += money
        print(f"{money}원이 입금되었습니다.")

    def withdraw(self, money):  # self 매개변수 추가
        if money > self.balance:
            print("출금 금액이 잔액을 초과하거나 잘못 입력 되었습니다.")
            return
        self.balance -= money
        print(f"{money}원이 출금되었습니다.")

    def check_balance(self):
        print(f"{self.owner}님의 계좌 잔액은 {self.balance}원입니다.")  # f-string 수정 및 메소드 이름 오타 수정


# account1 = Account("종섭",10000) 
# account1.check_balance()
# account1.deposit(5000)
# account1.withdraw(25000)

