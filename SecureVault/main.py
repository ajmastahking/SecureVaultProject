import json
from pathlib import Path

FILE = Path(__file__).with_name('passwords.json')


def load_passwords():
    if not FILE.exists():
        return {}
    try:
        with FILE.open('r', encoding='utf-8') as file:
            data = json.load(file)
        return data if isinstance(data, dict) else {}
    except (json.JSONDecodeError, OSError):
        print('Could not read passwords.json. Starting with an empty list.')
        return {}


def save_passwords(passwords):
    with FILE.open('w', encoding='utf-8') as file:
        json.dump(passwords, file, indent=4)


def add_account(passwords):
    name = input('Account name: ').strip()
    if not name:
        print('Account name cannot be empty.')
        return
    if name in passwords:
        print('That account already exists.')
        return
    username = input('Username: ').strip()
    password = input('Password (use a fake one): ')
    passwords[name] = {'username': username, 'password': password}
    save_passwords(passwords)
    print('Account saved!')


def view_accounts(passwords):
    if not passwords:
        print('No accounts saved yet.')
        return
    for name, info in passwords.items():
        print(f'\nAccount: {name}')
        print(f'Username: {info["username"]}')
        print(f'Password: {info["password"]}')


def search_account(passwords):
    name = input('Account name to search: ').strip()
    info = passwords.get(name)
    if info is None:
        print('Account not found.')
    else:
        print(f'Username: {info["username"]}')
        print(f'Password: {info["password"]}')


def delete_account(passwords):
    name = input('Account name to delete: ').strip()
    if name not in passwords:
        print('Account not found.')
        return
    confirm = input(f'Delete {name}? (yes/no): ').strip().lower()
    if confirm == 'yes':
        del passwords[name]
        save_passwords(passwords)
        print('Account deleted!')
    else:
        print('Deletion canceled.')


def main():
    passwords = load_passwords()
    while True:
        print('\n=== SecureVault Beginner ===')
        print('1. Add account')
        print('2. View accounts')
        print('3. Search account')
        print('4. Delete account')
        print('5. Exit')
        choice = input('Choose 1-5: ').strip()
        if choice == '1':
            add_account(passwords)
        elif choice == '2':
            view_accounts(passwords)
        elif choice == '3':
            search_account(passwords)
        elif choice == '4':
            delete_account(passwords)
        elif choice == '5':
            print('Goodbye!')
            break
        else:
            print('Invalid choice. Try again.')


if __name__ == '__main__':
    main()
