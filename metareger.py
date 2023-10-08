from tkinter import Tk, Label, Entry, Button
from eth_account import Account
import secrets
import os

def generate_keys():
    num_keys = int(entry.get())

    keys = []

    for i in range(num_keys):
        priv = secrets.token_hex(32)
        private_key = priv
        acct = Account.from_key(private_key)
        keys.append(private_key)

    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    file_path = os.path.join(desktop, "keys.txt")

    with open(file_path, 'w') as f:
        for key in keys:
            f.write(f"{key}\n")

    success_label.config(text=f"{num_keys} ключ(ей) сгенерирован(ы) и сохранен(ы) на рабочем столе!")

app = Tk()
app.title("Генератор ключей Ethereum")

label = Label(app, text="Введите количество ключей:")
label.pack(pady=10)

entry = Entry(app)
entry.pack(pady=5)

button = Button(app, text="Запуск", command=generate_keys)
button.pack(pady=20)

success_label = Label(app, text="")
success_label.pack(pady=10)

app.mainloop()
