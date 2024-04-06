from random import randint
from sys import exit

#parent class
class User():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

#child class
class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name,age,gender,)
        self.balance = 0
        self.acc_number = {}

    def User_details(self):
        print( self.name,self.age,self.gender,self.acc_number)


    def get_account(self):
            acc_number = 0
            for i in range(1):
                acc_number = randint(1000000,9999999)
                if self.name not in self.acc_number.keys():
                    self.acc_number[self.name] = acc_number
                else:
                    return self.acc_number


    def deposit(self):
        amount = int(input("How much do you want to deposit? "))
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self):
        while True:
            widthraw_amount = int(input('enter amount to withdraw: '))

            if self.balance > widthraw_amount:
                self.balance = self.balance - widthraw_amount
                print('your new balance is', self.balance)
                break
            else:
                print(f'your widthdraw amount exceeds {self.balance} choose amount less than {self.balance}')

    def transfer(self):
        transfer_amount = int(input("How much do you want to transfer? "))
        if self.balance >= transfer_amount:
            new_account = int(input("enter account number you'd like to transfer funds too: "))
            if new_account in self.acc_number.keys():
                self.balance = self.balance - transfer_amount
                print('your new balance is', self.balance)
        else:
            print(f'you do not have sufficient funds')

def menu():
        print('Menu')
        print('[1] Deposit')
        print('[2] Withdraw')
        print('[3] Transfer')
        print('[4] User info')
        print('[5] Exit')


def main():
    account_create = input('Welcome to Morgan Bank would you like to create an account? ')

    if account_create == "yes":
        User_input = Bank(input('enter name? '), int(input('age? ')), input('gender? '))
        User_input.get_account()
        User_input.User_details()
        while True:
            menu()
            user_select = int(input('Enter your choice: '))
            if user_select == 1:
                User_input.deposit()
            if user_select == 2:
                User_input.withdraw()
            if user_select == 3:
                User_input.transfer()
            if user_select == 4:
                User_input.User_details()
            if user_select == 5:
                print('Thank you for using Morgan bank')
                exit()



if __name__ == '__main__':
    main()

