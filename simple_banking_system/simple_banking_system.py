import random
import sqlite3


class BankingSystem:
    def __init__(self):
        self.conn = sqlite3.connect('card.s3db')
        self.cur = self.conn.cursor()
        self.cur.execute('DROP TABLE card')
        self.cur.execute('''CREATE TABLE IF NOT EXISTS card (
        id INTEGER constraint p_k primary key, 
        number TEXT, 
        pin TEXT, 
        balance INTEGER DEFAULT 0)''')

    def luhn_al_test(self, card_num):
        drop = card_num[:15]
        multiply = [int(drop[n]) * 2 if n % 2 == 0 else int(drop[n]) for n in range(len(drop))]
        n_more_9 = [n - 9 if n > 9 else n for n in multiply]
        n_sum = sum(n_more_9)
        checksum = card_num[15:]
        return checksum == str((10 - n_sum % 10) % 10)

    def create_info(self, card_num, pin_num):
        print()
        print("Your card has been created")
        print("Your card number:")
        print(card_num)
        print("Your card PIN:")
        print(pin_num)
        print()

    def main_menu(self):
        print("1. Create an account")
        print("2. Log into account")
        print("0. Exit")

    def generate_account(self):
        acc = ""
        while len(acc) < 9:
            acc += str(random.randint(0, 9))
        drop_l_n = "400000" + acc
        multiply = [int(drop_l_n[n]) * 2 if n % 2 == 0 else int(drop_l_n[n]) for n in range(len(drop_l_n))]
        n_more_9 = [n - 9 if n > 9 else n for n in multiply]
        n_sum = sum(n_more_9)
        if n_sum % 10 == 0:
            checksum = "0"
        else:
            checksum = str(10 - n_sum % 10)
        n_card = "400000" + acc + checksum
        return n_card

    def generate_pin(self):
        pin = ""
        while len(pin) < 4:
            pin += str(random.randint(0, 9))
        return pin

    def add_acc_to_db(self, acc, _pin):
        self.cur.execute('INSERT INTO card (number, pin) VALUES (?, ?)', (acc, _pin))
        self.conn.commit()

    def valid_or_not(self, acc, _pin):
        pair_card_pin = self.cur.execute(
            'SELECT id FROM card WHERE number IN (?) AND pin IN (?)', (acc, _pin))
        if list(pair_card_pin):
            return True
        return False

    def log_in_menu(self):
        print("1. Balance")
        print("2. Add income")
        print("3. Do transfer")
        print("4. Close account")
        print("5. Log out")
        print("0. Exit")

    def check_balance(self, acc):
        self.cur.execute('SELECT balance FROM card WHERE number = {}'.format(acc))
        bal = self.cur.fetchone()[0]
        return bal

    def add_income(self, income, acc):
        self.cur.execute("UPDATE card SET balance = balance + ? WHERE number = ?",
                         (income, acc))
        self.conn.commit()
        print("Income was added!")
        print()

    def transfer_process(self, acc):
        print("Transfer")
        trans_card = input("Enter card number:\n")
        if self.luhn_al_test(trans_card):
            if trans_card != acc:
                self.cur.execute('SELECT * FROM card WHERE number = {}'.format(trans_card))
                row = self.cur.fetchone()
                if row is not None:
                    trans_money = int(input("Enter how much money you want to transfer:\n"))
                    balance = self.check_balance(acc)
                    if trans_money <= balance:
                        self.cur.execute("UPDATE card SET balance = balance + ? WHERE number = ?",
                                         (trans_money, trans_card))
                        self.conn.commit()
                        self.cur.execute("UPDATE card SET balance = balance - ? WHERE number = ?",
                                         (trans_money, acc))
                        self.conn.commit()
                        print("Success!")
                        print()
                    else:
                        print("Not enough money!")
                        print()
                else:
                    print("Such a card does not exist.")
                    print()
            else:
                print("You can't transfer money to the same account!")
                print()
        else:
            print("Probably you made mistake in the card number. Please try again!")
            print()

    def delete_account(self, acc):
        self.cur.execute('DELETE FROM card WHERE number = {}'.format(acc))
        self.conn.commit()
        print("The account has been closed!")
        print()

    def account_management(self, acc):
        print()
        while True:
            self.log_in_menu()
            log_choice = input()
            print()
            if log_choice == "1":
                card_balance = self.check_balance(acc)
                print("Balance:", card_balance)
                print()
            elif log_choice == "2":
                income = int(input('Enter income:\n'))
                self.add_income(income, acc)
            elif log_choice == '3':
                self.transfer_process(acc)
            elif log_choice == "4":
                self.delete_account(acc)
                break
            elif log_choice == "5":
                print("You have successfully logged out!")
                print()
                break
            elif log_choice == "0":
                print("Bye!")
                exit()

    def card_management(self):
        while True:
            self.main_menu()
            choice = input()
            if choice == "1":
                account = self.generate_account()
                pin = self.generate_pin()
                self.add_acc_to_db(account, pin)
                self.create_info(account, pin)

            elif choice == '2':
                current_account = input("Enter your card number:\n")
                current_acc_pin = input("Enter your PIN:\n")
                print()
                if self.valid_or_not(current_account, current_acc_pin):
                    print("You have successfully logged in!")
                    self.account_management(current_account)
                else:
                    print("Wrong card number or PIN!")
                    print()
            elif choice == "0":
                break
        print("Bye!")


bank = BankingSystem()
bank.card_management()
