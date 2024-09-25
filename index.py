from cryptography.fernet import Fernet


def write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as k:
        k.write(key)

write_key()
        

def load_key():
    file = open('key.key', "rb")
    key = file.read()
    file.close()
    return key



key = load_key()
fer = Fernet(key)

def view():
    with open('password.text', 'r') as f:
        for line in f:
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user.strip(), "| Password:", fer.decrypt(passw.strip().encode()).decode())

def add():
    name = input("Enter Account name: ")
    pwd = input("Enter Password: ")
    encrypted_pwd = fer.encrypt(pwd.encode())
    with open('password.text', 'a') as f:
        f.write(name + " | " + encrypted_pwd.decode() + '\n')

while True:
    mode = input("Would you like to add a new password or view existing ones (view, add)? Press q to Quit: ").lower()

    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode")