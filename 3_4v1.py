import json
import os

#level 1
def register(login, password, filename="users.json"):

    user_data = {
        "login": login,
        "password": password
    }
    
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(user_data, file, ensure_ascii=False, indent=4)
    
    print(f"Пользователь {login} успешно зарегистрирован!")
    print(f"Данные сохранены в файл {filename}")

print("РЕГИСТРАЦИЯ ПОЛЬЗОВАТЕЛЯ")
login = input("Введите логин: ")
password = input("Введите пароль: ")

register(login, password)

#level 2
def register(login, password, filename="users.json"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            users = json.load(file)
            if not isinstance(users, list):
                users = [users]
    except (FileNotFoundError, json.JSONDecodeError):
        users = []
    
    for user in users:
        if user.get("login") == login:
            print(f"Ошибка! Пользователь с логином '{login}' уже существует.")
            return False

    new_user = {
        "login": login,
        "password": password
    }
    users.append(new_user)
    
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(users, file, ensure_ascii=False, indent=4)
    
    print(f"Пользователь {login} успешно зарегистрирован!")
    return True

print("РЕГИСТРАЦИЯ ПОЛЬЗОВАТЕЛЯ")
login = input("Логин: ")
password = input("Пароль: ")

register_user(login, password)

#level 3
def login_user(login, password, filename="users.json"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            users = json.load(file)
            
            if not isinstance(users, list):
                users = [users]
            
            for user in users:
                if user.get("login") == login and user.get("password") == password:
                    print(f"Добро пожаловать, {login}!")
                    return True
            
            print("Неверный логин или пароль!")
            return False