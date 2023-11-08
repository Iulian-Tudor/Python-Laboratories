class Account:
    def __init__(self, account_adress, funds=0):
        self.account_adress = account_adress
        self.funds = funds

    def deposit(self, amount):
        self.funds += amount

    def withdraw(self, amount):
        if amount > self.funds:
            print("N-ai bani, amaratule!")
        else:
            self.funds -= amount

    def calculate_interest(self):
        pass


class SavingsAccount(Account):
    def __init__(self, account_adress, funds=0, interest_rate=0.01):
        super().__init__(account_adress, funds)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.funds * self.interest_rate


class CheckingAccount(Account):
    def __init__(self, account_adress, funds=0, interest_rate=5):
        super().__init__(account_adress, funds)
        self.interest_rate = interest_rate

    def withdraw(self, amount):
        if amount > self.funds:
            print("N-ai bani, amaratule!")
        else:
            self.funds -= amount + self.interest_rate


def main():
    savings_account = SavingsAccount("SAV-001", 1000)
    savings_account.deposit(500)
    print(savings_account.calculate_interest())
    savings_account.withdraw(2000)
    print(savings_account.funds)

    checking_account = CheckingAccount("CHK-001", 1000)
    checking_account.deposit(500)
    print(checking_account.funds)
    checking_account.withdraw(2000)
    print(checking_account.funds)


main()