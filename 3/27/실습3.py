from 실습2 import Account  

class Upgrade_Account(Account):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)  
        self.interest_rate = interest_rate 
        self.balance += self.balance * (self.interest_rate / 100) 

    def check_interest_rate(self):
        print(f"이자율: {self.interest_rate}%")  

    def print_interest_rate(self):
        plus_money = self.balance * (self.interest_rate / 100) 
        print(f"{self.owner}님의 계좌에 {plus_money}원의 이자가 추가되었습니다.")  

js_account = Upgrade_Account("종섭", 10000, 5)  
js_account.check_balance()  
js_account.deposit(5000)
js_account.check_interest_rate()  
js_account.print_interest_rate()  
js_account.check_balance() 
