import sqlite3
import random


def wellcome():
    print('\nActions: Authorization(1), Registration(2), Search account(3)')
    reg = input('What you want do: ')
    if reg.lower() == 'authorization' or reg == '1':
        print('\nAuthorization to your account:')
        user_id = int(input('Enter your user id: '))
        a = len(sql.execute('SELECT user_id FROM users_list;').fetchall())
        b = 0
        for i in sql.execute('SELECT user_id FROM users_list;').fetchall():
            b += 1
            if user_id in i:
                password = input('Enter your password: ')
                authorization(user_id, password)
            elif b == a:
                print('No registered user id')
    elif reg.lower() == 'registration' or reg == '2':
        print('\nRegistration of account:')
        registration()
    elif reg.lower() == 'search account' or reg == '3':
        how_search = input('By what value to search for an account?(Name(1) or Number(2)): ')
        num = 0
        if how_search.lower() == 'name' or how_search == '1':
            search = input('Enter name to find account: ')
            result_of_search = sql.execute(f'SELECT * FROM users_list WHERE name={search};').fetchall()
            for i in result_of_search:
                num += 1
                print(f'Account №{num}: User Id - {i[0]}, Phone number - {i[3]} ')
                wellcome()
        elif how_search.lower() == 'number' or how_search == '2':
            search = int(input('Enter number to find account: '))
            result_of_search = sql.execute(f'SELECT * FROM users_list WHERE number={search};').fetchall()
            num = 0
            for i in result_of_search:
                num += 1
                print(f'Account №{num}: User Id - {i[0]}, Name - {i[1]} ')
                wellcome()
        else:
            print('Error')
    else:
        print('Error')


def authorization(id, ps):
    if sql.execute(f'SELECT password FROM users_list WHERE user_id={id};').fetchone()[0] == ps:
        print(f'Wellcome to your account {sql.execute(f"SELECT name FROM users_list WHERE user_id={id};").fetchone()[0]}')
        bank_actions(id)
    else:
        print('Incorrect password! \nPls try again!')



def registration():
    set_name = input('Enter your name for account: ')
    set_password = input('Enter password for you account: ')
    set_number = int(input('Enter you phone number: '))
    while True:
        set_user_id = int(random.random() * 100000000)
        if set_user_id not in sql.execute(f'SELECT user_id FROM users_list;').fetchall():
            break
        else:
            pass
    print(f'Save your account id: {set_user_id}')
    sql.execute(f'INSERT INTO users_list(user_id, name, password, number, balance) VALUES({set_user_id}, "{set_name}", "{set_password}", {set_number}, 0); ')
    connection.commit()
    print('Your account successfully registered!')
    bank_actions(set_user_id)


def return_balance(id):
    bal = sql.execute(f"SELECT balance FROM users_list WHERE user_id={id};").fetchone()
    return bal[0]


def update_balance(id, new_bal):
    bal = sql.execute(f'UPDATE users_list SET balance={new_bal} WHERE user_id={id};')
    connection.commit()




def bank_actions(id):
    while True:
        print('\nActions: Look balance(1), Put money(2), Take of money(3), Deposit(4), Exit account(5)')
        action = input('Enter your action: ')
        if action.lower() == 'look balance' or action == '1':
            print(f'Your balance: {return_balance(id)}')
        elif action.lower() == 'put money' or action == '2':
            put = int(input('Enter how many money you want put: '))
            new_balance = return_balance(id) + put
            update_balance(id, new_balance)
            print('Balance updated')
        elif action.lower() == 'take of money' or action == '3':
            print(f'Your balance: {return_balance(id)}')
            take_off = int(input('Enter how many money you want take off: '))
            if take_off < return_balance(id):
                new_balance = return_balance(id) - take_off
                update_balance(id, new_balance)
                print('Balance updated')
            else:
                print('You haven\'t so many money!')
        elif action.lower() == 'deposit' or action == '4':
            print(f'Your balance: {return_balance(id)}')
            deposit = int(input('Enter how many money you want put on deposit: '))
            if deposit <= return_balance(id):
                dep = [12, 24, 36]
                time = int(input('How long to put money on deposit(12, 24 or 36 months): '))
                if time in dep:
                    deposit_money = deposit / 100 / 12 * time
                    new_balance = return_balance(id) + deposit_money
                    update_balance(id, new_balance)
                else:
                    print('Incorrect quantity of months!')
            else:
                print('You haven\'t so many money!')
        elif action.lower() == 'exit account' or action == '5':
            wellcome()
        else:
            print('Error')


connection = sqlite3.connect('bank.db')
sql = connection.cursor()
sql.execute('CREATE TABLE IF NOT EXISTS users_list(user_id INTEGER, name TEXT, password TEXT, number INTEGER, balance INTEGER);')
print('Wellcome in our Bank!')
wellcome()